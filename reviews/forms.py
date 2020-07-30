from django import forms
from django.forms import ModelForm
from .models import Review

class review_form(forms.Form):
    STAR_CHOICES = [(i, i) for i in range(1, 6)]

    review_star = forms.ChoiceField(label='Review Star', choices=STAR_CHOICES, required=False)
    review_message = forms.CharField(required=True,widget=forms.Textarea)