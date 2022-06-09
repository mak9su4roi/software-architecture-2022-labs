from string import Template
import requests

url_t = Template('http://${dn}:${port}/${uri}')   
        
def remote_get(dn: str, port: str, uri: str) -> dict:
    url = url_t.substitute(dn=dn, port=port, uri=uri)
    return requests.get(url).json()

def remote_post(dn: str, port: str, uri: str, *, payload: dict = {}) -> dict:
    url = url_t.substitute(dn=dn, port=port, uri=uri)
    return requests.post(url, data=payload).json()
        
