import requests

def call_rest_endpoint(url, params, method, call_func=requests, data=None, files=None, headers=None):
    params = params if type(params) is dict else {}
    result = None
    if method == 'get':
        result = call_func.get(url,
                               params=params,
                               headers=headers)
    elif method == 'post':
        result = call_func.post(url,
                                data=data,
                                files=files,
                                json=params,
                                headers=headers)
    elif method == 'put':
        result = call_func.put(url,
                               data=data,
                               files=files,
                               json=params,
                               headers=headers)
    elif method == 'delete':
        result = call_func.delete(url,
                                  json=params,
                                  headers=headers,
                                  data=data)
    return result


class CallRestEndpointSession(object):
    def __init__(self):
        self.session = requests.Session()

    def __call__(self, url, params, method, files=None, data=None, headers=None):
        return call_rest_endpoint(url, params, method, call_func=self.session, files=files, data=data, headers=headers)


def apply_deep_format(v, vars):
    if type(v) in [str]:
        return v.format(**vars)
    elif type(v) in [int, float]:
        return v
    elif type(v) in [list, tuple]:
        new_list = []
        for i in v:
            new_list.append(apply_deep_format(i, vars))
        return new_list
    elif type(v) in [dict]:
        new_dict = {}
        for k, val in v.items():
            new_dict[k] = apply_deep_format(val, vars)
        return new_dict
    return v
