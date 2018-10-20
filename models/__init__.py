from peewee import Model, SqliteDatabase

db = SqliteDatabase('bot.db')


class BaseModel(Model):
    class Meta:
        database = db


from .quote import Quote


def init_database():
    db.connect()
    db.create_tables([Quote])

