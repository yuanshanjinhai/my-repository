# coding=utf-8
import re
import json
import requests

def update_issue_test_summary_field():
    url = "http://public-sentiment.dev.ennewi.cn/nms/keyword/type/save"

    headers = {
        "ticket": "t214042839e3f47b3967cb684845974be",
        "Accept": "application/json",
    }
    client = requests.Session()
    client.keep_alive = True
    client.headers = headers

    data = json.dumps('{ "orgId": "10000001", "orgName": "新奥新智", "typeId": null, "typeName": "投诉类27"}')

    res1 = client.post(url, data=data)
    print("res1=",res1,res1.json())
    print(json.dumps(res1.json(), sort_keys=True, indent=4, separators=(",", ": "), ensure_ascii=False))
update_issue_test_summary_field()