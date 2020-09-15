from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # add this field to the usercreationform

    class Meta:  # Nested namespace for configurations
        model = User  # what this interacts
        # this will affect user models
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):  # creates a form model

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']  # allow us to update username and email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']  # allows us to update the image
