from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # Specify what model you want to change or will be affected
        #
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Fields shown in order
