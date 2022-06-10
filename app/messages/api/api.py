from fastapi import APIRouter
from app.api.facade import UserMessage
from app.api.messages import QueuePC
from app.common.schemas import ServiceName
from app.common.hooks import log_hook

messages = APIRouter(
    prefix="/messages_service",
    tags=["messages"]
)

queue = QueuePC().crawl()

@messages.get("/", response_model=UserMessage)
async def send_message():
    response = UserMessage(txt=f"<{queue.get()}>")
    log_hook(f'FROM: {ServiceName.messages}::GET')
    log_hook(response)
    return response