from bson import ObjectId

from .models.models import Scheme


class SchemeStorage(object):
    def create(self, account_id, client_type, schema):
        schema_obj = Scheme(account_id=account_id,
                            client_type=client_type, schema=schema)
        schema_obj.save()
        return str(schema_obj.id)

    def get_one(self, *args, **kwargs):
        res = self.get(*args, **kwargs)
        if res:
            return res[0]
        return None

    def get_count(self, account_id=None, client_type=None):
        args = {
            'is_deleted': False
        }
        if account_id is not None:
            args['account_id'] = account_id
        if client_type is not None:
            args['client_type'] = client_type
        scheme = Scheme.objects(**args)
        return scheme.count()

    def get(self, db_id=None, account_id=None, client_type=None, offset=None, count=None):
        args = {
            'is_deleted': False
        }
        if db_id is not None:
            args['id'] = ObjectId(db_id)
        if account_id is not None:
            args['account_id'] = account_id
        if client_type is not None:
            args['client_type'] = client_type
        if offset is not None:
            args['offset'] = offset
        if count is not None:
            args['count'] = count
        scheme = Scheme.objects(**args)
        return [schema.to_dict() for schema in scheme]

    def delete(self, db_id):
        args = {
            'is_deleted': False,
            'id': ObjectId(db_id)
        }
        schema = Scheme.objects(**args)
        if not schema:
            return False
        schema.update(set__is_deleted=True)
        return True

    def update(self, db_id, schema=None):
        args = {
            'is_deleted': False,
            'id': ObjectId(db_id)
        }
        schema_obj = Scheme.objects(**args)
        if not schema_obj:
            return False
        if schema is not None:
            schema_obj.update(set__schema=schema)
        return True

