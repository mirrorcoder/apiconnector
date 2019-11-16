import json

from flask import abort, Response
from flask_login import current_user
from functools import wraps

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return Response(json.dumps({"auth": "fail"}), mimetype="application/json", status=401)
        return f(*args, **kwargs)
    return decorated_function

def requires_login_web(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(401)
        return f(*args, **kwargs)
    return decorated_function

