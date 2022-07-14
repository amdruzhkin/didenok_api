import re
from datetime import datetime

class Validator:
    @staticmethod
    def check_uuid(uuid):
        uuid_mask = "^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$"
        if type(uuid) != str:
            raise Exception("UUID Is Not A String")

        if len(uuid) == 0:
            raise Exception("UUID Is Empty")

        if not re.match(uuid_mask, uuid):
            raise Exception("Invalid UUID Format")

    @staticmethod
    def check_date(date):
        mask = '%Y-%m-%dT%H:%M:%S.%f%z'
        try:
            datetime.strptime(date, mask)
        except BaseException:
            raise Exception("Invalid Date Format")
