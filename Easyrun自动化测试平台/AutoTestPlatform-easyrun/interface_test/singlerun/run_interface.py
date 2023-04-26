# coding=utf-8
import requests
from GeneralTools.OtherTools import RemoveSpacesAndEnter
import json

def run_interface_get(address,header):
    if header != "":
        header = json.loads(header)
        actual_respone = requests.get(address, headers=header)
    elif header == "":
        actual_respone = requests.get(address)
    if actual_respone.status_code != 200:
        return actual_respone.status_code
    else:
        return actual_respone.text

def run_interface_post(address,header,body):
    if header != "":
        header = RemoveSpacesAndEnter(header)
        header = eval(header)
    # if body != "":
    #     body = json.loads(body) # 先转成字典
    #     body = json.dumps(body) # 再转成json

    client = requests.Session()
    client.keep_alive = True
    if header != "":
        client.headers = header
        if body != "":
            try:
                actual_respone = client.post(address, headers=header, data=body)
            except:
                actual_respone = client.post(address, headers=header, json=body)
        elif body == "":
            actual_respone = client.post(address, headers=header)
    elif header == "":
        if body != "":
            try:
                actual_respone = client.post(address, data=body)
            except:
                actual_respone = client.post(address, json=body)
        elif body == "":
            actual_respone = client.post(address)

    if actual_respone.status_code != 200:
        return str(actual_respone.text)
    elif actual_respone.status_code == 200:
        actual_respone = json.dumps(actual_respone.json(), sort_keys=True, indent=4, separators=(",", ": "), ensure_ascii=False)
        return str(actual_respone)

if __name__ == '__main__':
    body = '{"userid":2420,"token":"ddd3494c940a64654b924dd296261394", "title":"我的标题3","content":"我的内容3"}'
    # body = json.dumps(body)
    print("bodytype=",type(body))
    print( run_interface_post("http://39.100.104.214:8080/create/","",body) )