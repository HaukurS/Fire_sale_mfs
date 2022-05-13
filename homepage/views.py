from django.shortcuts import render
from items.models import Item, ItemBid

# Create your views here.

#function to render the homepage
def home(request):
    return render(request, 'HomePage/Index.html')

#function for the search bar
def search_item(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter(name__icontains=searched)
        return render(request, 'HomePage/Search_item.html',
                      {'searched': searched,
                       'items': items})
    else:
        return render(request, 'HomePage/Search_item.html')


def handler404(request, exception):
    return render(request, '404.html')





