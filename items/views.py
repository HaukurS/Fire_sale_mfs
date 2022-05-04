from django.shortcuts import render, redirect
from items.forms.item_form import ItemCreateForm
from items.models import ItemImage

# Create your views here.


def index(request):
    return render(request, 'Item/Index.html')


def create_item(request):
    if request.method == 'POST':
        print(1)
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('index')
    else:
        print(2)
        form = ItemCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Item/create_item.html', {
        'form': form
    })

