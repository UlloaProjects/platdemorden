from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional

    demand_file = models.FileField(upload_to='archivos', blank=True, validators=[validate_file_extension])
    order_file = models.FileField(upload_to='archivos', blank=True, validators=[validate_file_extension])

    #ses = models.DecimalField(decimal_places=5,max_digits=20)
    #dma = models.DecimalField(decimal_places=5,max_digits=20)


    def __str__(self):
        return self.user.username


class demanda(models.Model):

    demanda_diaria = models.DecimalField(decimal_places=10, max_digits=20)
    demanda_promedio = models.DecimalField(decimal_places=10, max_digits=20)


class ses(models.Model):

    alpha = models.DecimalField(decimal_places=1, max_digits=20)



