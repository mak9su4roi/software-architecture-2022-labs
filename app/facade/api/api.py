from uuid import uuid4
from app.common.hooks import log_hook
from app.common.schemas import ServiceName
from app.common.messaging import remote_post, remote_get
from app.api.facade import UserMessage
from app.api.logging import UserLog, LogDump
from app.api.messages import QueuePC
from fastapi import APIRouter
from os import environ

queue = QueuePC()

facade = APIRouter(
    prefix="/facade_service",
    tags=["facade"]
)

@facade.get("/", response_model=LogDump)
def make_dump():
    dump = LogDump(dump = " : ".join([
        remote_get(environ["logging_name"], environ["logging_port"], "logging_service/")["dump"],
        remote_get(environ["messages_name"], environ["messages_port"], "messages_service/")["txt"]
    ]))
    log_hook(f'FROM: {ServiceName.facade}::GET')
    log_hook(dump)
    return dump

@facade.post("/", response_model=UserLog)
def save_message(payload: UserMessage):
    log = UserLog(txt=payload.txt, id=uuid4().hex)
    rsp = remote_post(environ["logging_name"], environ["logging_port"], "logging_service/"
            ,payload=log.json()
    )
    queue.put(payload.txt)
    log_hook(f'FROM: {ServiceName.facade}::POST::{payload}')
    log_hook(rsp)
    return rsp