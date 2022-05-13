from django.shortcuts import render, redirect, get_object_or_404

from Users.models import Profile
from checkout.form.checkout_form1 import ContactCreateForm
from checkout.form.checkout_form2 import PaymentInfoCreateForm
from checkout.models import PaymentInfo
from items.models import Item, ItemBid
from django.contrib.auth.decorators import login_required


@login_required
def create_contactinfo(request, id):
    user_id = request.user.id
    profile_obj = get_object_or_404(Profile, user_id=user_id)
    bid_obj = get_object_or_404(ItemBid, id=id)
    if bid_obj.bidder_id != profile_obj.id:
        return redirect('homepage')
    instance = get_object_or_404(Profile, user_id=user_id)
    if request.method == 'POST':
        form = ContactCreateForm(data=request.POST, instance=instance)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('step_two', id)
    else:
        form = ContactCreateForm(instance=instance)
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Checkout/step_one.html', {
        'form': form,
        'bid': bid_obj
    })


@login_required
def create_paymentinfo(request, id):
    user_id = request.user.id
    profile_obj = get_object_or_404(Profile, user_id=user_id)
    bid_obj = get_object_or_404(ItemBid, id=id)
    if bid_obj.bidder_id != profile_obj.id:
        return redirect('homepage')
    if request.method == 'POST':
        form = PaymentInfoCreateForm(data=request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.profile = profile_obj
            payment.save()
            return redirect('review', id)
    else:
        form = PaymentInfoCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'Checkout/step_two.html', {
        'form': form,
        'bid': bid_obj
    })


def review_checkout(request, id):
    user_id = request.user.id
    profile_obj = get_object_or_404(Profile, user_id=user_id)
    bid_obj = get_object_or_404(ItemBid, id=id)
    if bid_obj.bidder_id != profile_obj.id:
        return redirect('homepage')
    item = get_object_or_404(Item, id=bid_obj.item_id)
    contact_info = get_object_or_404(Profile, user_id=user_id)
    payment_info = PaymentInfo.objects.last()
    return render(request, 'Checkout/review.html', {
        'contact_info': contact_info,
        'payment_info': payment_info,
        'item': item
    })
