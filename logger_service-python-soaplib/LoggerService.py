# Log Service
# Operations:
# -  Add log
# Author: Ivan Rodriguez Asqui

from soaplib.core import Application
from soaplib.core.server import wsgi
from soaplib.core.service import soap
from soaplib.core.service import DefinitionBase
from soaplib.core.model.primitive import String, Integer, Float
from soaplib.core.model.clazz import ClassModel, Array

from LogDb import LogDb


db = LogDb() #Interface to our sqlite database

# class Book(ClassModel):
#     """A book object to represent book rows in the database.
#        Boooks are easier to represent as a complex type, so we use this
#        helper class to hold our book properties, which match to the database table
#        Reference:
#        http://soaplib.github.io/soaplib/2_0/pages/usermanager.html"""
#
#     Id = Integer
#     title = String
#     author = String
#     year = Integer
#     price = Float

class LogService(DefinitionBase):
    """This is the main service class."""

    @soap(String,String,_returns=Integer)
    def add_log(self, cc_number, cc_type):
        """Adds a book to the database"""
        global db
        return db.add_log(cc_number, cc_type)



    @soap()
    def clear_logs(self):
        """Clears the database"""
        global db
        db.clear_logs()

if __name__=='__main__':
    from wsgiref.simple_server import make_server
    soap_app = Application([LogService], 'logger.itec833.ws')
    wsgi_app = wsgi.Application(soap_app)

    server = make_server('localhost', 7789, wsgi_app)
    server.serve_forever()
