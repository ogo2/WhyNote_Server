from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('playlists', playlists, name='playlists'),
    path('playlist/<str:share>', playlist, name='playlist')
]