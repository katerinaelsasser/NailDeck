from django.db import models

# Create your models here.
class contactus(models.Model):
    name = = forms.CharField(max_length=100, label=_("Your name"))
    email = forms.EmailField(max_length=200, label=_("Your email address"))
    body = forms.CharField(widget=forms.Textarea, label=_("Your message"))
    
    def __str__(self):
        return self.name