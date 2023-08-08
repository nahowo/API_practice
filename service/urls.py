from django.conf.urls import url
from . import views
from django.urls import path

app_name = "service"
urlpatterns = [
    path('',views.api_service_search, name="api_service_search"),
]