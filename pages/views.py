from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact

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
    class ContactCreate(CreateView):
    model = Contact
    fields = ["name", "email", "message"]
    success_url = reverse_lazy("thanks")


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")

# Your Images Page
def social_view(request):
    return render(request, "yourimages.html")