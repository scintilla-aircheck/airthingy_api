import unittest


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


class GetSensorDataTestCase(unittest.TestCase):

    def setUp(self):
        from ..schemas import GetSensorData
        self.schema = GetSensorData()

    def test_invalid_target_fails_validation(self):
        form_data = {'target': 'BAD_TARGET'}
        result = self.schema.load(form_data)
        self.assertIn('target', result.errors)