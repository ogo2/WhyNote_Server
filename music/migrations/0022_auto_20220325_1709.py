# Generated by Django 3.1.4 on 2022-03-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0021_auto_20220324_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='share',
            field=models.CharField(default='', max_length=50),
        ),
    ]
