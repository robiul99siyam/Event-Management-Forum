# Generated by Django 4.2.6 on 2024-01-17 04:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Event_creation', '0007_alter_event_creation_model_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_creation_model',
            name='user',
        ),
        migrations.AddField(
            model_name='event_creation_model',
            name='confirmed_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
