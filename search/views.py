from django.shortcuts import render
from profile_user.models import Profile
from django.contrib.auth.models import User
from music.models import Music, Playlists
from django.db.models import Q # новый
from magazine.models import article
from profile_user.models import Profile
def search(request):
    magaz = article.objects.filter(title__icontains=request.GET.get('search'))
    f = User.objects.filter(username__icontains=request.GET.get('search'))
    m = Music.objects.filter(Q(name_song__icontains=request.GET.get('search')) | Q(avtor=request.GET.get('search')))

    print(f)
    print(m)
    # try:
    #     return render(request, 'search/search_page.html', {'users': User, 'music': m, 'f': f})
    # except:
    # users = None
    # print(m)
    return render(request, 'search/search_page.html', {'music': m, 'article': magaz, 'f': f, 'profile': Profile})
