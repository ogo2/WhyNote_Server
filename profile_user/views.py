from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormView
from .forms import RegisterUserForm
from . forms import RegisterUserForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from music.models import Music
# def index(request):
#     name = Users.name
#     country = Users.objects.get(id=1)
#     about_me = Users.about_me
#     return render(request, 'profile_user/index.html', {'name': name, 'country': country, 'about_me': about_me})
from django.http import HttpResponseRedirect
from django.contrib import messages

def profile2(request, username):
    user = User.objects.all()
    user_info = User.objects.get(username=username)
    print(request.GET.get('this'))
    f = user_info.profile
    f2 = user_info.profile
    print(f2.subscribers.all())
    subscriptions = f2.subscriptions.all()
    subscribers = f2.subscribers.all()
    count_subscriptions = len(subscriptions)
    count_subscribers = len(subscribers)
    k = request.user
    if k.username == username:
        print(True)
    else:
        print(False)
    music_profile = f.music_list.all()
    if request.method == "POST":
        print(222222)
        user_section = User.objects.get(username=request.user)
        pr = User.objects.get(username=request.POST.get('this_sub'))
        user_section.profile.subscriptions.add(pr)
        f2.subscribers.add(user_section)
    if request.method == "GET":
        try:
            music_id = Music.objects.get(share=f'{request.GET.get("this")}')
            print(music_id)
            f2.music_list.remove(music_id)
        except Exception:
            pass
    return render(request, 'profile_user/profile.html', {'k': k, 'users': user, 'name_user': username,
                                                         'info_user': user_info.profile,
                                                         'profile': profile, 'music_profile': music_profile, 'subscriptions':subscriptions,
                                                         'subscribers': subscribers, 'count_subscriptions': count_subscriptions,
                                                         'count_subscribers': count_subscribers})



class profile(DetailView):
    model = User
    context_object_name = 'Profile'
    template_name = 'profile_user/profile.html'


def login_user(request):
    return render(request, 'profile_user/login.html')

class LazyUser(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_user'):
            from django.contrib.auth import get_user
            request._cached_user = get_user(request)
        return request._cached_user

class AuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request,
                       'session'), "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        request.__class__.user = LazyUser()


def get_user1(request):
    session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
    user_dict = get_user_from_icnet(session_key)
    print(session_key)
    if user_dict:
        user, iscreate = User.objects.get_or_create(username=user_dict['username'])
        print('good_suka', user_dict)
    else:
        user = AnonymousUser()
    return user
def suck_my_dick(user):
    request._cached_user = user
    global kak
    kak = request._cached_user
    return kak
def get_user_from_icnet(session_key):
    user_dict = {'username': 'test'}
    return user_dict

def RegisterUser(request):
    model = User
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            user2 = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password1'))
            if user2:
                print(True)
                from django.contrib.auth import get_user
                print(get_user1(request))
            else:
                print(False)
            user = User.objects.get(username=request.POST.get('username'))
            from django.contrib.auth import get_user
            login(request, user)
            request._cached_user = get_user(request)
            f = get_user(request)
            suck_my_dick(f)
            return redirect('register_next')
        else:
            messages.error(request, 'Ошибка регистрации')
            # return redirect('registr')
            # print(request)
            # return self.form_invalid(form)
    else:
        form = RegisterUserForm()
    return render(request, 'profile_user/registr.html', {'form': form})

def RegisterUserNext(request):
    from django.contrib.auth import get_user

    request._cached_user = get_user(request)
    gg = User.objects.get(username=kak)
    profile_user = Profile.objects.get(user=gg)
    print(profile_user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print('22')
            country = Country_list.objects.get(pk=int(request.POST.get('country')))

            # profile_user.country = int(request.POST.get('country'))
            profile_user.photo = request.FILES.get('photo')
            print(request.FILES.get('photo'))
            print(country)
            profile_user.country = country
            profile_user.about_me = request.POST.get('about_me')
            profile_user.save()
            print(profile_user.about_me)
            return redirect("index")
        else:
            print(23)
            form = ProfileForm()
    else:
        print(11)
        form = ProfileForm()
    return render(request, 'profile_user/register_next.html', {'form': form})

class LoginUser(LoginView):
    form_class = LodinUserForm
    template_name = 'profile_user/login.html'

    def get_success_url(self, **kwargs):

        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('index')
