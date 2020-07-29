from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
        else:
             messages.error(request, "Message was not sent")
        return redirect(reverse('contact'))
    return render(request, "contact.html", {'form': form})