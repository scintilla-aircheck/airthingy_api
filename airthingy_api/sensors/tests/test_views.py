import unittest


class SensorDataTestCase(unittest.TestCase):

    def setUp(self):
        from ..resources import SensorData
        self.resource = SensorData()
