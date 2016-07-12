from flask import Flask
from flask_restful import Api
from peewee import SqliteDatabase


# Set up Flask app and REST API
app = Flask(__name__)
api = Api(app)

# Configure database
database = SqliteDatabase('airthingy.db')
