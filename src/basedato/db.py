from peewee import MySQLDatabase

# local
db = MySQLDatabase(
    'db-marte' ,
    user= 'root',
    pessword='',
    host='localhost',
    port=3306
)