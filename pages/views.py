from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import contact_form, review_form
from .models import Review
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect

# Home Page 
def homepage(request):
    return render(request, "index.html")

# About page
def about_view(request):
    return render(request, "about.html")

#Terms and conditions page
def terms_view(request):
    return render(request, "terms.html")

# Your Images Page
def social_view(request):
    return render(request, "yourimages.html")

# Contact Form
def contact(request):
    if request.method == 'GET':
        form = contact_form()
    else:
        form = contact_form(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(contact_name, contact_message, contact_email, ['k.elsasser@aol.co.uk'])
                return render(request, "contactsent.html")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "contact.html", {'form': form})

# Review Form
def review(request):
    if request.method == 'GET':
        form = review_form()
    else:
        form = review_form(request.POST)
        if form.is_valid():
            review_star = form.cleaned_data['review_star']
            review_message = form.cleaned_data['review_message']
            try:
                return render(request, "reviewsent.html")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "reviews.html", {'form': form})
