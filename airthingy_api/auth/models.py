import os
import hashlib
import peewee


class APIToken(peewee.Model):
    """
    A table managing access tokens.
    """

    key = peewee.CharField(max_length=56)

    @staticmethod
    def new_key():
        return hashlib.sha224(os.urandom(128)).hexdigest()

    def clean(self):
        if not self.key:
            self.key = self.new_key()
