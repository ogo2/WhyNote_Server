from django.contrib import admin
from .models import Profile, Country_list


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'about_me', 'mail', 'photo']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country_list)