from modelo.estudiantes import Estudiante
from modelo.cursos import Curso 

class EstudianteServicio:
    
  @staticmethod
  def crear_estudiante(nombre):

    estudiante = Estudiante.create(nombre=nombre)
    return estudiante

  @staticmethod
  def mostrar_estudiante():
    return list(Estudiante.select())
  
  @staticmethod
  def eliminar_estudiante(id):
    estudiante = Estudiante .get(Estudiante.id ==id)
    estudiante.delete_instanve()
    return estudiante
