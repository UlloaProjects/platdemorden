from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from project_app.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    file_one = models.FileField(upload_to='csvfiles')
    file_two = models.FileField(upload_to='csvfiles')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse("my_app:details", kwargs={'pk': self.pk})


class Product(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    material = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
    oficina = models.CharField(max_length=255, blank=False, null=False)
    demanda_ses = models.DecimalField(max_digits=20, decimal_places=4, null=True, blank=True)
    texto_breve_material = models.CharField(max_length=255)
    demanda_anual = models.IntegerField(default=0)


class ProductDemand(models.Model):
    product = models.ForeignKey(Product, related_name='demands', on_delete=models.CASCADE)
    date = models.DateField()
    mes = models.IntegerField()
    anno = models.IntegerField()
    demand = models.IntegerField()

    def getKey(self):
        return self.date


class PronosticoSES(models.Model):
    owner = models.ForeignKey(Product, related_name='SES', on_delete=models.CASCADE)
    monthly_demand = ArrayField(models.IntegerField())

