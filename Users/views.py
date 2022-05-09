from django.shortcuts import render, redirect
from Users.form.user_form import UserCreateForm
from Users.models import Profile
# Create your views here.



def index(request):
    return render(request, 'User/Index.html')


def show_profile(request, id):
    profile_obj = Profile.objects.get(user_id=id)
    context = {
        'user': profile_obj
    }
    return render(request, 'User/Profile.html', context)
