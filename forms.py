from django import forms
from .models import *

class NurseForm(forms.Form):
    Nombre= forms.CharField(max_length=200)
    Apellido= forms.CharField(max_length=100)
    Profesion= forms.CharField(max_length=100)
    fecha_ingreso= forms.DateField()

class TurnoForm(forms.Form):
    Nombre= forms.CharField(max_length=200)
    Apellido= forms.CharField(max_length=100)
    fecha = forms.DateField()
    descripcion = forms.CharField(max_length=255)

class FrancoProgramadoForm(forms.Form):
    Nombre= forms.CharField(max_length=200)
    Apellido= forms.CharField(max_length=100)
    fecha = forms.DateField()
    motivo = forms.CharField(max_length=255)

class LicenciaForm(forms.Form):
    Nombre= forms.CharField(max_length=200)
    Apellido = forms.CharField(max_length=100)
    fecha_inicio = forms.DateField(input_formats=['%d/%m/%Y'])
    fecha_fin = forms.DateField(input_formats=['%d/%m/%Y'])
    motivo = forms.CharField(max_length=255)
    