import json
from app.common.schemas import MicroConfig 

with open("app/config/MicroConfig.json", "r", encoding="UTF-8") as file:
    micro_config=MicroConfig(**json.load(file))