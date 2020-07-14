from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse

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
class ContactCreate(CreateView):
    model = Contact
    fields = ["name", "email", "message"]
    success_url = reverse_lazy("thanks")


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")

# Your Images Page
def social_view(request):
    return render(request, "yourimages.html")