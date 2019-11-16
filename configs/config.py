# -*- coding: utf-8 -*-
from .config_mongo import *
import os.path as p
PROD = True

IMAGES_PATH = p.join(p.dirname(p.abspath(__file__)), 'static', 'images')
PROD_PATH = '/control_prod/'
SWITCH_BILLING = False
REST_IS_COOKIES_AUTH = True
if PROD:
    TIMEZONE = +4
    SECRET_KEY = 'A0Zr98˙™£ª¶3yX R~XHH!jmMPC.s39 LWfk wN]LWX/,?RT'
else:
    TIMEZONE = +4
    SECRET_KEY  = 'A0Zr98˙™£ª¶3yX R~XHH!jmMPC.s39 LWfk wN]LWX/,?RT'
