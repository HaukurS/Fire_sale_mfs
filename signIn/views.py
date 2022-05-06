from django.shortcuts import render, redirect
from signIn.forms.sign_in_forms import UserRegistration
from Users.models import User
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        form = UserRegistration(data=request.POST)
        if form.is_valid() and request.POST['password'] == request.POST['re_enter_password']:
            form.save()
            user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
            return redirect('homepage')
    else:
        form = UserRegistration()
    return render(request, 'SignIn/register.html', {'form': form})