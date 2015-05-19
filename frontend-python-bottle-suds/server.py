from bottle import *
from bpelclient import BPEL
import os

@get('/')
def index():
    return template('index.tpl')



def get_error(e):
    try:
        return e.args[0]
    except:
        return "Unknown error"

@post('/result')
def process():
    try:
        #Retrieve the form data
        cc_number = request.forms.get('cc_number')
        if not cc_number :
            fail("Please fill in the form.")

        #Do the service call
        srv = BPEL()
        res = srv.process(cc_number)

        return template('result.tpl', cc_number=cc_number, res=res)
    except Exception as e:
        return template('index.tpl', error=get_error(e))

    #redirect('/') ##All fine


def fail(msg):
    raise Exception(msg)

@get('/validator/<cc_number>')
def get_type(cc_number):
    if not cc_number:
        abort(404, "Missing credit card number" )

    srv = BPEL()
    res = srv.process(cc_number)
    return {'type': res}


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')

if __name__ == '__main__':
    run(debug=True, host='localhost', port=8888)


    
