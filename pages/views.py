from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import FormView

# Home Page 
def homepage(request):
    return render(request, "index.html")

#About page
def about_view(request):
    return render(request, "about.html")

#Terms and conditions page
def terms_view(request):
    return render(request, "terms.html")

#Contact page
def contact_view(request):
    
    return render(request, 'contact.html')

# Your Images Page
def social_view(request):
    return render(request, "yourimages.html")