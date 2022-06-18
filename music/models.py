from django.db import models
import random
from django.contrib.auth.models import User
import string

class Genre_songs(models.Model):
    name_genre = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name_genre


class Music(models.Model):
    name_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name_song = models.CharField(max_length=100)
    avtor = models.CharField(max_length=100)
    avtor_artist = models.ManyToManyField('artist.Artist', related_name='avtor_artist', blank=True)
    feat = models.CharField(max_length=150, blank=True, null=True)
    song_path = models.FileField(upload_to='song/')
    photo_song = models.ImageField(upload_to='song/photo')
    genre = models.ForeignKey(Genre_songs, on_delete=models.SET_NULL, blank=True, null=True)
    album = models.CharField(max_length=100, null=True, blank=True,)
    share = models.CharField(max_length=50, default='')
    time = models.CharField(max_length=10)
    def __str__(self):
        return self.name_song
    class Meat:
        verbose_name = 'Музыка'


class Playlists(models.Model):
    name_playlist = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='playlist/photo')
    avtor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    music = models.ManyToManyField(Music, related_name='music_in_playlist', blank=True)
    about_playlist = models.TextField()
    date_playlist = models.DateField(blank=True, null=True)
    share = models.CharField(max_length=15, blank=True, null=True)
    views = models.ManyToManyField(User, related_name='playlist_views', blank=True)

    def __str__(self):
        return self.name_playlist

    class Meat:
        verbose_name = 'Плейлисты'