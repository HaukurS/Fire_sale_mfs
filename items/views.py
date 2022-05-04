from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'Item/Index.html')


def create_item(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
        # TODO: Instance new ItemCreateForm()

