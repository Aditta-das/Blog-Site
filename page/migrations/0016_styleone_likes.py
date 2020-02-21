# Generated by Django 3.0.1 on 2020-02-12 16:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0015_auto_20200212_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='styleone',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
