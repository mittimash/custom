from peewee import *


db = SqliteDatabase('Flask-app-data.db')


class Navigation(Model):
    id = IntegerField(primary_key=True, null=False)
    name = CharField(null=False)
    description = TextField(null=True)
    url = CharField(null=False)

    class Meta:
        database = db