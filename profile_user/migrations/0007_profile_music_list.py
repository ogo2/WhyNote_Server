# Generated by Django 3.1.4 on 2022-03-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0006_auto_20220308_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='music_list',
            field=models.TextField(blank=True),
        ),
    ]
