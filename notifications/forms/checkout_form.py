from django.forms import ModelForm, widgets
from Users.models import Profile
from django import forms


class CheckoutInfoForm(ModelForm):
    class Meta:
        model = Profile
        exclude =[]