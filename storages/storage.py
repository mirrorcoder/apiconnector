from accounts.storage import AccountStorage
from scheme.storage.storage import SchemeStorage


class MongoStorage(object):
    def __init__(self):
        self.scheme = SchemeStorage()
        self.account = AccountStorage()
