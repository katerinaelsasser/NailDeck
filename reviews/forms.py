from django import forms
from django.forms import ModelForm
from .models import Review

class review_form(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review_star', 'review_message')