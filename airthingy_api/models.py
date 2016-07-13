import peewee

from . import database


class BaseModel(peewee.Model):
    class Meta(object):
        database = database
