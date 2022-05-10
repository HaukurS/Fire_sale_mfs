from django.shortcuts import render, get_object_or_404

# Create your views here.
from notifications.models import Notification


def show_notifications(request):
    id = request.user.id
    context = {'notifications': Notification.objects.filter(user_id=id)}
    return render(request, 'Notification/your_notification.html', context)


