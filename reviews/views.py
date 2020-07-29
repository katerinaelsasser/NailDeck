from django.shortcuts import render, redirect
from .forms import review_form
from .models import Review
from django.contrib import messages

# Review Form
def review(request):
    if request.method == 'GET':
        form_review = review_form()
    else:
        form_review = review_form(request.POST)
        if form_review.is_valid():
            form.save() 
        else:
            messages.error(request, "Review was not sent")
            return redirect(reverse('review'))
    return render(request, "reviews.html", {'form_review': form_review})