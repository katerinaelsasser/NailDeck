from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    message = models.TextField(max_length=1024)


    def __str__(self):
        return self.name