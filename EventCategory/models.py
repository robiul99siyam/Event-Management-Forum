from django.db import models

# Create your models here.
class Event_category(models.Model):
    event_category_tags = models.CharField(max_length=50)
    def __str__(self):
        return self.event_category_tags