from bson import ObjectId

from accounts import models


class AccountStorage(object):
    def create(self, email, password):
        args = {
            'email': email,
            'password': password
        }
        account = models.Account(**args)
        account.save()
        return str(account.id)

    def get(self, db_id=None, email=None, password=None, dict_convert=True):
        args = {
            'is_deleted': False
        }
        if db_id is not None:
            args['id'] = ObjectId(db_id)
        if email is not None:
            args['email'] = email
        if password is not None:
            args['password'] = password
        objs = models.Account.objects(**args)
        if dict_convert:
            return [obj.to_dict() for obj in objs]
        return [obj for obj in objs]

    def get_one(self, *args, **kwargs):
        res = self.get(*args, **kwargs)
        if res:
            return res[0]
        return None

    def update(self, db_id, email=None, password=None):
        args = {
            'is_deleted': False,
            'id': ObjectId(db_id)
        }
        obj = models.Account.objects(**args)
        if not obj:
            return False
        if email is not None:
            obj.update(set__email=email)
        if password is not None:
            obj.update(set__password=password)
        return True
