# Generated by Django 3.1.6 on 2021-03-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0002_article_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
