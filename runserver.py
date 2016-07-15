import os
import airthingy_api


_DB = os.environ.get('TEST_DB_URI', 'airthingy.db')

airthingy_api.database.init(_DB)
airthingy_api.app.run()
