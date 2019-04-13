import util
from formatter.uuid import Uuid

class UuidShort(Uuid):
    def format(self, uuid, task):
        return util.uuid_short(uuid)
