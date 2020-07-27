from django.shortcuts import render, redirect
from .forms import review_form
from .models import Review
from django.core.mail import send_mail, BadHeaderError

# Review Form
def review(request):
    reviews = reviews.objects.all()
    if request.method == 'GET':
        form_review = review_form()
    else:
        form_review = review_form(request.POST)
        if form_review.is_valid():
            review_star = form.cleaned_data['review_star']
            review_message = form.cleaned_data['review_message']
            try:
                return render(request, "review.html")
            except BadHeaderError:
                return HttpResponse('Invalid.')
    return render(request, "reviews.html", {'form_review': form_review, 'reviews': reviews})