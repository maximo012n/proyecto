from servicio.estudiante_servicio import EstudianteServicio

class cursoControlador ():

    def crear(nombre,descripcion ):
        return EstudianteServicio.crear_curso(nombre, descripcion)
    
    def mostrar():
        return EstudianteServicio.mostrar_cursos()
  