from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *


# Registration form
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "bio"]

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscriptionRecipients
        fields = ["name", "email", "your_address", "phone", "age"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["author", "description", "cover", "subject", "title"]
