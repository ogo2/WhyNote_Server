from django.urls import path
from .views import *



urlpatterns = [
    path('add_song/', add_song, name='add_song'),

]