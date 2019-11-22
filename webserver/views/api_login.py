# -*- coding: utf-8 -*-
import json

from flask import Blueprint, Response
from flask_login import login_user, current_user
from storages.storage import MongoStorage
from webserver.constants.constants import STATUS_OK
from webserver.utils.decorators import requires_login
from webserver.views.req_parser_login_input import req_parser_login_input

storage = MongoStorage()
api_login = Blueprint('accounts', __name__, url_prefix = '/api/accounts')

ACCOUNT_CREATED_STATUS = 1
ACCOUNT_EXIST_STATUS = -1
ACCOUNT_NOT_EXIST = -2
ACCOUNT_AUTH = 2

@api_login.route("/reg", methods=['POST'])
def reg_accounts():
    data = req_parser_login_input.parse_args()
    email = data.get('email')
    password = data.get('password')
    account = storage.account.get_one(email=email)
    if account:
        return Response(json.dumps({
            'status': STATUS_OK,
            'code': ACCOUNT_EXIST_STATUS
        }), status=200)
    acc_id = storage.account.create(email, password)

    return Response(json.dumps({
        'status': STATUS_OK,
        'code': ACCOUNT_CREATED_STATUS,
        'account_id': acc_id
    }), status=200)

@api_login.route("/login", methods=['GET', 'POST'])
def login_accounts():
    data = req_parser_login_input.parse_args()
    email = data.get('email')
    password = data.get('password')
    account = storage.account.get_one(email=email, password=password, dict_convert=False)
    if not account:
        return Response(json.dumps({
            'status': STATUS_OK,
            'code': ACCOUNT_NOT_EXIST
        }), status=401)

    login_user(account)

    return Response(json.dumps({
        'status': STATUS_OK,
        'code': ACCOUNT_AUTH,
        'account': account.to_dict()
    }), status=200)

@api_login.route("/self", methods=['GET'])
@requires_login
def self_accounts():
    user = storage.account.get_one(db_id=str(current_user.id))
    return Response(json.dumps({
        'status': STATUS_OK,
        'user': user
    }), status=200)
