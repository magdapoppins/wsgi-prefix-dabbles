from flask import Flask
import os
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# # Setting the prefix this w works
# class PrefixMiddleware(object):

#     def __init__(self, app, prefix=''):
#         self.app = app
#         self.prefix = prefix

#     def __call__(self, environ, start_response):

#         if environ['PATH_INFO'].startswith(self.prefix):
#             environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
#             environ['SCRIPT_NAME'] = self.prefix
#             return self.app(environ, start_response)
#         else:
#             start_response('404', [('Content-Type', 'text/plain')])
#             return ["This url does not belong to the app.".encode()]


os.environ["SCRIPT_NAME"] = "/a/b/c/d/e"
print("Prefix: ", os.environ["SCRIPT_NAME"])

app = Flask(__name__)
# This only works together w werkzeugs wsgi DispatchMiddleware
#app.config['APPLICATION_ROOT'] = "/a/b/c/d/e"


@app.route('/hernekeitto')
def hello_world():
    return 'Hello world'


@app.route('/jello')
def jello_world():
    return 'Jello'


@app.route('/')
def blurb_world():
    return "The URL for this page is"

def simple(env, resp):
    resp(b'200 OK', [(b'Content-Type', b'text/plain')])
    return [b'Hello WSGI World']

#app.wsgi_app = DispatcherMiddleware(simple, {os.environ["SCRIPT_NAME"]: app.wsgi_app})

#app.wsgi_app = PrefixMiddleware(app.wsgi_app, os.environ['SCRIPT_NAME'])

