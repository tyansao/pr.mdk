from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, ProfileForm
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db.models import Q
from order.models import Order, OrderItem


def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('mainPage')
    else:
        form = RegisterForm
    return render(request, 'register.html', {
        'form' : form,
    })

def loginUser(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('mainPage')
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form' : form,
    })

def logoutUser(request):
    logout(request)
    return redirect('mainPage')

@login_required(login_url='login')
def profileView(request: HttpRequest):
    user = Profile.objects.select_related('user').get(user=request.user)
    orders = Order.objects.filter(Q(customer_user=request.user)).select_related('customer_user').prefetch_related('items__book')
    return render(request, 'profile.html', {
        'user': user,
        'orders': orders,
    })

@login_required(login_url='login')
def profileEdit(request: HttpRequest):
    user = Profile.objects.select_related('user').get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'profile_edit.html', {
        'form' : form,
    })


