from scheme.constants import TYPE_CLIENT_HTTP_API
from scheme.factory_client import FactoryClient

SCHEMA1 = {
    '__config__': {
        'type': TYPE_CLIENT_HTTP_API
    },
    'get_ip': [{
        'url': 'https://api.ipify.org',
        'method': 'GET',
        'params': {
            'format': 'json'
        },
        'result': {
            'success': {
                'is_json': True,
                'status': [200],
                'check_field': [],
                'save_to_vars': {
                    '__result__': {
                        'ip': 'ip'
                    }
                }
            }
        }
    }]
}

client = FactoryClient().build(SCHEMA1)
print(client.call_method('get_ip', {}))
print(client.get_value_var('ip'))

with FactoryClient(SCHEMA1) as client1:
    print(client1.call_method('get_ip', {}))
    print(client1.get_value_var('ip'))

