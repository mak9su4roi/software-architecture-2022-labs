from operator import concat
from pydantic import BaseModel
from app.common.hooks import log_hook
from uuid import UUID

class UserLog(BaseModel):
    txt: str
    id: UUID

class LogDump(BaseModel):
    dump: str

class HashTable():
    table: dict
    def __init__(self):
        self.table = {}
    
    def dump(self) -> LogDump:
        dump = LogDump(dump=f'[{", ".join(self.table.values())}]')
        log_hook(dump)
        return dump

    def put(self, msg: UserLog) -> UserLog:
        log_hook(msg)
        self.table[msg.id] = msg.txt
        return msg