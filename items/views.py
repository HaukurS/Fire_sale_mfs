from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from items.forms.item_form import ItemCreateForm, ItemUpdateForm, BidCreateForm
from items.models import ItemImage, Item, ItemCategory, ItemBid
from Users.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from core.services.notification_creater import create_notification
from notifications.models import Type

# Create your views here.


def index(request):
    context = {'items': Item.objects.all().order_by('name'),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)


def orderpricehigh(request):
    context = {'items': Item.objects.all().order_by('-price'),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)


def orderpricelow(request):
    context = {'items': Item.objects.all().order_by('price'),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)


def get_item_by_id(request, id):
    item_obj = get_object_or_404(Item, pk=id)
    category = item_obj.category
    highest_bid1 = ItemBid.objects.all().filter(item_id=id).aggregate(Max('item_price'))
    max_bid = highest_bid1.get('item_price__max')
    if max_bid == None:
        max_bid = "No bid has been made"
    similar_items = Item.objects.all().filter(category__name__exact=category).exclude(pk=id)
    return render(request, 'Item/item_details.html', {
        'item': item_obj,
        'Highest_bid': max_bid,
        'similar_items': similar_items
    })


def get_items_by_category(request, category):
    context = {'items': Item.objects.all().filter(category__name__exact=category),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)
    #context = {'items': Item.objects.filter(category__item__name=category)}
    #return render(request, 'Item/Index.html', context)

@login_required
def create_item(request):
    user = request.user
    user_obj = Profile.objects.get(user_id=user.id)   #user_id þegar nyja profile er implementað
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = user_obj  #skoða með tengja á auth user
            item.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('index')
    else:
        form = ItemCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Item/create_item.html', {
        'form': form
    })

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('index')

@login_required
def update_item(request, id):
    instance = get_object_or_404(Item, pk=id)
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

@login_required
def place_bid(request, id):
    user = request.user
    profile_obj = Profile.objects.get(user_id=user.id)   # sama og uppi :)
    item_obj = Item.objects.get(id=id)
    owner_obj = get_object_or_404(User, pk=item_obj.owner_id)
    if request.method == 'POST':
        form = BidCreateForm(data=request.POST)
        if form.is_valid():
            item_bid = form.save(commit=False)
            item_bid.bidder = profile_obj
            item_bid.item = item_obj
            item_bid.owner = owner_obj
            item_bid.save()
            some = create_notification(get_object_or_404(Type, name='New Bid'), ItemBid.objects.last(), item_obj.owner.user)
            return redirect('item_details', id=id)
    else:
        form = BidCreateForm()
    return render(request, 'Item/place_bid.html', {
        'form': form,
        'id': id
    })

@login_required
def get_user_items(request):
    user = request.user
    context = {'items': Item.objects.filter(owner_id=user.id)}
    return render(request, 'Item/my_items.html', context)

@login_required
def get_user_bids(request):
    user = request.user
    context = {'item_offers': ItemBid.objects.filter(bidder_id=user.id),
               'items': Item.objects.all().order_by('name')}
    return render(request, 'Item/my_bids.html', context)


@login_required
def get_user_offers(request):
    user = request.user
    context = {'item_your_offers': ItemBid.objects.filter(owner_id=user.id)}
    return render(request, 'Item/my_offers.html', context)


