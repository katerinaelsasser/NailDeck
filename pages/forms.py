from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["full_name", "email", "message"]
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Leave us a message"
                }
            )
        }