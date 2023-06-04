from django.db import models


# Create your models here.

class Feedback(models.Model):
    email = models.CharField(max_length=35)
    text = models.TextField()
