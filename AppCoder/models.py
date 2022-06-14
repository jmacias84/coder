import email
from pyexpat import model
from django.db import models
from numpy import require

# Create your models here.
class family(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    relationship = models.CharField(max_length=10)
    