from django.shortcuts import render
from items.forms.item_form import ItemCreateForm

# Create your views here.


def index(request):
    return render(request, 'Item/Index.html')


def create_item(request):
    if request.method == 'POST':
        print(1)
    else:
        form = ItemCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'candy/create_candy.html', {
        'form': form
    })

