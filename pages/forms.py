from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "message"]
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Would love to talk about Philip K. Dick"
                }
            )
        }