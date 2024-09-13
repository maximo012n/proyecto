from servicio.curso_servicio import cursoServicio

class cursoControlador ():
    def crear(nombre,descripcion ):
        return cursoServicio.crear_curso(nombre, descripcion)
    
    def mostrar():
        return cursoServicio.mostrar_cursos()

