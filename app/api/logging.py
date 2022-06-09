from pydantic import BaseModel
from app.common.hooks import log_hook
from uuid import UUID



class UserLog(BaseModel):
    txt: str
    id: UUID

class LogDump(BaseModel):
    dump: str

class HashTable():
    def __init__(self):
        from hazelcast.proxy.map import Map
        import hazelcast

        self.table = hazelcast.HazelcastClient(
            cluster_name="dev",
            cluster_members=["localhost:5701"]
        ).get_map("map").blocking()
    
    def dump(self) -> LogDump:
        dump = LogDump(dump=f'[{", ".join(self.table.values())}]')
        log_hook(dump)
        return dump

    def put(self, msg: UserLog) -> UserLog:
        log_hook(msg)
        self.table.put(msg.id, msg.txt)
        return msg