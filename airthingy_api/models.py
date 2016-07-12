from peewee import Model

from . import database


class BaseModel(Model):
    class Meta(object):
        database = database
