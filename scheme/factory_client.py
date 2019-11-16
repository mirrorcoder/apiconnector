from scheme.clients.adv_client_http_api import AdvClientHttpApi
from scheme.constants import TYPE_CLIENT_HTTP_API


class FactoryClient(object):

    def __init__(self, scheme=None):
        self.scheme = scheme

    def build(self, schema=None):
        s = schema if schema else self.scheme
        if not s:
            return None
        if s.get('__config__', {}).get('type', None) == TYPE_CLIENT_HTTP_API:
            return AdvClientHttpApi(s)
        return None

    def __enter__(self):
        return self.build()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

