from django import forms
from .models import Alumno, Curso, NotasAlumnosPorCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'cui']


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']


class NotasAlumnosPorCursoForm(forms.ModelForm):
    class Meta:
        model = NotasAlumnosPorCurso
        fields = ['alumno', 'curso', 'nota']
