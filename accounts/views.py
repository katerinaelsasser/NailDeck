from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm, UpdateUserDetailsForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from products.models import Product
from checkout.models import Order, OrderLineItem
from django.contrib.auth.models import User

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('homepage'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('homepage'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)

# Profile Page
@login_required
def profile(request):
 """  A view that displays order history and lets user update their detail """
    user = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        update_form = UpdateUserDetailsForm(
            request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(
                request, 'You have successfully updated your account details.')
            return redirect('profile')
    else:
        update_form = UpdateUserDetailsForm(instance=request.user)

    orders = Order.objects.filter(user=request.user)
    
    all_orders = []

    for order in orders:
        order_fetch = OrderLineItem.objects.filter(order=order)
        order_items = []
        order_total = 0
        for order_item in order_fetch:
            order_items.append(order_item)
            order_total += int(order_item.product.price * order_item.quantity)
        all_orders.append({'order': order, 'order_items': order_items, "total": order_total})
    
    print(all_orders)
    return render(request, 'profile.html', {"form": form, "all_orders": all_orders})

def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('homepage'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
