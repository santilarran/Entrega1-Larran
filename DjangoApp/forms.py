from django import forms


class FormEstudiante(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class FormCurso(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class FormProfesor(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)