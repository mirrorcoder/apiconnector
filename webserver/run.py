# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), '../'))

from .app import app_factory_tg

app = app_factory_tg()

application = app
