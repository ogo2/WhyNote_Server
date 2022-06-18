from django.db import models
from django.contrib.auth.models import User
from profile_user.models import Profile
from django.utils.text import slugify
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
# from likes.models import Like
import random
import string


class Genre_article(models.Model):
    name_genre = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name_genre


class article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField(upload_to='article/%Y/%m/%d')
    genre = models.ForeignKey(Genre_article, on_delete=models.SET_NULL, blank=True, null=True)
    name_user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.CharField(max_length=50, default='')
    like = models.ManyToManyField(User, related_name='post_like', blank=True)
    disslike = models.JSONField(blank=True, null=True)
    views = models.ManyToManyField(User, related_name='post_views', blank=True)

    def __str__(self):
        return self.title
    class Meat:
        verbose_name = 'Статьи'

class Comment(models.Model):
    post_name = models.ForeignKey(article, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return '{}'.format(self.post_name)
    class Meat:
        verbose_name = 'Комментарии'

