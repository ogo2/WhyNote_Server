# Generated by Django 3.2.8 on 2022-03-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0011_alter_article_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='share',
            field=models.CharField(default='vBdmvCDqfIADWUHuILPHvDippGmulZuNwkahxFZrmwVTiJyxNg', max_length=50),
        ),
    ]
