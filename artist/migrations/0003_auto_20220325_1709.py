# Generated by Django 3.1.4 on 2022-03-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0022_auto_20220325_1709'),
        ('artist', '0002_auto_20220308_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='music',
        ),
        migrations.AddField(
            model_name='artist',
            name='music',
            field=models.ManyToManyField(blank=True, related_name='music_artist', to='music.Music'),
        ),
    ]
