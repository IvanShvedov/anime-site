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

        ctx = {}
        return render(request, 'anime_page.html', context=ctx)