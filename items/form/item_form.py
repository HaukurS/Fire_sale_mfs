from django.forms import ModelForm, widgets
from items.models import Item


class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),

        }
