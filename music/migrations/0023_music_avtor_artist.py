# Generated by Django 3.1.4 on 2022-03-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0004_auto_20220325_1724'),
        ('music', '0022_auto_20220325_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='avtor_artist',
            field=models.ManyToManyField(blank=True, related_name='avtor_artist', to='artist.Artist'),
        ),
    ]
