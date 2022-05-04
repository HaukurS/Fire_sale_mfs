from django.shortcuts import render
from items import models

# Create your views here.

def home(request):
    return render(request, 'HomePage/Index.html')

def search_item(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = models.Item.filter(name__contains=searched)
        return render(request, 'HomePage/Search_item.html',
                      {'searched':searched,
                       'items':items})
    else:
        return render(request, 'HomePage/Search_item.html')
