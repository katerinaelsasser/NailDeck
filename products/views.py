from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, Category

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
    polish_category = Category.objects.get(title="polishes")
    polishes = Product.objects.filter(category='polishes')
    return render(request, "polish.html", {"products": products})

# Nail Care
@login_required
def care_category(request, *args, **kwargs):
    """
    Displays all products that are in the care category
    """
    cares = Products.objects.filter(category=care)
    return render(request, "care.html", {"cares": cares})