from os.path import dirname
import fnmatch
import os
import importlib

from urls.example import routes as example_urls
from urls.docs import routes as docs_urls
from apistar.frameworks.wsgi import WSGIApp as App
from apistar import Include


routes = [Include('/example', example_urls),
          Include('', docs_urls),]
        
app = App(routes=routes)
