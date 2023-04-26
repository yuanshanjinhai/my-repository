# coding=utf-8
import time
import re
import os

s='{"code": "00", "data": [{"update_time": "null", "title": "python", "content": "python port test", "articleId": 1, "owner": 2, "posted_on": "【时间3】"}]}'
d=eval(s)
print(type(d))
if "'" in s:
    print(1)