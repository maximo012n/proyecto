from peewee import Model, AutoField, CharField, DateField
from basedato.db import db
 
class Curso(Model):
    curso_id = AutoField()
    nombre = CharField(unique=True)
    descripcion = CharField()
    feoha_inioio = DateField()
    feoha_fin = DateField()
    horas= CharField()

    class Meta:
        database = db
        table_name ='cursos'
