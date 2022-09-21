from django.shortcuts import render
from django.http import HttpResponse
from DjangoApp.models import *
from DjangoApp.forms import *

# Create your views here.

def inicio(request):
    return render(request,'DjangoApp/inicio.html')

def curso(request):
    return render(request,'DjangoApp/cursos.html')

def estudiante(request):
    return render(request,'DjangoApp/estudiantes.html')

def profesor(request):
    return render(request,'DjangoApp/profesores.html')


def formulario1(request):
    if request.method=="POST":

        formulario1 = FormEstudiante(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            EstF = Estudiante(nombre = info["nombre"], apellido = info["apellido"], email = info["email"])

            EstF.save()

            return render(request, "DjangoApp/inicio.html")
    
    else:
        
        formulario1 = FormEstudiante()
    
    return render(request, "DjangoApp/form1.html", {"form1":formulario1})

def formulario2(request):
    if request.method=="POST":

        formulario2 = FormCurso(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            cursoF = Curso(nombre = info["nombre"], camada = info["camada"])

            cursoF.save()

            return render(request, "DjangoApp/inicio.html")
    
    else:
        
        formulario2 = FormCurso()
    
    return render(request, "DjangoApp/form2.html", {"form2":formulario2})

def formulario3(request):
    if request.method=="POST":

        formulario3 = FormProfesor(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            ProfF = Profesor(nombre = info["nombre"], apellido = info["apellido"])

            ProfF.save()

            return render(request, "DjangoApp/inicio.html")
    
    else:
        
        formulario3 = FormProfesor()
    
    return render(request, "DjangoApp/form3.html", {"form3":formulario3}) 


def busquedaCursos(request):

    return render(request, "DjangoApp/busquedaCursos.html")

def buscar(request):

    if request.GET["camada"]:

        busqueda = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains = busqueda)

        return render(request, "DjangoApp/resultados.html", {"cursos":cursos, "busqueda":busqueda})

    else:

        mensaje = "No enviaste datos."

    return HttpResponse(mensaje)
