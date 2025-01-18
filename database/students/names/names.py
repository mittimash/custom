from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):

    id = AutoField()
    full_name = CharField()
    birthday = DateField()
    name = CharField()
    family_name = CharField()
    surname = CharField(null=True)

    class Meta:
        database = db
