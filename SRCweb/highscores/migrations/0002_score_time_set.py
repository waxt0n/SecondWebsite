# Generated by Django 3.1.5 on 2021-01-05 23:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('highscores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='time_set',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
