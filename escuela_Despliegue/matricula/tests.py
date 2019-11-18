from django.test import TestCase
from matricula.models import Curso,Alumno
# Create your tests here.

class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(abrev="BACH", denom="Bachillerato", imagen="fotos/thor.jpg")
        Curso.objects.create(abrev="ESO", denom="Secundaria" )

    def test_curso_crear_curso(self):
       BACH = Curso.objects.get(abrev="BACH")
       ESO = Curso.objects.get(abrev="ESO")
       self.assertEqual(BACH.__str__(),"Bachillerato") 
       self.assertEqual(ESO.imagen,"")


class AlumnoTestCase(TestCase):
    def setUp(self):
        Alumno.objects.create(dni="11111111A", nombre="Verónica",apellidos="Toro Gómez", imagen="fotos/caty.jpg")

    def test_alumno_crear_alumno(self):
        DNI = Alumno.objects.get(dni="11111111A")
        self.assertEqual(len(DNI.dni),9)


        