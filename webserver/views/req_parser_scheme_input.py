from flask_restful import reqparse

req_parser_scheme_input = reqparse.RequestParser()
req_parser_scheme_input.add_argument('client_type', type=int, location='json', required = True)
req_parser_scheme_input.add_argument('schema', type=dict, location='json', required = True)
