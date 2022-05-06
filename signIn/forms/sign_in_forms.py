from django.forms import ModelForm, widgets
from Users.models import User
from django import forms
#from django.contrib.auth.forms import UserCreationForm



class UserRegistration(ModelForm):
    re_enter_password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        exclude = ['id','bio', 'street_name', 'phone_number', 'country', 'city', 'zip']
        widgets = {
            'name': widgets.TextInput(attrs= {'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }
#class UserLogInForm(ModelForm):


