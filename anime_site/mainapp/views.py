from django.shortcuts import render
from django.views.generic import View
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
            'animes': animes
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
        pass


class StudioView(View):

    def get(self, request, *args, **kwargs):
        pass 