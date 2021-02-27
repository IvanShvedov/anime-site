from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('anime/<str:slug>/', views.AnimeView.as_view(), name='anime page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
