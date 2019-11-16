from mongoengine import *

from storages.extends import AddonFunc, TimeStampMixin, IsDeletedModelMixin


class Scheme(IsDeletedModelMixin, TimeStampMixin, AddonFunc, Document):
    account_id = StringField()
    client_type = IntField()
    schema = DictField()
