from peewee import *


db = SqliteDatabase('Flask-app-data.db')


class Users(Model):
    id = IntegerField(primary_key=True)
    username = CharField(null=False, unique=True)
    password = CharField(null=False)
    email = CharField(null=False, unique=True)

    class Meta:
        database = db

