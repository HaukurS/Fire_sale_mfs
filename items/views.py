from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from items.forms.item_form import ItemCreateForm, ItemUpdateForm, BidCreateForm
from items.models import ItemImage, Item, ItemCategory, ItemBid
from Users.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from core.services.notification_creater import create_notification, send_all_notification
from notifications.models import Type

# Create your views here.

#function that renders all items to page
def index(request):
    context = {'items': Item.objects.all().order_by('name'),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)

#orders the items from high-low
def orderpricehigh(request):
    context = {'items': Item.objects.all().order_by('-price'),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)

#orders the items from low-high
def orderpricelow(request):
    context = {'items': Item.objects.all().order_by('price'),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)

#gets an item by a specific id
def get_item_by_id(request, id):
    user = request.user
    item_obj = get_object_or_404(Item, pk=id)
    profile_obj = get_object_or_404(Profile, user_id=user.id)
    category = item_obj.category
    highest_bid1 = ItemBid.objects.all().filter(item_id=id).aggregate(Max('item_price'))
    max_bid = highest_bid1.get('item_price__max')
    if max_bid == None:
        max_bid = "No bid has been made"
    similar_items = Item.objects.all().filter(category__name__exact=category).exclude(pk=id)
    return render(request, 'Item/item_details.html', {
        'item': item_obj,
        'Highest_bid': max_bid,
        'user_profile': profile_obj,
        'similar_items': similar_items
    })

#gets items by a specific category
def get_items_by_category(request, category):
    context = {'items': Item.objects.all().filter(category__name__exact=category),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)
    #context = {'items': Item.objects.filter(category__item__name=category)}
    #return render(request, 'Item/Index.html', context)

#function to create an item
@login_required
def create_item(request):
    user = request.user
    user_obj = Profile.objects.get(user_id=user.id)
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = user_obj  # skoða með tengja á auth user
            item.save()
            for img in ['image', 'image1', 'image2']:
                image = request.POST[img]
                if image:
                    item_image = ItemImage(image=request.POST['image'], item=item)
                    item_image.save()
            # item.owner = user_obj  #skoða með tengja á auth user
            # item.save()
            return redirect('index')
    else:
        form = ItemCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Item/create_item.html', {
        'form': form
    })

#function that deletes an item with a specific id
@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('homepage')

#function that updates an item
@login_required
def update_item(request, id):
    user = request.user
    profile = get_object_or_404(Profile, user_id=user.id)
    instance = get_object_or_404(Item, pk=id)
    if profile.id != instance.owner_id:
        return redirect('homepage')
    if request.method == 'POST':
        form = ItemUpdateForm(data = request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('item_details', id=id)
    else:
        form = ItemUpdateForm(instance=instance)
    return render(request, 'Item/update_item.html', {
        'form': form,
        'id': id
    })

#function to place a bid
@login_required
def place_bid(request, id):
    user = request.user
    bidder_obj = Profile.objects.get(user_id=user.id)
    item_obj = Item.objects.get(id=id)
    OwnerProfile = Profile.objects.get(id=item_obj.owner_id)
    OwnerUser = User.objects.get(id = OwnerProfile.user_id)
    #owner_obj = get_object_or_404(Profile, pk=item_obj.owner_id)
    if request.method == 'POST':
        form = BidCreateForm(data=request.POST)
        if form.is_valid():
            item_bid = form.save(commit=False)
            item_bid.bidder = bidder_obj
            item_bid.item = item_obj
            item_bid.owner = OwnerUser
            item_bid.save()
            name = 'New Bid'
            create_notification(name, item_obj.owner.user)
            return redirect('item_details', id=id)
    else:
        form = BidCreateForm()
    return render(request, 'Item/place_bid.html', {
        'form': form,
        'id': id
    })

#function to delete a bid by specific id
def delete_bid(request, id):
    item_bid = get_object_or_404(ItemBid, id=id)
    instance2 = Item.objects.get(id=item_bid.item_id)
    form2 = ItemCreateForm(instance=instance2)
    item_item = form2.save(commit=False)
    item_item.accepted = False
    item_item.save()
    item_bid.delete()
    return redirect('my_bids')

#function to delete an offer by specific id
def delete_offer(request, id):
    item_bid = get_object_or_404(ItemBid, id=id)
    user_obj = item_bid.bidder.user
    item_bid.delete()
    create_notification('Rejected', user_obj)
    return redirect('my_offers')


#function that gets all the items of a specific user
@login_required
def get_user_items(request):
    user = request.user
    profile = get_object_or_404(Profile, user_id=user.id)
    context = {'items': Item.objects.filter(owner_id=profile.id)}
    return render(request, 'Item/my_items.html', context)

#function that gets all bids from a specific user
@login_required
def get_user_bids(request):
    user = request.user
    profile = get_object_or_404(Profile, user_id=user.id)
    context = {'item_offers': ItemBid.objects.filter(bidder_id=profile.id),
               'items': Item.objects.all().order_by('name')}
    return render(request, 'Item/my_bids.html', context)


#function that gets all offers from a specific user
@login_required
def get_user_offers(request):
    user = request.user
    context = {'item_your_offers': ItemBid.objects.filter(owner_id=user.id)}
    return render(request, 'Item/my_offers.html', context)

#function to accept an offer
@login_required
def accept_offer(request, id):
    instance = ItemBid.objects.get(id=id)
    instance2 = Item.objects.get(id=instance.item_id)
    bidder = get_object_or_404(Profile, id=instance.bidder_id)
    item_obj = instance.item      #skoða ARNAR HVAÐ ERTU AÐ GERA???
    all_offers = ItemBid.objects.all()
    for offer in all_offers:
        if offer.id != instance.id and offer.item_id == instance.item_id:
            item_bid = get_object_or_404(ItemBid, id=offer.id)
            bid_user = item_bid.bidder.user
            create_notification('Rejected', bid_user)
            item_bid.delete()
    if request.method == 'GET':
        form = BidCreateForm(instance=instance)
        item_offer = form.save(commit=False)
        item_offer.accepted = True
        item_offer.save()

        form2 = ItemCreateForm(instance=instance2)
        item_item = form2.save(commit=False)
        item_item.accepted = True
        item_item.save()
        create_notification('Accepted', instance.bidder.user)
        return redirect('my_offers')
    return redirect('my_offers')
