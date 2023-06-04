from django.db import models


# Create your models here.

class Feedback(models.Model):
    email = models.CharField(max_length=35)
    text = models.TextField()


class Items(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    price = models.IntegerField()
