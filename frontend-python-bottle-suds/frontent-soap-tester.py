# Client calls BPEL Web Service
# This will call the BPEL process deployed on Tomcat
# Author: Ivan Rodriguez

from suds.client import Client
import logging
url = "http://localhost:8080/ode/processes/WS_Integrator?wsdl"
location = "http://localhost:8080/ode/processes/WS_Integrator.WS_IntegratorPort" #Suds does not find the endpoint correctly, so we provide it manually
client = Client(url, location=location)

client.options.cache.clear()
client.set_options(cache=None)


logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

#Reset remote database
result = client.service.process('4556394058714517')
print("It is a %s credit card" % result)

