from django.db import models


# Create your models here.
class MyFirstModel(models.Model):
    test_model = models.CharField(max_length=100)
