# -*- coding: utf-8 -*-
from configs import config
from webserver.create_app import create_app
from webserver.extensions import mongoengine, login_manager
from webserver.views.call_method_view import call_method_view
from webserver.views.api_login import api_login
from webserver.views.api_scheme import api_scheme

views = [
    call_method_view,
    api_login,
    api_scheme
]
extensions = [
    mongoengine,
    login_manager
]

def app_factory_tg(extensions=extensions,
                   views=views,
                   config=config):
    app = create_app(extensions=extensions,
                     modules=views,
                     config=config)
    return app
