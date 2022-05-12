from django.forms import ModelForm, widgets

from notifications.models import Notification


class NotificationCreateForm(ModelForm):
    class Meta:
        model = Notification
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'})
        }