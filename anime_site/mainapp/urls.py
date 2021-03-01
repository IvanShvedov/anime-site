from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('anime/<str:slug>', views.AnimeView.as_view(), name='anime_page'),
    path('genres/<str:slug>', views.GengerView.as_view(), name='genres_page'),
    path('studio/<str:slug>', views.StudioView.as_view(), name='studio_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
