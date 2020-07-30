from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'GET':
        ContactForm = ContactForm()
    else:
        form = ContactForm(request.POST)
        if ContactForm.is_valid():
            ContactForm.save() 
        else:
             messages.error(request, "Message was not sent")
        return redirect(reverse('contact'))
    return render(request, "contact.html", {'ContactForm': ContactForm})