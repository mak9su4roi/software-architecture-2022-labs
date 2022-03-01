from enum import Enum
from pydantic import BaseModel, Field
from ipaddress import IPv4Address
from string import Template
from signal import SIGTERM
from os import kill
from subprocess import Popen
from shlex import split
from .hooks import log_hook


cmd_t = Template('uvicorn app.${name}:app --port ${port} --reload')
info_t = Template(
    '*'*10+'\n'+
    'Service-name: ${name}\n'+
    '\tAction: ${action}\n'+
    '\tStartPort: ${port}\n'+
    '\tPids: ${pids}\n'+
    '*'*10+'\n'
)

class ServiceName(str, Enum):
    facade = "facade"
    logging = "logging"
    messages = "messages"

class ServiceData(BaseModel):
    reddundancy: int = Field(..., ge=1)
    ip: IPv4Address
    port: int = Field(..., ge=8000)

class ActiveService(BaseModel):
    debug: bool
    name: str
    data: ServiceData
    pids: list[int]
    def terminate(self) -> None:
        if self.debug:
            log_hook(info_t.substitute(name=self.name, pids=self.pids, **self.data.dict(),
                action="terminate"
            ))
        [ kill(pid, SIGTERM) for pid in self.pids ]

class Service(BaseModel):
    debug: bool = False
    name: str
    data: ServiceData  
    
    def launch(self) -> ActiveService:
        pids=[
            Popen(split(cmd_t.substitute(name=self.name, port=self.data.port+n))
            ,start_new_session=True).pid
            for n in range(self.data.reddundancy)    
        ]

        if self.debug:
            log_hook(info_t.substitute(name=self.name, pids=pids, **self.data.dict(),
                action="launch"
            ))
        
        return ActiveService(debug=self.debug, name=self.name, data=self.data, pids=pids)


class MicroConfig(BaseModel):
    services: dict[ServiceName, Service]
 