from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('anime/<str:slug>/', views.AnimeView.as_view(), name='anime page'),
]
