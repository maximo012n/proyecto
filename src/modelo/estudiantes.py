from peewee import Model, AutoField, CharField, DateField,IntegerField, ForeignKeyField
from basedato.db import db
from modelo.cursos import Curso 
 
class Estudiante(Model):
    estudiante_id= AutoField()
    nombre= CharField()
    dni= IntegerField(unique=True)
    email= CharField()
    telefono=IntegerField()
    fecha_nacimiento= DateField()
    ourso_id = ForeignKeyField(Curso)

    class meta :
        database=db
        table_nama= 'estudiantes'
      