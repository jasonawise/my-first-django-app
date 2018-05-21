from django.db import models


# Create your models here.
class Question(models.Model):
    test_model = models.CharField(max_length=100)
