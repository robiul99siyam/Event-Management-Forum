from django.db import models
from EventCategory.models import Event_category
from .constant import EVENT_TYPE_CHOICES
from django.contrib.auth.models import User

# ------------ event creation model ------------------------->
class Event_creation_model(models.Model):
    event_category = models.ForeignKey(
        Event_category, blank=True, null=True, on_delete=models.CASCADE, default=None
    )
    user = models.ForeignKey(User, blank=True,on_delete=models.CASCADE,null=True)
    count = models.IntegerField(default=0)
    event_name = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
    description = models.TextField()
    event_type = models.CharField(
        max_length=50, choices=EVENT_TYPE_CHOICES, default="Pablic"
    )


    def __str__(self):
        return self.event_name



class Confirm_Event (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    save_events = models.ManyToManyField(Event_creation_model,related_name='save_events')
    creation_time = models.DateTimeField(auto_now_add=True)