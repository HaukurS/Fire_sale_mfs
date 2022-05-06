from django.shortcuts import render, redirect, get_object_or_404
from items.forms.item_form import ItemCreateForm, ItemUpdateForm, BidCreateForm
from items.models import ItemImage, Item, ItemCategory
from Users.models import User

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
    return render(request, 'Item/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })


def get_items_by_category(request, category):
    context = {'items': Item.objects.all().filter(category__name__exact=category),
               'categorys': ItemCategory.objects.all()}
    return render(request, 'Item/Index.html', context)
    #context = {'items': Item.objects.filter(category__item__name=category)}
    #return render(request, 'Item/Index.html', context)


def create_item(request):
    user = request.user
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            form.cleaned_data['owner'] = user
            item = form.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('index')
    else:
        form = ItemCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Item/create_item.html', {
        'form': form
    })


def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('index')


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


def place_bid(request, id):
    instance = get_object_or_404(Item, pk=id)
    user = request.user
    if request.method == 'POST':
        form = BidCreateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.cleaned_data['bidder'] = user
            form.save()
            return redirect('item_details', id=id)
    else:
        form = BidCreateForm(instance=instance)
    return render(request, 'Item/place_bid.html', {
        'form': form,
        'id': id
    })
