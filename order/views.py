from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import OrderForm
from cart.cart import CartSession
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order

@login_required(login_url='login')
def create_order(request: HttpRequest):
    cart = CartSession(request.session)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer_user = request.user
            order.save()
            for item_cart in cart:
                OrderItem.objects.create(order=order, book=item_cart['book'], quantity=item_cart['quantity']).save()
            cart.clear()
            return redirect(reverse('account'))
    else:
        form = OrderForm()
    return redirect(reverse('cart_detail'))