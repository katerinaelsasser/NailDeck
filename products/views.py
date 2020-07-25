from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# Product Page
@login_required
def all_products(request):
    """
    Displays all products
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

# Nail Polishes
@login_required
def polish_category(request, *args, **kwargs):
    """
    Displays all products that are in the polish category
    """
     if request.method == 'POST':
        context = get_post_request_context(request, 'Polishes')
        return render(request, "polish.html", context)

    context = get_context('Polishes')
    return render(request, "polish.html", context)

# Nail Care
@login_required
def care_category(request, *args, **kwargs):
    """
    Displays all products that are in the care category
    """
    if request.method == 'POST':
        context = get_post_request_context(request, 'Care')
        return render(request, "care.html", context)

    context = get_context('Care')
    return render(request, "care.html", context)

def get_post_request_context(post_request, category_name):
    context = {
        'products': results,
        'select': sort,
        'category': category_name
    }
    return context

def get_context(category_name):
    """ Returns relevant context for category views """
    
    context = {
        'products': Product.objects.all().filter(category=category_name),
        'category': category_name
    }
    return context