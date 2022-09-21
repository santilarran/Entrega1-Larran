from django.urls import path
from DjangoApp.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cursos/', curso, name="Curso"),
    path('profesores/', profesor, name="Profesores"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('form1', formulario1, name = "FormEst"),
    path('form2', formulario2, name = "FormCursos"),
    path('form3', formulario3, name = "FormProf"),
    path('buscarCursos/', busquedaCursos, name = "Buscar"),
    path('buscar/', buscar),
]
