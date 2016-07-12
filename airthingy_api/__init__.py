from .app import app, api, database

from . import sensors


# Helper method to establish database connection
@app.before_request
def _db_connect():
    database.connect()


# Helper method to close database connection
@app.teardown_request
def _db_close(exc):
    if not database.is_closed():
        database.close()


# Connect resources with respective endpoints
api.add_resource(sensors.resources.SensorData, '/data/', endpoint='get')
