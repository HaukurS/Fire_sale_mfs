from django.forms import ModelForm, widgets
from Users.models import User
from django import forms


class UserRegisterForm(ModelForm):
    re_enter_password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        exclude = ['id','bio', 'street_name', 'phone_number']
        widgets = {
            'name': widgets.TextInput(attrs= {'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),

        }
#class UserLogInForm(ModelForm):


