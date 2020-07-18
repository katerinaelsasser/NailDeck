from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import contact_form

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
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success(request):
    return HttpResponse('Success! Thank you for your message.')