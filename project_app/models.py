from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional

    demand_file = models.FileField(upload_to='archivos', blank=True)
    order_file = models.FileField(upload_to='archivos', blank=True)

    def __str__(self):
        return self.user.username
