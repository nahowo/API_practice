from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'movie'
urlpatterns = [
    path('', views.menu, name = 'menu'),
    path('api_book_search/', views.api_book_search, name='api_book_search'),
    path('api_movie_search/', views.api_movie_search, name = 'api_movie_search'),
]