from django.db import models

class Peliculas(models.Model):
  nombre = models.CharField(max_length=30)
  descripcion = models.CharField(max_length=30)
  disponible = models.BooleanField()
  director = models.CharField(max_length=30)