from django.db import models

from django.contrib.auth.models import User


#---------------------- model contact --------------->
class contactUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField()

    