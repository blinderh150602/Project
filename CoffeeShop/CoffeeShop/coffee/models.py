from unittest.util import _MAX_LENGTH
from django.db import models
class coffee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=500)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    