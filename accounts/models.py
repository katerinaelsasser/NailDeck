from django.db import models

# Create your models here.
class order_history(models.Model):
    date = models.DateField()
    product = models.CharField(max_length=254, default='')
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name