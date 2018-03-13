from django import forms
from django.contrib.auth.models import User
from project_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserFileUploadForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('demand_file', 'order_file')
