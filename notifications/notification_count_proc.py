from notifications.models import Notification


def notifications(request):
    id = request.user.id
    context = {
        'num_of_notify': Notification.objects.filter(user_id=id).count()
    }
    return context