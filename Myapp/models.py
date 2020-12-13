from django.db import models

# Create your models here.

class MyQuotes(models.Model):
    Quote  = models.CharField(max_length=500)
    Author  = models.CharField(max_length=100)
    likes  = models.IntegerField(blank=True, null =True)