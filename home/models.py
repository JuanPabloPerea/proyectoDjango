from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class departamento(models.Model):
    codigo = models.IntegerField(primary_key=TRUE)
    nombre = models.CharField(max_length=100)
    presupuesto = models.FloatField()
    
class empleado(models.Model):
    codigo = models.IntegerField(primary_key=TRUE)
    nif = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)
