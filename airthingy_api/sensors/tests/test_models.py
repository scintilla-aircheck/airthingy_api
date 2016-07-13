import unittest


class SensorUnitTestCase(unittest.TestCase):

    def setUp(self):
        self.sensor_data = {
            'slug': 'INOVAFIT_SDS_021',
            'name': 'Inovafit SDS-021',
            'target': 'DUST'}

    def test_clean_sets_slug(self):
        from ..models import Sensor
        self.sensor_data.pop('slug')
        sensor = Sensor(name='Inovafit SDS-021')
        sensor.clean()
        expected = 'INOVAFIT_SDS_021'
        self.assertEqual(expected, sensor.slug)

    def test_invalid_target_raises_exc(self):
        from ..models import Sensor
        from airthingy_api.exceptions import ValidationError
        self.sensor_data['target'] = 'BAD_TARGET'
        model = Sensor(**self.sensor_data)
        with self.assertRaises(ValidationError):
            model.validate()


class SensorDataPointUnitTestCase(unittest.TestCase):

    def setUp(self):
        from datetime import datetime
        time_now = datetime.utcnow().isoformat()
        self.model_data = {
            'datetime': time_now,
            'latitude': 34.0922,
            'longitude': 118.0755,
            'target': 'SO2',
            'unit': 'PPM',
            'value': 12.345
        }

    def test_invalid_unit_raises_exc(self):
        from ..models import SensorDataPoint
        from airthingy_api.exceptions import ValidationError
        self.model_data['unit'] = 'BAD_UNIT'
        model = SensorDataPoint(**self.model_data)
        with self.assertRaises(ValidationError):
            model.validate()


class SensorsIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        from datetime import datetime
        time_now = datetime.utcnow().isoformat()
        self.sensor_data = {'name': 'SPEC_SO2_20PPM'}
        self.data_point_data = {
            'datetime': time_now,
            'latitude': 34.0922,
            'longitude': 118.0755,
            'target': 'SO2',
            'unit': 'PPM',
            'value': 12.345
        }
