# Generated by Django 3.0.1 on 2020-02-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_auto_20200212_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='styleone',
            name='category',
            field=models.CharField(default='Personal', max_length=15),
        ),
    ]
