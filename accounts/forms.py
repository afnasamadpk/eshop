from django import forms
from accounts.models import UserAccounts,Address
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ['shortname','email']




class EditForm(UserChangeForm):
    class Meta:
        model = UserAccounts
        fields = ['shortname','email']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        del self.fields['password']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address','country','state','city','phone','pincode']