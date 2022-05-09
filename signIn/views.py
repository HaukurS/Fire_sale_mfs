from django.shortcuts import render, redirect
from signIn.forms.sign_in_forms import UserRegistration
from django.contrib.auth import authenticate, login
from Users.models import Profile
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        form = UserRegistration(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('homepage')
    else:
        form = UserRegistration()
    return render(request, 'SignIn/register.html', {'form': form})

#def user_profile(request):
#    profile = User.objects.filter(user=request.user).first()
#    if request.method == 'POST':
#        form = UserRegistration(data=request.POST)
#        if form.is_valid():
#            form.save()
#    #else:
     #   form = UserProfile()
#    return render(request, 'User/Profile.html', {'form': user_profile(instance=profile)})

