from django.shortcuts import render

# Create your views here.

#about page
def about_view(request):
    return render(request, "about.html")
#payments page
def pay_view(request):
    return render(request, "payments.html")

#terms and conditions page
def terms_view(request):
    return render(request, "terms.html")