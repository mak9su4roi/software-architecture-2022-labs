from pydantic import BaseModel

class UserMessage(BaseModel):
    txt: str