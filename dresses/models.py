

from django.db import models

class Dress(models.Model):
    dress_name = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    colour = models.CharField(max_length=50)
    price = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.dress_name} ({self.size})"
# Create your models here.
