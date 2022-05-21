from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    """ Managers para el modelo libro"""

    def listar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range = ('1969-01-01', '1972-01-01')
        )

        return resultado