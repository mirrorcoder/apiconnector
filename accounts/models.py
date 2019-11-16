from mongoengine import Document, StringField, IntField, BooleanField

from storages.models import IsDeletedModelMixin, TimeStampMixin, AddonFunc


class Account(IsDeletedModelMixin, TimeStampMixin, AddonFunc, Document):
    email = StringField()
    password = StringField()
