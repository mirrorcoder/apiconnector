from mongoengine import Document, StringField, IntField, BooleanField

from storages.extends import IsDeletedModelMixin, TimeStampMixin, AddonFunc


class Account(IsDeletedModelMixin, TimeStampMixin, AddonFunc, Document):
    email = StringField()
    password = StringField()
    is_active = BooleanField(default=True)
    is_authenticated = BooleanField(default=True)

    def get_id(self):
        return str(self.id)
