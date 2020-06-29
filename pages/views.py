from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

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
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            message = contact_form.cleaned_data['message']
            from_email = contact_form.cleaned_data['email']
            send_mail(name, message, from_email, [
                      'k.elsasser@aol.co.uk'], fail_silently=False)
            messages.success(
                request, "Your message has been sent, we will be in touch soon.")
            return redirect('homepage')
    else:
        contact_form = ContactForm()
    return render(request, "contact.html", {'contact_form': contact_form})

# Your Images Page
def social_view(request):
    return render(request, "yourimages.html")