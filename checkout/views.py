from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from Users.models import User
from checkout.form.checkout_form1 import ContactCreateForm
from checkout.form.checkout_form2 import PaymentInfoCreateForm
from checkout.models import PaymentInfo


def create_paymentinfo(request):
    if request.method == 'POST':
        form = PaymentInfoCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = PaymentInfoCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Checkout/step_two.html', {
        'form': form
    })


def create_contactinfo(request):
    if request.method == 'POST':
        form = ContactCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('step_two')
    else:
        form = ContactCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Checkout/step_one.html', {
        'form': form
    })


def review_checkout(request):
    payment_info = PaymentInfo.objects.last()
    contact_info = User.objects.last()
    return render(request, 'Checkout/review.html', {
        'contact_info': contact_info,
        'payment_info': payment_info
    })
