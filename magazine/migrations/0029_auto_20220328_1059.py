# Generated by Django 3.1.4 on 2022-03-28 07:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazine', '0028_auto_20220322_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='share',
            field=models.CharField(default='', max_length=50),
        ),
    ]