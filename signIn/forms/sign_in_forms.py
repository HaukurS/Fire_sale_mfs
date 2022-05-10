from django.forms import ModelForm, widgets
from Users.models import Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class UserRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
#        exclude = ['id','last_login', 'is_supervisor', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
        #widgets = {
            #'username': widgets.TextInput(attrs= {'class': 'form-control'}),
            #'password1': widgets.PasswordInput(attrs={'class': 'form-control'}),
            #'password2': widgets.PasswordInput(attrs={'class': 'form-control'}),
            #'email': widgets.TextInput(attrs={'class': 'form-control'})
 #       }
#=======


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


