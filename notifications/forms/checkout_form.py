from django.forms import ModelForm, widgets
from Users.models import User
from django import forms


class CheckoutInfoForm(ModelForm):
    class Meta:
        model = User
        exclude =[]