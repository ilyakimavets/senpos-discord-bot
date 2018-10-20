import peewee

from . import BaseModel


class Quote(BaseModel):
    author_id = peewee.IntegerField()
    text = peewee.TextField(unique=True)
