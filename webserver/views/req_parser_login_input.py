from flask_restful import reqparse

req_parser_login_input = reqparse.RequestParser()
req_parser_login_input.add_argument('email', type=str, location='json', required = True)
req_parser_login_input.add_argument('password', type=str, location='json', required = True)
