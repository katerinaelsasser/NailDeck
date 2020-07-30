from django.shortcuts import render, redirect
from .forms import review_form
from .models import Review
from django.contrib import messages

# Review Form
def review(request):
    if request.method == 'GET':
        form = review_form()
    else:
        form = review_form(request.POST)
        if form.is_valid():
            form.save() 
        else:
            messages.error(request, "Review was not sent")
            return redirect(reverse('review'))
    return render(request, "reviews.html", {'form': form})