from django.shortcuts import render, redirect
from Users.form.user_form import UserCreateForm
# Create your views here.


def index(request):
    return render(request, 'User/Index.html')


def create_user(request):
    if request.method == 'POST':
        pass
    else:
        form = UserCreateForm()