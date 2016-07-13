import flask
import flask_restful as frest

from playhouse.shortcuts import model_to_dict

from . import schemas, models


_TARGETS = [t[0] for t in models.TARGETS]


class SensorData(frest.Resource):
    """`/api/{version}/data/"""

    _MODEL = models.SensorDataPoint

    @property
    def _cursor(self):
        return self._MODEL.select()

    def post(self):
        """
        Create a new collection of sensor data points.
        """
        data, errors = self.sanitize_data(schemas.CreateSensorData)
        if errors:
            flask.abort(400)
        else:
            data_points = data.pop('data')
            for data_point in data_points:
                data_point['datetime'] = data['datetime']
                data_point['latitude'] = data['latitude']
                data_point['longitude'] = data['longitude']
                self._MODEL.create(**data_point)
            return None, 204

    def get(self):
        """
        Query existing sensor data points.
        """
        raw_data = flask.request.args
        schema = schemas.GetSensorData()
        schema_out = schema.load(raw_data)
        if schema_out.errors:
            flask.abort(400)

        target = schema_out.data.get('target')
        if target:
            results = [model_to_dict(d) for d in self._cursor.where(self._MODEL.target == target)]
        else:
            results = [model_to_dict(d) for d in self._cursor]

        return flask.jsonify(results)

    @staticmethod
    def sanitize_data(schema, **kwargs):
        """
        Shortcut method to sanitize data with a given schema and return any
        errors.

        :param schema: A schema class
        :return: A two-tuple containing data and form errors
        """
        if flask.request.method == 'GET':
            raw_data = flask.request.args
        else:
            raw_data = flask.request.get_json()
        schema = schema(**kwargs)
        schema_output = schema.load(raw_data)
        return schema_output.data, schema_output.errors
