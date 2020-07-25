from django.db import models

#Products
class Product(models.Model):

    POLISHES = 'Polishes'
    CARE = 'Care'
    CHOICES = [
        (POLISHES, 'Polishes'),
        (CARE, 'Care')
    ]
    category = models.CharField(
        max_length=20,
        choices=CHOICES,
        default=POLISHES,
    )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=11, choices=CHOICES, default='Polishes')

    def __str__(self):
        return self.name