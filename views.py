from django.shortcuts import render
from .models import Nurse, Turno, FrancoProgramado, Licencia
from .forms import *

# Create your views here.


def inicio(request):
    
    return render(request, "inicio.html")


def index(request):
    if request.method == "POST":
        info_formulario = NurseForm(request.POST)
        
        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            nuevo_enfermero = Nurse(
                Nombre=info["Nombre"],
                Apellido=info["Apellido"],
                Profesion=info["Profesion"],
                fecha_ingreso=info["fecha_ingreso"]
            )
            nuevo_enfermero.save()
            return render(request, "Enfermeros.html")
    else:
        try:
            nuevo_formulario = NurseForm()
        except Exception as e:
            print(f"Error al crear el formulario: {e}")
            nuevo_formulario = None  
    
    return render(request, "Enfermeros.html", {"formu": nuevo_formulario if 'nuevo_formulario' in locals() else None})

def insertar_turno(request):
    if request.method == "POST":
        info_form = TurnoForm(request.POST)
        if info_form.is_valid():
            info = info_form.cleaned_data
            Nombre = info_form.cleaned_data['Nombre']
            Apellido = info_form.cleaned_data['Apellido']
            nuevo_turno = Turno(
                Nombre=Nombre,
                Apellido=Apellido,
                fecha=info["fecha"],
                descripcion=info["descripcion"]
            )
            nuevo_turno.save()
            
            return render(request, "turnos.html", {"x": nuevo_turno})
    else:
        try:
            nuevo_formulario = TurnoForm()
        except Exception as e:
            print(f"Error al crear el formulario: {e}")
            nuevo_formulario = None  
    
    return render(request, "turnos.html", {"x": nuevo_formulario if 'nuevo_formulario' in locals() else None})



def FrancoPedido(request):
    if request.method == 'POST':
        form = FrancoProgramadoForm(request.POST)
        if form.is_valid():
            Nombre = form.cleaned_data['Nombre']
            Apellido= form.cleaned_data['Apellido']
            fecha = form.cleaned_data['fecha']
            motivo = form.cleaned_data['motivo']
            nuevo_franco_programado = FrancoProgramado(
                Nombre =Nombre,
                Apellido=Apellido,
                fecha=fecha,
                motivo=motivo
            )
            nuevo_franco_programado.save()

            return render(request, 'FrancoPedido.html', {'form': form})
    else:
        form = FrancoProgramadoForm()

    return render(request, 'FrancoPedido.html', {'form': form})


def Lic(request):
    if request.method == "POST":
        form = LicenciaForm(request.POST)
        if form.is_valid():
            Nombre = form.cleaned_data['Nombre']
            Apellido= form.cleaned_data['Apellido']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            motivo = form.cleaned_data['motivo']

            nueva_licencia = Licencia(
                Nombre =Nombre,
                Apellido=Apellido,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                motivo=motivo
            )
            nueva_licencia.save()

            return render(request, "Licencias.html", {"form": form})
    else:
        form = LicenciaForm()
    return render(request, "Licencias.html", {"form": form})

def busqueda_enfermero(request):
    
    return render(request, "AppEnfermeria/buscar_enfermero.html")

def resultado_busqueda(request):
    
    if request.method=="GET":
        Nombre= request.GET["Nombre"]
        resultado_busqueda= Nurse.objects.filter(Nombre__icontains=Nombre)
    return render(request, "AppEnfermeria/buscar_enfermero.html",{"Nombre": resultado_busqueda})

