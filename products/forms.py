from django import forms
from .models import Products,Category,Review
from django.contrib.auth.forms import UserCreationForm,UserChangeForm




class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject','comment']