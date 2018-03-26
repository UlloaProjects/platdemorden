from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from project_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserFileUploadForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data.get("file", False)
        filetype = magic.from_buffer(file.read())
        if not "CSV" in filetype:
            raise ValidationError("File is not CSV.")
        return file

    class Meta():
        model = UserProfileInfo
        fields = ('demand_file', 'order_file')
