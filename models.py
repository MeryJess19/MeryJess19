from django.db import models

# Create your models here.

class Nurse(models.Model):
    
    Nombre= models.CharField(max_length=200)
    Apellido= models.CharField(max_length=100)
    Profesion= models.CharField(max_length=100)
    fecha_ingreso= models.DateField()
    
class Turno(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=100, default='')  
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)

class FrancoProgramado(models.Model):
    Nombre= models.CharField(max_length=200, default='ValorPorDefecto')
    Apellido= models.CharField(max_length=100, default='')  
    fecha = models.DateField()
    motivo = models.CharField(max_length=255)

class Licencia(models.Model):
    Nombre= models.CharField(max_length=200,default='your_default_value')
    Apellido = models.CharField(max_length=100, default='')  
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    motivo = models.CharField(max_length=255)
