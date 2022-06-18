# Generated by Django 3.1.4 on 2022-03-30 18:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_user', '0008_auto_20220324_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]