import flask
import peewee

from airthingy_api import resources

from . import schemas, models


_TARGETS = [t[0] for t in models.TARGETS]


class Sensors(resources.IModelResource):

    _MODEL = models.Sensor

    _SCHEMAS = {
        'POST': schemas.CreateSensor(),
        'GET': schemas.RetrieveSensors()
    }

    def post(self):
        params, errors = self.get_params()

        if errors:
            return errors, 400

        sensor = self.model.create(**params)
        return flask.jsonify(sensor.serialize()), 204

    def get(self):
        params, errors = self.get_params()

        if errors:
            return errors, 400

        cursor = self.get_cursor()
        target = params.get('target')
        if target:
            cursor = cursor.where(self.model.target == target)
        results = [d.serialize() for d in cursor]

        return flask.jsonify(results)


class SensorDetail(resources.IModelResource):

    _MODEL = models.Sensor

    _SCHEMAS = {
        'PUT': schemas.UpdateSensor(),
    }

    def get(self, sensor):
        try:
            sensor = self.model.get(slug=sensor)
        except peewee.DoesNotExist:
            flask.abort(404)

        return flask.jsonify(sensor.serialize())

    def put(self, sensor):
        params, errors = self.get_params()

        if errors:
            return errors, 400

        result = self.model.update(**params).where(
            self.model.slug == sensor).execute()

        if result:
            return None, 204

        else:
            flask.abort(404)


class SensorData(resources.IModelResource):

    _MODEL = models.SensorDataPoint

    _SCHEMAS = {
        'POST': schemas.CreateSensorData(),
        'GET': schemas.RetrieveSensorData()
    }

    def post(self):
        params, errors = self.get_params()

        if errors:
            return errors, 400

        data_points = params.pop('data')
        for idx, data_point in enumerate(data_points):
            sensor_slug = data_point['sensor']

            sensor = models.Sensor.get_or_create(slug=sensor_slug)

            data_point['sensor'] = sensor
            data_point['datetime'] = params['datetime']
            data_point['latitude'] = params['latitude']
            data_point['longitude'] = params['longitude']

            self.model.create(**data_point)
        return None, 204

    def get(self):
        params, errors = self.get_params()
        if errors:
            flask.abort(400)
        cursor = self.get_cursor()
        target = params.get('target')
        if target:
            results = [d.serialize() for d
                       in cursor.where(self.model.target == target)]
        else:
            results = [d.serialize() for d in cursor]
        return flask.jsonify(results)
