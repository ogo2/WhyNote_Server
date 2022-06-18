from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from music.models import Music

class Country_list(models.Model):
    country = models.CharField(max_length=100,  null=True, blank=True)
    def __str__(self):
        return self.country

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    about_me = models.TextField(blank=True)
    mail = models.EmailField(max_length=150)
    music_list = models.ManyToManyField(Music, related_name='music', blank=True)
    country = models.ForeignKey(Country_list, on_delete=models.CASCADE, blank=True, null=True)
    subscriptions = models.ManyToManyField(User, related_name='subscriptions', blank=True, null=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank=True, null=True)
    def get_absolute_url(self):
        return reversed('profile', kwargs={'username': self.user.username})

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
