# -*- coding: utf-8 -*-
import json

from flask import Blueprint, Response
from flask import request

from scheme.factory_client import FactoryClient
from storages.storage import MongoStorage

call_method_view = Blueprint('call_method_view', __name__, url_prefix = '/')

storage = MongoStorage()

def get_args_by_method():
    if request.method == 'GET':
        return request.args
    elif request.method in ['POST', 'PUT', 'DELETE']:
        form = request.form
        json_data = request.json
        if not form is None:
            return form
        if not json_data is None:
            return json_data
        return {}
    return {}

def create_response_from_dict(result):
    mimetype = result.get('mimetype', None)
    content_type = result.get('content_type', None)
    response = result.get('response', None)
    headers = result.get('headers', None)
    status = result.get('status', None)
    if type(response) is dict:
        response = json.dumps(response)
    return Response(response=response,
                    status=status,
                    mimetype=mimetype,
                    content_type=content_type,
                    headers=headers)

@call_method_view.route("method/scheme/<schema_id>/method/<name_method>",
                        methods=['GET', 'POST', 'PUT', 'DELETE'])
def call_method_view_func(schema_id, name_method):
    schema = storage.scheme.get(db_id=schema_id)
    with FactoryClient(schema) as client1:
        result = client1.call_method(name_method, get_args_by_method())
        result = create_response_from_dict(result)
    return result
