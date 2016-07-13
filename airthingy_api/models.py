import peewee

from . import database


class BaseModel(peewee.Model):
    """
    A base model class used to establish the target database and make up for
    peewee's missing clean and validate methods.
    """

    class Meta(object):
        database = database

    def clean(self):
        pass

    def validate(self):
        pass

    def save(self, *args, **kwargs):
        self.clean()
        self.validate()
        super().save(*args, **kwargs)
