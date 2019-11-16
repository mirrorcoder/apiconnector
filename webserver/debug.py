# -*- coding: utf-8 -*-
import sys
import os

from configs import config

sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), '../'))

from webserver.app import app_factory_tg
from werkzeug.middleware.shared_data import SharedDataMiddleware

def start():
    app = app_factory_tg()
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {})
    app.run(port=8080, debug=True)

