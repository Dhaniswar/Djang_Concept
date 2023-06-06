from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=16)
    first_name = forms.CharField(max_length = 254)
    last_name = forms.CharField(max_length=254)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'first_name', 'last_name']
        