# -*- coding: utf-8 -*-
from flask import Flask
from configs import config_logs

from utils.mylogger.mylogger import get_dict_from_file, LOGGER

def create_app(extensions = None,
               modules=None,
               config=None,
               converters=None):
    app = Flask(__name__)

    if converters:
        for key in converters.keys():
            app.url_map.converters[key] = converters[key]

    configure_app(app, config)
    configure_extensions(app, extensions)
    configure_modules(app, modules)
    configure_logging(app)

    return app

def configure_app(app, config):
    if config is not None:
        app.config.from_object(config)


def configure_modules(app, modules):
    for module in modules:
        app.register_blueprint(module)

def configure_extensions(app, exts):
    for ext in exts:
        ext.init_app(app)


def configure_logging(app):
    LOGGER.setup_config(
        get_dict_from_file(
            config_logs.LOG_CONFIG_CALLBACKS_SERVER_PATH
        )
    )
