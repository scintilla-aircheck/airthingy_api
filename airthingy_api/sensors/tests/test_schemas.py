import unittest


class CreateSensorTestCase(unittest.TestCase):

    def setUp(self):
        from ..schemas import CreateSensor
        self.schema = CreateSensor()

    def test_invalid_slug_raises_exception(self):
        sensor_data = {
            'slug': 'Invalid Slug!',
            'name': 'Inovafit SDS-021',
            'target': 'DUST'}
        result = self.schema.load(sensor_data)
        self.assertIn('slug', result.errors)

    def test_invalid_target_raises_exception(self):
        sensor_data = {
            'slug': 'INOVAFIT_SDS_021',
            'name': 'Inovafit SDS-021',
            'target': 'BAD_TARGET'}
        result = self.schema.load(sensor_data)
        self.assertIn('target', result.errors)


class CreateSensorDataPointTestCase(unittest.TestCase):

    def setUp(self):
        from ..schemas import CreateSensorDataPoint
        self.schema = CreateSensorDataPoint()
        self.form_data = {
            'unit': 'PPM',
            'target': 'SO2',
            'value': 12.345}

    def test_target_required(self):
        self.form_data.pop('target')
        result = self.schema.load(self.form_data)
        self.assertIn('target', result.errors)

    def test_unit_required(self):
        self.form_data.pop('unit')
        result = self.schema.load(self.form_data)
        self.assertIn('unit', result.errors)

    def test_value_required(self):
        self.form_data.pop('value')
        result = self.schema.load(self.form_data)
        self.assertIn('value', result.errors)

    def test_invalid_target_fails_validation(self):
        self.form_data['target'] = 'BAD_TARGET'
        result = self.schema.load(self.form_data)
        self.assertIn('target', result.errors)

    def test_invalid_unit_fails_validation(self):
        self.form_data['unit'] = 'BAD_UNIT'
        result = self.schema.load(self.form_data)
        self.assertIn('unit', result.errors)


class CreateSensorDataTestCase(unittest.TestCase):

    def setUp(self):
        from ..schemas import CreateSensorData
        from datetime import datetime
        self.schema = CreateSensorData()
        time_now = datetime.utcnow().isoformat()
        self.form_data = {
            'datetime': time_now,
            'latitude': 34.0922,
            'longitude': 118.0755,
            'data': [
                {
                    'target': 'SO2',
                    'unit': 'PPM',
                    'value': 12.345
                }
            ]
        }

    def test_datetime_required(self):
        self.form_data.pop('datetime')
        result = self.schema.load(self.form_data)
        self.assertIn('datetime', result.errors)

    def test_latitude_required(self):
        self.form_data.pop('latitude')
        result = self.schema.load(self.form_data)
        self.assertIn('latitude', result.errors)

    def test_longitude_required(self):
        self.form_data.pop('longitude')
        result = self.schema.load(self.form_data)
        self.assertIn('longitude', result.errors)

    def test_data_required(self):
        self.form_data.pop('data')
        result = self.schema.load(self.form_data)
        self.assertIn('data', result.errors)

    def test_data_not_empty(self):
        self.form_data['data'] = []
        result = self.schema.load(self.form_data)
        self.assertIn('data', result.errors)


class RetrieveSensorDataTestCase(unittest.TestCase):

    def setUp(self):
        from ..schemas import RetrieveSensorData
        self.schema = RetrieveSensorData()

    def test_invalid_target_fails_validation(self):
        form_data = {'target': 'BAD_TARGET'}
        result = self.schema.load(form_data)
        self.assertIn('target', result.errors)

    def test_offset_default_zero(self):
        form_data = {'target': 'SO2'}
        result = self.schema.load(form_data)
        offset = result.data['offset']
        self.assertEqual(0, offset)

    def test_limit_default_zero(self):
        form_data = {'target': 'SO2'}
        result = self.schema.load(form_data)
        offset = result.data['limit']
        self.assertEqual(100, offset)

