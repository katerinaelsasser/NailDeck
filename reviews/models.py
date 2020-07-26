from django.db import models

#Reviews
class Review(models.Model):
    STAR_CHOICES =(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    review_star = models.CharField(max_length=11, choices=STAR_CHOICES, default='5')
    review_message = models.CharField(max_length=1024)

    def __str__(self):
        return self.review_star