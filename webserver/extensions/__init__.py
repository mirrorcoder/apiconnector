# -*- coding: utf-8 -*-
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from storages.storage import MongoStorage

storage = MongoStorage()
mongoengine = MongoEngine()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    account = storage.account.get_one(db_id=user_id, dict_convert=False)
    return account

__all__ = ['mongoengine', 'login_manager']
