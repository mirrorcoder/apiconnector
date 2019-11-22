# -*- coding: utf-8 -*-
import json

from flask import Blueprint, Response
from flask import request
from flask_login import current_user
from storages.storage import MongoStorage
from webserver.constants.constants import STATUS_OK
from webserver.utils.decorators import requires_login
from webserver.views.req_parser_scheme_input import req_parser_scheme_input

storage = MongoStorage()
api_scheme = Blueprint('scheme', __name__, url_prefix = '/api/scheme')

MAX_COUNT_SCHEME_GET = 10

SCHEMA_SUCCESSFUL_STATUS = 1
SCHEMA_NOT_FOUND_STATUS = -1

@api_scheme.route("", methods=['POST'])
@requires_login
def create_schema():
    data = req_parser_scheme_input.parse_args()
    schema_id = storage.scheme.create(str(current_user.id),
                                      data.get('client_type', None),
                                      data.get('schema', {}))
    return Response(json.dumps({
        'status': STATUS_OK,
        'code': SCHEMA_SUCCESSFUL_STATUS,
        'schema_id': schema_id
    }), status=200)

@api_scheme.route("", methods=['GET'])
@requires_login
def get_scheme():
    count = min(request.args.get('count', MAX_COUNT_SCHEME_GET), MAX_COUNT_SCHEME_GET)
    offset = request.args.get('offset', 0)
    total = storage.scheme.get_count(account_id=str(current_user.id))
    scheme = storage.scheme.get(account_id=str(current_user.id), offset=offset, count=count)
    return Response(json.dumps({
        'status': STATUS_OK,
        'scheme': scheme,
        'pages': {
            'count': count,
            'offset': offset,
            'total': total
        }
    }), status=200)

@api_scheme.route("/<schema_id>", methods=['GET'])
@requires_login
def get_schema(schema_id):
    schema = storage.scheme.get_one(account_id=str(current_user.id), db_id=schema_id)
    return Response(json.dumps({
        'status': STATUS_OK,
        'schema': schema
    }), status=200)

@api_scheme.route("/<schema_id>", methods=['PUT'])
@requires_login
def update_schema(schema_id):
    schema = storage.scheme.get_one(account_id=str(current_user.id), db_id=schema_id)
    if not schema:
        return Response(json.dumps({
            'status': STATUS_OK,
            'code': SCHEMA_NOT_FOUND_STATUS
        }), status=404)
    schema_body = request.json.get('schema', {})
    storage.scheme.update(schema_id, schema_body)
    return Response(json.dumps({
        'status': STATUS_OK,
        'code': SCHEMA_SUCCESSFUL_STATUS
    }), status=200)

@api_scheme.route("/<schema_id>", methods=['DELETE'])
@requires_login
def delete_schema(schema_id):
    schema = storage.scheme.get_one(account_id=str(current_user.id), db_id=schema_id)
    if not schema:
        return Response(json.dumps({
            'status': STATUS_OK,
            'code': SCHEMA_NOT_FOUND_STATUS
        }), status=404)
    storage.scheme.delete(schema_id)
    return Response(json.dumps({
        'status': STATUS_OK,
        'code': SCHEMA_SUCCESSFUL_STATUS
    }), status=200)

