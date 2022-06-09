from fastapi import APIRouter
from app.api.logging import UserLog, HashTable, LogDump
from app.common.hooks import log_hook
from app.common.schemas import ServiceName

logging = APIRouter(
    prefix="/logging_service",
    tags=["logging"]
)

log = HashTable()

@logging.get("/", response_model=LogDump)
async def get_log():
    log_hook(f'FROM: {ServiceName.logging}::GET')
    return log.dump()

@logging.post("/", response_model=UserLog)
def put_log(payload: UserLog):
    log_hook(f'FROM: {ServiceName.logging}::POST')
    return log.put(payload)