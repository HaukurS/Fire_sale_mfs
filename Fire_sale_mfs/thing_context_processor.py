from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from Users.models import Profile
from items.models import ItemBid, Item
from notifications.models import Notification


def notifications(request):
    id = request.user.id
    context = {
        'num_of_notify': len(Notification.objects.filter(user_id=id))
    }
    return context








