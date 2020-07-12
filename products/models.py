from django.db import models

# Categories 
class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

#Products
class Product(models.Model):
    CHOICES =(
        ('polishes', 'Polishes'),
        ('care', 'Care')
    )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=11, choices=CHOICES, default='polishes')

    def __str__(self):
        return self.name