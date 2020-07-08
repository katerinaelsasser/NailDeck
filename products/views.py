from django.shortcuts import render
from .models import Product

# Product Page
def all_products(request):
    """
    Displays all products
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

# Nail Polishes
def polish_category(request, *args, **kwargs):
    """
    Displays all products that are in the polish category
    """
    context = get_context('Polish')
    return render(request, "polish.html", context)

# Nail Care
def care_category(request, *args, **kwargs):
    """
    Displays all products that are in the care category
    """
    context = get_context('care')
    return render(request, "care.html", context)

# Content for Categories 
def get_context(category_name):
    """ Returns relevant context for category views """
    
    context = {
        'products': Product.objects.all().filter(category=category_name),
        'category': category_name
    }
    return context