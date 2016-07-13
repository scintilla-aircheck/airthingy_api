import peewee

from airthingy_api import sensors


_models = (
    sensors.models.Sensor,
    sensors.models.SensorDataPoint,
)


peewee.create_model_tables(_models)
