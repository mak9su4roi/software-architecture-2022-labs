from string import Template
import requests
from .schemas import Service

url_t = Template('http://${ip}:${port}/${path}')   
        
def remote_get(srvs: Service, path: str) -> dict:
    url = url_t.substitute(ip=srvs.data.ip, port=srvs.data.port, path=path)
    return requests.get(url).json()

def remote_post(srvs: Service, path: str, *, payload: dict = {}) -> dict:
    url = url_t.substitute(ip=srvs.data.ip, port=srvs.data.port, path=path)
    return requests.post(url, data=payload).json()
        
