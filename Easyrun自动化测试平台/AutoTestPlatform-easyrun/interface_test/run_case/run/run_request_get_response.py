# coding = utf-8
import json
import os
import requests
from urllib import parse
from GeneralTools.OtherTools import RemoveSpacesAndEnter
from GeneralTools.OtherTools import encrypt_decrypt
from GeneralTools.AllPath import encrypt_decrypt_load_path0

def run_request_get_response(address, method, header, body):
    if method == "POST":
        # if header != "":
        #     header = json.loads(header)
        #     if body != "":
        #         body = json.loads(body)
        #         print(11111111111111)
        #         try:
        #             actual_respone = requests.post(address, headers=header, data=body)
        #         except:
        #             actual_respone = requests.post(address, headers=header, json=body)
        #     elif body == "":
        #         actual_respone = requests.post(address, headers=header)
        # elif header == "":
        #     if body != "":
        #         body = json.loads(body)
        #         try:
        #             actual_respone = requests.post(address, data=body)
        #         except:
        #             actual_respone = requests.post(address, json=body)
        #     elif body == "":
        #         actual_respone = requests.post(address)
        client = requests.Session()
        client.keep_alive = True
        if header != "":
            client.headers = header
            if body != "":
                print('body=',body,type(body))
                try:
                    actual_respone = client.post(address, headers=header, data=body)
                except:
                    actual_respone = client.post(address, headers=header, json=body)
            elif body == "":
                actual_respone = client.post(address, headers=header)
        elif header == "":
            if body != "":
                print(1111111111111111111111111111111)
                try:
                    actual_respone = client.post(address, data=body)
                except:
                    actual_respone = client.post(address, json=body)
            elif body == "":
                actual_respone = client.post(address)

    elif method == "GET":
        if header != None:
            actual_respone = requests.get(address, headers=header)
        elif header == None:
            actual_respone = requests.get(address)

    return actual_respone

# a = [("0", "无"), ("1", "url编码-url解码"), ("2", "加密-解密"),
    #      ("3", "url编码-加密-解密-url解码"), ("4", "仅url编码"), ("5", "仅url解码")]