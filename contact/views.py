from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['k.elsasser@aol.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('confirmation')
    return render(request, "contact.html", {'form': form})

def contact_sent(request):
    return render(request, "contantsent.html")