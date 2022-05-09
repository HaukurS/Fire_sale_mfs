from django.forms import ModelForm, widgets
#from Users.models import User
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class UserRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
#<<<<<<< Updated upstream
#        exclude = ['id','bio', 'street_name', 'phone_number', 'country', 'city', 'zip']
#        widgets = {
#            'name': widgets.TextInput(attrs= {'class': 'form-control'}),
#            'password': widgets.PasswordInput(attrs={'class': 'form-control'}),
#            'email': widgets.TextInput(attrs={'class': 'form-control'})
#        }
#=======
        fields = ['username', 'email', 'password1', 'password2']

#class UserProfile(ModelForm):
#    class Meta:
#        model = User
#        exclude = ['user','id','bio', 'street_name', 'phone_number', 'country', 'city', 'zip']
#        widgets = {
#            'name': widgets.Select(),
 #           'email': widgets.Select()
#
#        }
#ç>>>>>>> Stashed changes
#class UserLogInForm(ModelForm):


