# ITEC833 Group Assignment

This is a demonstration of composition of web services using BPEL.

## How to run
Both tomcat servers should be started to test

1. `itec833_tomcat_ode\bin\startup.bat` BPEL server
2. `tomcat7_8082\bin\startup.bat` Logger server
3. Start the python server `C:\Python27\python.exe frontend-python-bottle-suds\server.py`
4. Access the front end at `http://localhost:8888/`
5. Optionally, use SoapUI to test. 
   Test entry point to Integration Server is at: `http://localhost:8080/ode/processes/WS_Integrator?wsdl`
   
Perform a service call with a fake credit card number. 

Expected results:
1. The credit card type (Visa, Mastercard, etc)
2. A new row written in the sqlite database.


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
This is the webpage that is loaded by the user. It displays a form where credit card numbers can be submitted. There is also a button to tests the REST interface.

### logger_service-python-soaplib (DEPRECATED)
Python Logger Service. First attempt of the logger service implemented in python. Web service works but Apache ODE does not accept it
Integration 



##Troubleshoot
###Tomcat
The Tomcat servers of this project are stand alone servers. You don't need to install Tomcat on your system, 
but if you have, make sure that that version is not running. Start the project's Tomcat servers as explained above.

Another common error is not having the environment properly configured. Make sure to have a JDK installed, and JAVA_HOME configured.

1. Right click "Computer" or "My Computer" in the Start Menu and choose "Properties" from the context menu. 
2. Under the "Advanced" tab, you can define new variables. 
3. Set the JAVA_HOME variable to point to your JDK's main directory (i.e. C:/path/to/jdkx.x, not the bin directory). 
4. Additionally, add %JAVA_HOME%\jre\bin to the PATH variable, which will help prevent possible problems with orphaned DLL files across Windows versions. - [Reference](https://www.mulesoft.com/tcat/tomcat-windows)
