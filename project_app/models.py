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


class demanda(models.Model):

    demanda_diaria = models.DecimalField(decimal_places=10)
    demanda_promedio = models.DecimalField(decimal_places=10)


class ses(models.Model):

    alpha = models.DecimalField(decimal_places=1)



