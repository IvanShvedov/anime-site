from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .choices import *



def get_anime_url(obj, viewname: str):
    ct_model = obj.__class__._meta.model_name
    return reversed(viewname, kwargs = {'ct_model': ct_model, 'slug': obj.slug})


class Anime(models.Model):

    title = models.CharField(max_length=100, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    image_url = models.URLField(verbose_name='Ссылка на картинку')
    genres = models.ManyToManyField('Genre', verbose_name='Жанры')
    year = models.DateField(verbose_name='Год')
    author = models.ManyToManyField('Author', verbose_name='Автор')
    season = models.CharField(max_length=10, choices=SEASONS)
    age_raiting = models.CharField(max_length=30, choices=RATING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return get_anime_url(self, 'anime')


class Episode(models.Model):
    
    anime = models.ForeignKey(Anime, verbose_name='Аниме', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Наименование эпизода')
    number = models.PositiveIntegerField(verbose_name='Номер серии', null=True)
    video_url = models.URLField(verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title


class Author(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Имя автора')
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование жанра')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, verbose_name='Аниме', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий')
    pub_date = models.DateTimeField(verbose_name='Дата комментария')

    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return f"User: {self.user}, comment: {self.comment}"


class Grade(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, verbose_name='Аниме', on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(verbose_name='Оценка')

    def __str__(self):
        return f"User: {self.user}, grade: {self.grade}"


class Library(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, verbose_name='Аниме', on_delete=models.CASCADE)

    def __str__(self):
        return f"UserL {self.user}, anime: {self.anime}"