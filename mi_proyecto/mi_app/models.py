from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    lanzamiento = models.DateField()
    portada = models.ImageField(upload_to='albumes', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    duracion = models.DurationField()

    def __str__(self):
        return self.titulo
# Create your models here.
