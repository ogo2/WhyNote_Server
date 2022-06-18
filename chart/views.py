from django.shortcuts import render
from django.http import HttpResponse
from music.models import Music, Playlists
from profile_user.models import User, Profile
# from mutagen.mp3 import MP3

def index(request):
    current_user = request.user
    try:
        f = request.user.profile
        if request.method == "GET":
            # print(request.GET.get('add_music_user'))
            f.music_list.add(request.GET.get('this'))
    except Exception:
        pass
    # print(current_user.id)
    print(request.GET.get('this'))
    music = Music.objects.all()
    playlists = Playlists.objects.all()
    print(music[0].song_path)

    return render(request, 'chart/index.html', {
        'music': music,
        'playlists': playlists
    })
def playlists(request):
    playlist = Playlists.objects.all()

    return render(request, 'chart/playlists.html', {"playlists": playlist})

def playlist(request, share):
    playlist = Playlists.objects.get(share=share)
    music_all = Music.objects.all()
    music = playlist.music.all()
    print(music[0].avtor)
    # for k in music:
    #     print(k)
    return render(request, 'chart/playlist.html', {"playlist": playlist})