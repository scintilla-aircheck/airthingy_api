import os
import unittest


class UnitTestLayer(object):
    pass


class PeeWeeIntegrationTestLayer(UnitTestLayer):

    _DB = os.environ.get('TEST_DB_URI', ':memory:')

    @classmethod
    def setUp(cls):
        import airthingy_api
        from bootstrap import bootstrap
        airthingy_api.app.config['TESTING'] = True
        bootstrap(cls._DB)


class AppIntegrationTests(unittest.TestCase):

    layer = PeeWeeIntegrationTestLayer

    def setUp(self):
        import airthingy_api
        self.app = airthingy_api.app.test_client()
