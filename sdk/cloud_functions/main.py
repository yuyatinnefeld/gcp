from flask import escape
import base64
import mock



def hello_get(request):
    return 'Hello World!'

def hello_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))




if __name__ == "__main__":

    print("run main.py")
