# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    url('<str:room_name>/', views.room, name='room'),
]
