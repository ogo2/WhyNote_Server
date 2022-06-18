# Generated by Django 3.1.4 on 2022-03-28 11:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazine', '0029_auto_20220328_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like',
        ),
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
