from django.shortcuts import render, redirect

# Create your views here.
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
