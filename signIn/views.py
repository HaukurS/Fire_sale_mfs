from django.shortcuts import render, redirect
from signIn.forms.sign_in_forms import UserRegistration
from django.contrib.auth import authenticate, login
from Users.models import Profile
from django.contrib.auth.models import User


# function to register a user
def register_user(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = UserRegistration(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            new_profile = Profile(name = user.username, email = user.email, user_id = user.id)
            new_profile.save()
            return redirect('homepage')
    else:
        form = UserRegistration()
    return render(request, 'SignIn/register.html', {'form': form})

