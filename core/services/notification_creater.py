from notifications.forms.notification_form import NotificationCreateForm


def create_notification(type_obj, bid_obj, user_obj):
    form = NotificationCreateForm()
    notification = form.save(commit=False)
    notification.type = type_obj
    notification.item_bid = bid_obj
    notification.user = user_obj
    notification.save()

