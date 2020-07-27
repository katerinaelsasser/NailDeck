from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_form
from .models import Product
from django.core.mail import send_mail, BadHeaderError

# Contact Form
def contact(request):
    if request.method == 'GET':
        form_contact = contact_form()
    else:
        form_contact = contact_form(request.POST)
        if form_contact.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(contact_name, contact_message, contact_email, ['k.elsasser@aol.co.uk'])
                return render(request, "contactsent.html")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "contact.html", {'form_contact': form_contact})