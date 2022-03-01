from uuid import uuid4
from app.common.hooks import log_hook
from app.config import micro_config
from app.common.schemas import ServiceName
from app.common.messaging import remote_post, remote_get
from .schemas import UserMessage
from app.logging_service.api.schemas import UserLog, LogDump
from fastapi import APIRouter

facade = APIRouter(
    prefix="/facade_service",
    tags=["facade"]
)

@facade.get("/", response_model=LogDump)
def make_dump():
    dump = LogDump(dump = " : ".join([
        remote_get(micro_config.services[ServiceName.logging], "logging_service/")["dump"],
        remote_get(micro_config.services[ServiceName.messages], "messages_service/")["txt"]
    ]))
    log_hook(f'FROM: {ServiceName.facade}::GET')
    log_hook(dump)
    return dump

@facade.post("/", response_model=UserLog)
def save_message(payload: UserMessage, ):
    log = UserLog(txt=payload.txt, id=uuid4().hex)
    rsp = remote_post(micro_config.services[ServiceName.logging], "logging_service/"
            ,payload=log.json()
    )
    log_hook(f'FROM: {ServiceName.facade}::POST')
    log_hook(rsp)
    return rsp