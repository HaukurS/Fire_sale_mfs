from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'HomePage/Index.html')

def search_item(request):
    if request.method == "POST":
        searched = request.POST['searched']
        return render(request, 'HomePage/Search_item.html',
                      {'searched':searched})
    else:
        return render(request, 'HomePage/Search_item.html')
