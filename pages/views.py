from django.shortcuts import render

# Home Page 
def homepage(request):
    return render(request, "index.html")

#About page
def about_view(request):
    return render(request, "about.html")

#Payments page
def pay_view(request):
    return render(request, "payments.html")

#Terms and conditions page
def terms_view(request):
    return render(request, "terms.html")