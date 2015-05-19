# Client calls BPEL Web Service
# This will call the BPEL process deployed on Tomcat
# Author: Ivan Rodriguez

from suds.client import Client
import logging



class BPEL:
    url = "http://localhost:8080/ode/processes/WS_Integrator?wsdl"
    location = "http://localhost:8080/ode/processes/WS_Integrator.WS_IntegratorPort" #Suds does not find the endpoint correctly, so we provide it manually

    def __init__(self):
        client = Client(self.url, location=self.location)

        client.options.cache.clear()
        client.set_options(cache=None)
        self.client = client


        logging.basicConfig(level=logging.INFO)
        logging.getLogger('suds.client').setLevel(logging.DEBUG)

    def process(self, cc_number):
        return self.client.service.process(cc_number)

if __name__ == '__main__':
    srv = BPEL()
    result = srv.process('4556394058714517')
    print("It is a %s credit card" % result)