from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'movie'
urlpatterns = [
    path('', views.api_book_search, name='api_book_search'),
]