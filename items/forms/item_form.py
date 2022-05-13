from django.forms import ModelForm, widgets
from items.models import Item, ItemBid, ItemImage
from django import forms


class ItemUpdateForm(ModelForm):
    #image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id','owner', 'accepted']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'image1': widgets.TextInput(attrs={'class': 'form-control'}),
            'image2': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id', 'owner', 'accepted']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs= {'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class BidCreateForm(ModelForm):
    class Meta:
        model = ItemBid
        exclude = ['id', 'item', 'bidder', 'seen', 'accepted', 'owner']
        widgets = {
            'item_price': widgets.NumberInput(attrs={'class': 'form-control'})
        }
