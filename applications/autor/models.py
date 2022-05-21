from django.db import models

# Managers
from .managers import AutorManager

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

    objects = AutorManager()

    def __str__(self):
        return f'{self.nombre}-{self.apellidos}'