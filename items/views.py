from django.shortcuts import render, redirect, get_object_or_404
from items.forms.item_form import ItemCreateForm
from items.models import ItemImage, Item
from Users.models import User

# Create your views here.


def index(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'Item/Index.html', context)


def get_item_by_id(request, id):
    return render(request, 'Item/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })


def get_items_by_category(request, category):
    context = {'items': Item.objects.filter(category__item__name=category)}
    return render(request, 'Item/Index.html', context)


def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
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
    redirect('index')

