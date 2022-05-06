from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from Users.models import User
from checkout.form.checkout_form1 import ContactCreateForm
from checkout.form.checkout_form2 import PaymentInfoCreateForm


def create_paymentinfo(request):
    if request.method == 'POST':
        form = PaymentInfoCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PaymentInfoCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Item/create_item.html', {
        'form': form
    })


def create_contactinfo(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = ContactCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactCreateForm(instance=instance)
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Item/create_item.html', {
        'form': form
    })