from django.shortcuts import render, redirect
from Users.models import Profile




def index(request):
    return render(request, 'User/Index.html')


def show_profile(request):
    #user = request.user
    #profile_obj = Profile.objects.get(user_id=user.id)
    id = request.user.id
    profile_obj = Profile.objects.get(user_id=id)
    context = {
        'user1': profile_obj
    }
    return render(request, 'User/Profile.html', context)
