from django.forms import ModelForm, widgets
from items.models import Item
from items.models import ItemOffer
from django import forms


class ItemUpdateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'})
        }


class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs= {'class': 'form-control'}),
            'description': widgets.TextInput(attrs= {'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'})
        }

class PlaceBidForm(ModelForm):
    class Meta:
        model = ItemOffer
        exclude = ['id']
        widgets = {
            'price': widgets.NumberInput(attrs= {'class': 'form-control'})
        }
