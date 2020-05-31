from django.shortcuts import render

# Create your views here.

#about page
def about(request):
    return render(request, "about.html")
#payments page
def payments(request):
    return render(request, "payments.html")

#terms and conditions page
def terms(request):
    return render(request, "terms.html")