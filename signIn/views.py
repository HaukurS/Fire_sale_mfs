from django.shortcuts import render, redirect
from signIn.forms.sign_in_forms import UserRegisterForm
from Users.models import User

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'SignIn/register.html', {'form': form})