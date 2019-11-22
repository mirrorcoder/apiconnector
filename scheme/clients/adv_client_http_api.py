from scheme.clients.abstract_advertiser_adapter import AbstractAdvertiserAdapter
from scheme.utils import CallRestEndpointSession, apply_deep_format


class AdvClientHttpApi(AbstractAdvertiserAdapter):
    def __init__(self, schema):
        self.reqmethod = CallRestEndpointSession()
        self.schema = schema
        self.ns = {}

    def return_build_func(self, schema_endpoint, vars):
        headers = schema_endpoint.get('headers', None)
        url = schema_endpoint.get('url', '').format(**vars)
        method = schema_endpoint.get('method', '').lower()
        vars.update(self.ns)
        params = apply_deep_format(schema_endpoint.get('params', {}), vars)
        data__ = apply_deep_format(schema_endpoint.get('data', {}), vars)
        success_is_json = schema_endpoint.get('result', {}).get('success', {}).get('is_json', False)
        success_statuses = schema_endpoint.get('result', {}).get('success', {}).get('status', [200, 204])
        success_check_field = schema_endpoint.get('result', {}).get('success', {}).get('check_field', None)
        save_to_vars = schema_endpoint.get('result', {}).get('success', {}).get('save_to_vars', {})

        def get_field(d, field):
            i = d
            for f in field.split("."):
                if type(i) == dict:
                    if f == '$':
                        i = d
                    i = i.get(f, {})
                elif type(i) in [tuple, list]:
                    if f == '$':
                        i = d
                        continue
                    try:
                        index = int(f)
                    except ValueError:
                        return ''
                    if index < len(i):
                        i = i[index]
                    else:
                        return ''
            return i

        def check_status_code(res):
            if not res.status_code in success_statuses:
                return False
            return True

        def check_is_json(res):
            try:
                json_response = res.json()
            except ValueError:
                if success_is_json:
                    return False
            return True

        def check_check_field(res):
            json_response = res.json()
            if success_check_field:
                result_field = get_field(json_response, success_check_field[0])
                if not result_field in success_check_field[1]:
                    return False
            return True

        def save_vars_recursive(res, ns, save_to_vars):
            for dst, src in save_to_vars.items():
                if type(src) in [str]:
                    ns[dst] = get_field(res, src)
                elif type(src) in [dict]:
                    if not dst in ns:
                        ns[dst] = {}
                    save_vars_recursive(res, ns[dst], src)


        def save_vars(res):
            json_response = res.json()
            save_vars_recursive(json_response, self.ns, save_to_vars)

        # def save_vars(res):
        #     json_response = res.json()
        #     for dst, src in save_to_vars.items():
        #         self.ns[dst] = get_field(json_response, src)

        def call_reqmethod():
            res = self.reqmethod(url, params if params else None, method, headers=headers, data=data__ if data__ else None)
            result = check_status_code(res)\
                     and check_is_json(res)\
                     and check_check_field(res)
            if result:
                save_vars(res)
            return result
        return call_reqmethod

    def build_and_execute_schema(self, schema, vars):
        if not schema:
            return None
        for s in schema:
            is_success_result = self.return_build_func(s, vars)()
            if not is_success_result:
                return False
        return True

    def get_value_var(self, name_value):
        return self.ns.get(name_value, {})

    def call_method(self, name_method, vars):
        result = self.build_and_execute_schema(self.schema.get(name_method, []), vars)
        return self.get_value_var('__result__')


#TODO: Add map-filter
#TODO: Add processing callback-answers