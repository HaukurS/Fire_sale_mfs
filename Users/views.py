from django.shortcuts import render, redirect, get_object_or_404

from Users.form.user_form import ProfileUpdateForm
from Users.models import Profile, ProfileImage


def index(request):
    return render(request, 'User/Index.html')


def show_profile(request):
    id = request.user.id
    profile_obj = Profile.objects.get(user_id=id)
    context = {
        'user1': profile_obj
    }
    return render(request, 'User/Profile.html', context)


def update_profile(request):
    id = request.user.id
    instance = get_object_or_404(Profile, user_id=id)
    if request.method == 'POST':
        form = ProfileUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=instance)
    return render(request, 'User/update_profile.html', {
        'form': form,
    })
