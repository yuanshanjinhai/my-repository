# coding=utf-8
import re

s = '{"userid":"【$get_userid】","token":"【$get_token】"}'
sd = eval(s)
print(type(sd))