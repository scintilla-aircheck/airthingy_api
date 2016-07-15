import os
import peewee
import airthingy_api


_models = (
    airthingy_api.sensors.models.Sensor,
    airthingy_api.sensors.models.SensorDataPoint,
)


def bootstrap(db=None):
    db = db or os.environ.get('TEST_DB_URI', 'airthingy.db')
    airthingy_api.database.init(db)
    peewee.create_model_tables(_models)


if __name__ == '__main__':
    bootstrap()
