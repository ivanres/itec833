# This is a simple script to test that the LoggerServices is working
# If the database logs.db does not exist, run createdb.py first
# Make sure the server is running before executing this script
# Author: Ivan Rodriguez



from suds.client import Client
import logging
url = "http://localhost:7789/?wsdl"
client = Client(url)
#client.options.cache.clear()
#client.set_options(cache=None)


logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

#Reset remote database
result = client.service.add_log('123456', 'VISA')
print("Inserted row %d " % result)

