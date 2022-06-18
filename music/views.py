from django.shortcuts import render
from profile_user.models import Profile
from artist.models import Artist
from music.models import Music
from .forms import *


def add_song(request):
    if request.method == 'POST':
        add_form_song = Add_music(request.POST, request.FILES)
        if add_form_song.is_valid():
            print(request.POST.get("avtor"))
            artist_name = Artist.objects.get(name_artist=request.POST.get("avtor"))

            add = add_form_song.save(commit=False)

            share_life = ''.join(random.choice(string.ascii_letters) for _ in range(50))
            add.share = share_life
            add.name_user = request.user

            add.save()
            music_bd = Music.objects.get(share=share_life)
            if Artist.objects.get(name_artist=request.POST.get("avtor")):
                artist_name.music_artist.add(music_bd)
                music_bd.avtor_artist.add(artist_name)
                print(True)
            else:
                print(123232)
    else:
        add_form_song = Add_music()
    return render(request, 'music/add_song.html', {'form': add_form_song})