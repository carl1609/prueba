from django.db import models

# Create your models here.
# models.py
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=[('pendiente', 'Pendiente'),
    ('completado', 'Completado')])
def __str__(self):
    return self.titulo

class Persona(models.Model):
    nombre=models.TextField()
    edad=models.IntegerField()
    dni=models.IntegerField()
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE)
