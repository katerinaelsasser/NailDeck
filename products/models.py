from django.db import models

# Create your models here.
class Product(models.Model):
    Nail_Polishes = 'Polishes'
    Nail_Care = 'NailCare'
    Category_Options = [(Nail_Polishes, 'Polishes'), (Nail_Care, 'NailCare'),
    ]
    category = models.CharField(max_length=20, choices=Category_Options, default=Nail_Polishes)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')



    def __str__(self):
        return self.name