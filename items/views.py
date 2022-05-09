from django.shortcuts import render, redirect, get_object_or_404
from items.forms.item_form import ItemCreateForm, ItemUpdateForm, BidCreateForm
from items.models import ItemImage, Item, ItemCategory, ItemBid
from Users.models import Profile
from django.contrib.auth.decorators import login_required

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
    similar_items = Item.objects.all().filter(category__name__exact=category).exclude(pk=id)
    return render(request, 'Item/item_details.html', {
        'item': item_obj,
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
    user_obj = Profile.objects.get(user_id=user.id)   # sama og uppi :)
    item_obj = Item.objects.get(id=id)
    if request.method == 'POST':
        form = BidCreateForm(data=request.POST)
        if form.is_valid():
            item_bid = form.save(commit=False)
            item_bid.bidder = user_obj
            item_bid.item = item_obj
            item_bid.save()
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
    context = {'item_offers': ItemBid.objects.filter(bidder_id=user.id)}
    return render(request, 'Item/my_bids.html', context)

