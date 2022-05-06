from django.forms import ModelForm, widgets

from Users.models import User



class ContactCreateForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'description', 'bio', 'password', 'email', 'phone_number']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.Select(attrs={'class': 'form-control'})
        }
