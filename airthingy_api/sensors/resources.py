import flask

from playhouse.shortcuts import model_to_dict

from airthingy_api import resources

from . import schemas, models


_TARGETS = [t[0] for t in models.TARGETS]


class SensorData(resources.IModelResource):

    _MODEL = models.SensorDataPoint

    _SCHEMAS = {
        'POST': schemas.CreateSensorData(),
        'GET': schemas.GetSensorData()
    }

    def post(self):
        """
        Create a new collection of sensor data points.
        """
        params = self.get_params()
        if params.errors:
            return params.errors, 400
        else:
            data_points = params.data.pop('data')
            for data_point in data_points:
                data_point['datetime'] = params.data['datetime']
                data_point['latitude'] = params.data['latitude']
                data_point['longitude'] = params.data['longitude']
                self._MODEL.create(**data_point)
            return None, 204

    def get(self):
        """
        Query existing sensor data points.
        """
        params = self.get_params()
        if params.errors:
            flask.abort(400)

        cursor = self.get_cursor()
        target = params.data.get('target')
        if target:
            results = [model_to_dict(d) for d
                       in cursor.where(self.model.target == target)]
        else:
            results = [model_to_dict(d) for d in cursor]

        return flask.jsonify(results)
