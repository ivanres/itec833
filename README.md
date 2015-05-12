# ITEC833 Group Assignment

This is a demonstration of composition of web services using BPEL.

## Structure
The structure so far is as follows

### itec833_tomcat_ode
Integration Server.
This is a Tomcat 6 server. It contains Apache ODE and the BPEL process

### integrator-bpel-ode
BPEL project source files.

### axis-logger-service
`SqlLoggerService` project files.

### sampledb
This is a sample database used by the `SqlLoggerService`
Place the `logs.db` database in `C:\databases`. At the moment the location it is hardcoded in that path.
`C:\databases\logs.db`

### tomcat7_8082
Private Web Service server.
This is a tomcat 7 server. It contains the `SqlLoggerService` web service.

### frontend-python-bottle-suds
This will be the front end server. Work in progress.

### logger_service-python-soaplib (DEPRECATED)
Python Logger Service. First attempt of the logger service implemented in python. Web service works but Apache ODE does not accept it
Integration 


## Execution
Both tomcat servers should be started to test

1. `itec833_tomcat_ode\bin\startup.bat`
2. `tomcat7_8082\bin\startup.bat`
3. Until front end is available, use SoapUI to test. 
   Test entry point to Integration Server is at: `http://localhost:8080/ode/processes/WS_Integrator?wsdl`
   
Perform a service call with a fake credit card number. 

Expected results:
1. The credit card type (Visa, Mastercard, etc)
2. A new row written in the sqlite database.

