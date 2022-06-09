from fastapi import APIRouter
from app.api.facade import UserMessage
from app.common.schemas import ServiceName
from app.common.hooks import log_hook

messages = APIRouter(
    prefix="/messages_service",
    tags=["messages"]
)

@messages.get("/", response_model=UserMessage)
async def send_message():
    response = UserMessage(txt="Not implemented, yet...")
    log_hook(f'FROM: {ServiceName.messages}::GET')
    log_hook(response)
    return {
        "txt": "Not implemented" 
    }