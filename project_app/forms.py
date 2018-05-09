from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import models

from project_app.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class UploadFilesForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('file_one', 'file_two')