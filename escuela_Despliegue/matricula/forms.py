from django.forms import ModelForm
from .models import Alumno
from .models import Curso


# Crea la clase del formulario
class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['dni', 'nombre', 'apellidos', 'imagen', 'curso']

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['abrev', 'denom', 'imagen']

#class FormLogin(Form)
#         user=CharField(max_length=20)
#         pwd=CharField(max_length=20)