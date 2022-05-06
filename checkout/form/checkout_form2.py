from checkout.models import PaymentInfo
from django.forms import ModelForm, widgets


class PaymentInfoCreateForm(ModelForm):
    class Meta:
        model = PaymentInfo
        exclude = ['id']
        widgets = {
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control'})
        }
