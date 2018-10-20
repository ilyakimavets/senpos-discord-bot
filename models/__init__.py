from peewee import Model, SqliteDatabase
from dynaconf import settings

db = SqliteDatabase(settings.DB_URL)


class BaseModel(Model):
    class Meta:
        database = db


from .quote import Quote


def init_database():
    db.connect()
    db.create_tables([Quote])

