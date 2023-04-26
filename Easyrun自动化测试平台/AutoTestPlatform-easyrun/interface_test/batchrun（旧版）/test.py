# coding=utf-8
import re
from GeneralTools.OtherTools import *
from GeneralTools.ExcelAllSheet import *
from GeneralTools.AllPath import *
import json

s0='{"a":1}'
print(type(s0))
s=json.loads(s0)
print(s,type(s))