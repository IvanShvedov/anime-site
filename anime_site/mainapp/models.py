from django.db import models

from .choices import *


class Anime(models.Model):

    title = models.CharField(max_length=100, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    image_url = models.URLField(verbose_name='Ссылка на картинку')
    genres = models.ManyToManyField('Genre', verbose_name='Жанры')
    year = models.DateField(verbose_name='Год')
    author = models.ForeignKey('Author', verbose_name='Автор', on_delete=models.CASCADE)
    season = models.CharField(max_length=10, choices=SEASONS)
    age_raiting = models.CharField(max_length=30, choices=RATING)
    episodes = models.ManyToManyField('Episode', verbose_name='Эпизоды')

    def __str__(self):
        return self.title


class Episode(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Наименование эпизода')
    video_url = models.URLField(verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title


class Author(models.Model):
    pass


class Genre(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование жанра')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name