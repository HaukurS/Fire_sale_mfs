from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from Users.models import Profile
from items.models import ItemBid, Item
from notifications.models import Notification


@login_required
def notifications(request):
    id = request.user.id
    context = {
        'num_of_notify': len(Notification.objects.filter(user_id=id))
    }
    return context


@login_required
def bids(request):
    id = request.user.id
    profile_obj = get_object_or_404(Profile, user_id=id)
    context = {
        'num_of_bids': ItemBid.objects.filter(bidder_id=profile_obj.id).count()
    }
    return context





