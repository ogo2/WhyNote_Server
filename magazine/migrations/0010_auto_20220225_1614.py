# Generated by Django 3.2.8 on 2022-02-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0009_alter_article_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='share',
            field=models.CharField(default='lgnmMxteWVQkaduQZiIWIfFmNTUzUBPTKHqhQxaBJhSLHWWUig', max_length=50),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
