# Generated by Django 3.1.4 on 2022-03-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0021_auto_20220308_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='share',
            field=models.CharField(default='fXynzRljlpTjxNySRZdPCzcYvZQFMVtPMgoWxRxHjiBBuerzvB', max_length=50),
        ),
    ]
