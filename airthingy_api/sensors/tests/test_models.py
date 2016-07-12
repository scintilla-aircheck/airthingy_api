import unittest


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

    def test_datetime_is_required(self):
        from ..models import SensorDataPoint
        self.model_data.pop('datetime')
        model = SensorDataPoint(**self.model_data)
        self.fail('Need validation test patern for peewee models')
