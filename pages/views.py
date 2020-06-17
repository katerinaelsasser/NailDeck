from django.shortcuts import render

# Home Page 
def homepage(request):
    return render(request, "index.html")

#About page
def about_view(request):
    return render(request, "about.html")

#Terms and conditions page
def terms_view(request):
    return render(request, "terms.html")

#FAQ page
def faq_view(request):
    return render(request, "faq.html")
    
#Contact page
def contact_view(request):
    return render(request, "contact.html")