from django import forms

class contact_form(forms.Form):
    contact_name = forms.CharField(label='Contact Name', max_length=255)
    contact_email = forms.CharField(label='Contact Email',max_length=255)
    contact_message = forms.CharField(required=True, widget=forms.Textarea)

class review_form(forms.Form):
    STAR_CHOICES = [(i, i) for i in range(1, 6)]

    review_star = forms.ChoiceField(label='Month', choices=STAR_CHOICES, required=False)
    review_message = forms.CharField(required=True,widget=forms.Textarea)