from peewee import *
from .users import Users

db = SqliteDatabase('Flask-app-data.db')


class Posts(Model):
    id = IntegerField(primary_key=True)
    user = ForeignKeyField(Users, backref='posts')
    title = CharField(null=False)
    content = TextField(null=False)

    class Meta:
        database = db