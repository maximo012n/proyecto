from modelo.cursos import Curso

class cursoServicio:
    @staticmethod
    def crear_curso(nombre):
        curso = Curso.create(nombre=nombre)
        return curso
    
    @staticmethod
    def mostrar_cursos():
        return list(Curso.select())
    
 