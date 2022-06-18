from django.urls import path
from .views import *



urlpatterns = [
    path('profile/<str:username>/', profile2, name='profile'),
    path('registr/', RegisterUser, name='registr'),
    path('register_next/', RegisterUserNext, name='register_next'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]