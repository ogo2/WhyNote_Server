from django.contrib import admin

from .models import Artist, Sex, Genre

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Sex)
