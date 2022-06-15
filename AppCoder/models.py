import email
from pyexpat import model
from django.db import models
from numpy import require

# Create your models here.
class family(models.Model):
    nombre = models.CharField(max_length=30)
    fechanacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    parentesco = models.CharField(max_length=10)
    
    def __str__(self):
        fila = "nombre: " + self.name + " - " + "fechanacimiento: " + str(self.date_of_birth) + " - " + "fenero: " + self.gender + " - " + "parentesco: " + self.relationship
        return fila
    