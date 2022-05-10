from django.forms import ModelForm, widgets

from Users.models import Profile


class ContactCreateForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'bio', 'password', 'email', 'phone_number', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'})
        }
