# Generated by Django 3.2.11 on 2022-02-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='header',
            field=models.CharField(default='', max_length=100),
        ),
    ]
