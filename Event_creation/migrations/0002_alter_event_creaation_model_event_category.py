# Generated by Django 4.2.6 on 2024-01-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCategory', '0001_initial'),
        ('Event_creation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_creaation_model',
            name='event_category',
            field=models.ManyToManyField(blank=True, to='EventCategory.event_category'),
        ),
    ]
