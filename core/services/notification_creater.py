from notifications.forms.notification_form import NotificationCreateForm
from django.contrib.auth.decorators import login_required


def create_notification(name, bid_obj, user_obj):
    form = NotificationCreateForm()
    notification = form.save(commit=False)
    notification.name = name
    notification.item_bid = bid_obj
    notification.user = user_obj
    notification.save()


def send_all_notification(name, bid_obj, user_list):
    for user_set in user_list:
        form = NotificationCreateForm()
        notification = form.save(commit=False)
        notification.name = name
        notification.item_bid = bid_obj
        notification.user = user_set[0]
        notification.save()



