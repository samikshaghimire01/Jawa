from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
    
class Comment(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    body = models.TextField()