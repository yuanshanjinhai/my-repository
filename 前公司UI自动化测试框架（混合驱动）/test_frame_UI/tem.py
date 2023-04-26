# coding=utf-8
import json

d='{"name": "【BeJson","url": "http://www.bejson.com","page": 88,"isNonProfit": true,"address": {"street": "【科技园路.","city": "江苏苏州","country": "中国"},"links": [{"name": "【Google","url": "http://www.google.com"},{"name": "Baidu","url": "http://www.baidu.com"},{"name": "SoSo","url": "http://www.SoSo.com"}]}'

d_dict = json.loads(d)

def FindDictValue(d_dict,a):
    for k,v in d_dict.items():
        if type(v) == dict:
            FindDictValue(v,a)
        elif type(v) == list:
            for iv in v:
                if type(iv) == dict:
                    FindDictValue(iv,a)
        elif type(v) != dict and type(v) != list:
            if "【" in str(v) and "+" not in str(v):
                d_dict[k] = a
    return d_dict

print(FindDictValue(d_dict,"AAAAA"))