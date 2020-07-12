from django.shortcuts import render
from .models import Product, Category

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
    polish_category = Category.objects.get(category_name="polishes")
    polishes = Product.objects.filter(category='polishes')
    return render(request, "polish.html", {"polishes": polishes})

# Nail Care
def care_category(request, *args, **kwargs):
    """
    Displays all products that are in the care category
    """
    cares = Products.objects.filter(category=care)
    return render(request, "care.html", {"cares": cares})