# Generated by Django 4.2.6 on 2024-02-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event_creation', '0015_alter_event_creation_model_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirm_event',
            name='event_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], max_length=20, null=True),
        ),
    ]