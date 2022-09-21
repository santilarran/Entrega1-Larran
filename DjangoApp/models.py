from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)

