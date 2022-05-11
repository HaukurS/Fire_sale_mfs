from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from notifications.models import Notification


def show_notifications(request):
    id = request.user.id
    context = {'notifications': Notification.objects.filter(user_id=id)}
    return render(request, 'Notification/your_notification.html', context)


def delete_notification(request, id):
    notification = get_object_or_404(Notification, id=id)
    notification.delete()
    return redirect('notifications')
