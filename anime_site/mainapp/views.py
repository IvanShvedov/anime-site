import json
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from django.core.serializers import serialize
from django.http.response import HttpResponse, JsonResponse

from .models import *


class MainView(View):

    def get(self, request):
        animes = []
        all_anime = Anime.objects.all()
        for anime in all_anime:
            authors = anime.author.all()
            genres = anime.genres.all()
            animes.append({
                'anime': anime,
                'authors': authors,
                'genres': genres
            })
        ctx = {
            'animes': animes,
            'user': request.user
        }
        return render(request, 'main_page.html', context=ctx)


class AnimeView(View):
    
    def get(self, request, *args, **kwargs):
        anime = Anime.objects.get(slug=kwargs.get('slug'))
        genres = anime.genres.all()
        authors = anime.author.all()
        episodes = Episode.objects.filter(anime=anime)
        ctx = {
            'anime': anime,
            'genres': genres,
            'authors': authors,
            'episodes': episodes
        }
        return render(request, 'anime_page.html', context=ctx)


class GenreView(View):

    def get(self, request, *args, **kwargs):
        animes = []
        slug = kwargs.get('slug')
        genre_filter = Genre.objects.get(slug=slug)
        all_anime = Anime.objects.filter(genres=genre_filter)
        for anime in all_anime:
            genres = anime.genres.all()
            authors = anime.author.all()
            animes.append({
                'anime': anime,
                'authors': authors,
                'genres': genres
            })
        ctx = {
            'filter': genre_filter.name,
            'animes': animes
        }
        return render(request, 'genres.html', context=ctx)


class GenresListView(View):

    def get(self, request):
        genres = Genre.objects.all()
        body = serialize('json', genres)
        return JsonResponse(body, safe=False)


class StudioView(View):

    def get(self, request, *args, **kwargs):
        pass


class AccountView(View):

    def get(self, request, *args, **kwargs):
        animes = []
        if request.user:
            all_anime = Library.objects.filter(user=request.user)
            ctx={}
            for anime in all_anime:
                print(anime)
                an = Anime.objects.get(title = anime.anime)
                authors = anime.anime.author.all()
                genres = anime.anime.genres.all()
                animes.append({
                    'anime': an,
                    'authors': authors,
                    'genres': genres
                })
            ctx = {
                'animes': animes,
            }
            return render(request, 'account.html', context=ctx)


class LoginView(View):

    def get(self, request,):
        ctx = {}
        return render(request, 'login_form.html')

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.POST['name'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main')
            else:
                return render(request, 'login_form.html', context={'status': False, 'msg': 'Пользователь не активен'})
        else:
            return render(request, 'login_form.html', context={'status': False, 'msg': 'Такого пользователя нету'})


def log_out(request):
    logout(request)
    return redirect('main')


class RegView(View):

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, 'register_form.html', context=ctx)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.create_user(request.POST['name'], request.POST['e-mail'], request.POST['password'])
            user.save()
        except IntegrityError:
            return render(request, 'register_form.html', context={'msg': 'Пользователь с таким именем уже существует'})
        return redirect('main')


class CommentView(View):

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode("utf-8"))

            if data['comment'] != None and data['comment'] != '':
                anime = Anime.objects.get(slug=data['anime'])
                comment = Comment.objects.create(
                    user = request.user,
                    anime = anime,
                    comment = data['comment']
                )
                comment.save()
        except Exception as e:
            print(e)
        return HttpResponse(content="success")

    def get(self, request, *args, **kwargs):
        anime = Anime.objects.get(slug=request.GET['slug'])
        comments = Comment.objects.filter(anime=anime)
        body = []
        for comment in comments:
            body.append({
                'comment': comment.comment,
                'user': comment.user.username
                }
            )
        return JsonResponse(body, safe=False)


class GradeView(View):

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            if data['grade'] != None and data['grade'] != '':
                anime = Anime.objects.get(slug=data['anime'])
                grade = Grade.objects.get(user=request.user, anime=anime)
                grade.grade = data['grade']
                grade.save()
        except Grade.DoesNotExist:
            data = json.loads(request.body.decode('utf-8'))
            if data['grade'] != None and data['grade'] != '':
                anime = Anime.objects.get(slug=data['anime'])
                grade = Grade.objects.create(
                    user = request.user,
                    anime = anime,
                    grade = data['grade']
                )
                grade.save()
        return HttpResponse(content="success")

    def get(self, request):
        try:
            anime = Anime.objects.get(slug=request.GET['slug'])
            grade = Grade.objects.get(anime=anime, user=request.user)
            body = {
                'grade': grade.grade
            }
        except TypeError:
            return HttpResponse(content="fail")
        return JsonResponse(body, safe=False)

    
class LibraryView(View):

    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            if data['slug'] != None and data['slug'] != '':
                anime = Anime.objects.get(slug=data['slug'])
                lib = Library.objects.get_or_create(user=request.user, anime=anime)
        except Library.DoesNotExist:
            pass
        except Anime.DoesNotExist:
            return HttpResponse(content="fail")
        return HttpResponse(content="success")

    def get(self, request):
        try:
            anime = Anime.objects.get(slug=request.GET['slug'])
            lib = Library.objects.get(anime=anime, user=request.user)
        except Library.DoesNotExist:
            return HttpResponse(content="fail to get lib", status=404)
        except Anime.DoesNotExist:
            return HttpResponse(content="fail to get anime", status=404)
        return HttpResponse(status=200)

    def delete(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            if data['slug'] != None and data['slug'] != '':
                anime = Anime.objects.get(slug=data['slug'])
                lib = Library.objects.get(user=request.user, anime=anime)
                lib.delete()
        except Anime.DoesNotExist:
            return HttpResponse(content="fail")
        return HttpResponse(content="success")
        