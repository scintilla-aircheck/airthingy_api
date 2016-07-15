from airthingy_api import testing


class SensorsTestCase(testing.AppIntegrationTests):

    def setUp(self):
        from peewee import create_model_tables
        from ..models import Sensor
        create_model_tables(Sensor)

    def tearDown(self):
        from ..models import Sensor
        Sensor.drop_table()

    def test_none_body_returns_400(self):
        response = self.app.post('/sensors/')
        self.assertEqual(400, response.status_code)

    def test_post_creates_sensor(self):
        import json
        sensor_data = {
            'slug': 'INOVAFIT_SDS_021',
            'name': 'Inovafit SDS-021',
            'target': 'DUST'}
        response = self.app.post(
            '/sensors/',
            data=json.dumps(sensor_data),
            content_type='application/json')
