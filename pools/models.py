from django.db import models


# Create your models here.

class Feedback(models.Model):
    email = models.CharField(max_length=35)
    text = models.TextField()


class Items(models.Model):
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True)
    name = models.CharField(max_length=30)
    price = models.CharField()


class Clients(models.Model):
    surname = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    feedback = models.TextField()


class Orders(models.Model):
    item = models.IntegerField()
    client = models.TextField()
