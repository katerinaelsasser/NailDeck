from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, default='', blank=False)
    email = models.EmailField(max_length=200, default='', blank=False)
    message = models.TextField(max_length=1024, default='')


    def __str__(self):
        return self.name