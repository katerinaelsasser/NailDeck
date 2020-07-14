from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Would love to talk about Philip K. Dick"
                }
            )
        }