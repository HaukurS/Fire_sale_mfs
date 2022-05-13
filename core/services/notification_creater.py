from notifications.forms.notification_form import NotificationCreateForm
from django.contrib.auth.decorators import login_required


# a function that creates a notification automatically
def create_notification(name, user_obj):
    form = NotificationCreateForm()
    notification = form.save(commit=False)
    notification.name = name
    notification.user = user_obj
    notification.save()




