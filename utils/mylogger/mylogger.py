import json
import logging
import logging.config
import os

import yaml


def get_dict_from_json_file(config_filename):
    path = config_filename
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        return config
    return {}

def get_dict_from_yaml_file(config_filename):
    path = config_filename
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        return config
    return {}


def get_dict_from_file(config_filename):
    if '.yaml' in config_filename:
        return get_dict_from_yaml_file(config_filename)
    elif '.json' in config_filename:
        return get_dict_from_json_file(config_filename)
    return {}


class MyLogger(object):
    LOG = {}

    def __init__(self):
        self.default_level=logging.INFO
        self.env_key = 'LOG_CFG'
        self.value_env_key = os.getenv(self.env_key, None)
        self.config_dict = {} if not self.value_env_key else self.value_env_key
        self.setup_config()

    def setup_config(self, config_dict=None):
        self.config_dict = config_dict if config_dict else self.config_dict
        if self.config_dict:
            logging.config.dictConfig(self.config_dict)
        else:
            logging.basicConfig(level=self.default_level)
        return self

    def get_instance(self, namespace=None):
        if not MyLogger.LOG.get(namespace, None):
            MyLogger.LOG[namespace] = logging.getLogger(namespace)
        return MyLogger.LOG[namespace]

LOGGER = MyLogger()


