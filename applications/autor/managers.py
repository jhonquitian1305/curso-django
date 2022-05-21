from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """ managers para el modelo autor """

    # Filtrar por nombre
    def buscar_autor(self, kword):

        resultado = self.filter(
            nombre__icontains = kword
        )

        return resultado

    # Filtrar por nombre o apellido
    def buscar_autor2(self, kword):

        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)
        )

        return resultado

    # Excluyendo a los que tienen 70 años
    def buscar_autor3(self, kword):

        resultado = self.filter(
            nombre__icontains = kword
        ).exclude(
             Q(edad = 70) | Q(edad = 45)
        )

        return resultado

    def buscar_autor4(self, kword):

        resultado = self.filter(
            edad__gt = 40,
            edad__lt = 75
        ).order_by('apellidos', 'nombre')

        return resultado