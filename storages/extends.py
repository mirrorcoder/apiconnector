import json
from datetime import datetime
import time

from mongoengine import DateTimeField, BooleanField, IntField


class AddonFunc(object):
    @classmethod
    def get_name_fields(cls):
        EXCLUDES = ['amount']
        model_fields = cls._fields
        return [k for k in model_fields.keys() if k not in EXCLUDES]

    def convert_dt_to_str(self, dt):
        PATTERN = '%Y.%m.%dT%H:%M:%S.%fZ%z'
        return dt.strftime(PATTERN)

    def convert_dt_to_stamp(self, dt):
        return time.mktime(dt.timetuple())

    def to_dict(self):
        _id = str(self.id)
        d = json.loads(self.to_json())
        d['id'] = _id
        d['created_at'] = self.convert_dt_to_str(getattr(self, 'created_at'))
        d['updated_at'] = self.convert_dt_to_str(getattr(self, 'updated_at'))
        if 'expired_date' in d:
            d['expired_date'] = self.convert_dt_to_str(getattr(self, 'expired_date'))
        d['created_at_timestamp'] = self.convert_dt_to_stamp(getattr(self, 'created_at'))
        d['updated_at_timestamp'] = self.convert_dt_to_stamp(getattr(self, 'updated_at'))
        if 'expired_date' in d:
            d['expired_date_timestamp'] = self.convert_dt_to_stamp(getattr(self, 'expired_date'))
        d['created_at_timetuple'] = time.mktime(getattr(self, 'created_at').timetuple())
        return d


class TimeStampMixin(object):
    created_at_timestamp = IntField(default=0)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def __init__(self, **values):
        super(TimeStampMixin, self).__init__(**values)

    def save(self, *args, **kwargs):
        self.created_at_timestamp = int(time.time())
        self.updated_at = datetime.utcnow()
        super(TimeStampMixin, self).save(*args, **kwargs)

    def update(self, **values):
        super(TimeStampMixin, self).update(set__updated_at=datetime.utcnow(), **values)


class IsDeletedModelMixin(object):
    is_deleted = BooleanField(default=False)

    def __init__(self, **values):
        super(IsDeletedModelMixin, self).__init__(**values)

    def save(self, *args, **kwargs):
        self.is_deleted = False
        super(IsDeletedModelMixin, self).save(*args, **kwargs)

    # def mixin_query(self, query):
    #     query_add = {
    #         'is_deleted': False
    #     }
    #     query.update(query_add)
    #     return query