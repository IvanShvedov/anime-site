from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('anime/<str:slug>', views.AnimeView.as_view(), name='anime_page'),
    path('genres/<str:slug>', views.GengerView.as_view(), name='genres_page'),
    path('studio/<str:slug>', views.StudioView.as_view(), name='studio_page'),
    path('account/<int:id>', views.AccountView.as_view(), name='account_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('logout', views.log_out, name='logout'),
    path('register', views.RegView.as_view(), name='reg_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
