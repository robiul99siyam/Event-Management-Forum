from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Apply_Organizer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, default=1)
    apply_organizer = models.BooleanField(default=False)
    