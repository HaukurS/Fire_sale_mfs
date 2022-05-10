from checkout.models import PaymentInfo
from django.forms import ModelForm, widgets


class PaymentInfoCreateForm(ModelForm):
    cvc = widgets.NumberInput(attrs={'class': 'form-control'})
    class Meta:
        model = PaymentInfo
        exclude = ['id', 'profile']
        widgets = {
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control'})
        }
