from django.shortcuts import get_object_or_404

from Users.models import Profile
from items.models import ItemBid, Item
from notifications.models import Notification


def notifications(request):
    id = request.user.id
    context = {
        'num_of_notify': Notification.objects.filter(user_id=id).count()
    }
    return context


def bids(request):
    id = request.user.id
    profile_obj = get_object_or_404(Profile, user_id=id)
    context = {
        'num_of_bids': ItemBid.objects.filter(bidder_id=profile_obj.id).count()
    }
    return context


def items(request):
    id = request.user.id
    profile_obj = get_object_or_404(Profile, user_id=id)
    context = {
        'num_of_items': Item.objects.filter(owner_id=profile_obj.id).count()
    }
    return context