import json
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers

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


class GengerView(View):

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


class StudioView(View):

    def get(self, request, *args, **kwargs):
        pass


class AccountView(View):

    def get(self, request, *args, **kwargs):
        if request.user:
            ctx={}
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
        data = serializers.serialize('json', comments)
        return JsonResponse(data, safe=False)