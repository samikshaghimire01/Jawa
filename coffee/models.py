
from django.db import models

# Create your models here.
class Coffee(models.Model):

    DRINK_CHOICES = [
        ('H', 'Hot'),
        ('C', 'Cold'),
        ('N', 'Normal'),
    ]
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    drink = models.CharField(max_length=1, choices=DRINK_CHOICES, default='N')
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    body = models.TextField()
    # models.py

