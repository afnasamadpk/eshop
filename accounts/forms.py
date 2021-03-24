from django import forms
from accounts.models import UserAccounts
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ['email']