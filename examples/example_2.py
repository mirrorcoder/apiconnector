from pprint import pprint

from scheme.utils import CallRestEndpointSession

HOST = 'http://127.0.0.1:8080'
cres = CallRestEndpointSession()
#Registration
res = cres(HOST+"/api/accounts/reg", {
    'email': 'q@q.com',
    'password': 'q'
}, 'post')
pprint(res.json())
#Authorization
res = cres(HOST+"/api/accounts/login", {
    'email': 'q@q.com',
    'password': 'q'
}, 'post')
pprint(res.json())
#Get Self
res = cres(HOST+"/api/accounts/self", {
    'email': 'q@q.com',
    'password': 'q'
}, 'get')
pprint(res.json())
# Create Schema
# res = cres(HOST+"/api/scheme", {
#     'client_type': 1,
#     'schema': {
#         '__config__': {
#             'type': 1
#         },
#         'get_ip': [{
#             'url': 'https://api.ipify.org',
#             'method': 'GET',
#             'params': {
#                 'format': 'json'
#             },
#             'result': {
#                 'success': {
#                     'is_json': True,
#                     'status': [200],
#                     'check_field': [],
#                     'save_to_vars': {
#                         '__result__': {
#                             'response': {
#                                 'ip': 'ip'
#                             },
#                             'status': 200,
#                         }
#                     }
#                 }
#             }
#         }]
#     }
# }, 'post')
# pprint(res.json())
schema_id = '5dd81c6f1182c868bdeb7ef1'
res = cres(HOST+"/method/scheme/%s/method/get_ip" % schema_id, {    }, 'get')
pprint(res.json())
