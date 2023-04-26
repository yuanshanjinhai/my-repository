# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
from GeneralTools.md5_encrypt import *
from login.DB.OtherDB import GetUeridByUserLoginName
import json

Blue_login=Blueprint("login",__name__)

class Login(MethodView):
    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form

        user_login_name = data_dict['user_login_name']
        password = data_dict['password']
        if user_login_name == 'admin':
            if password == '123456':
                data1 = {"code": 1, "info": "success","data": {"user_id":1}}
            else:
                data1 = {"code": 0, "info": "用户名或密码错误"}
        if user_login_name != 'admin':
            password = md5_encrypt(password)
            user_id = GetUeridByUserLoginName(user_login_name)
            if user_login_name == password:
                data1 = {"code": 1, "info": "success","data": {"user_id":user_id}}
            else:
                data1 = {"code": 0, "info": "用户名或密码错误"}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_login.add_url_rule("/login/",view_func=Login.as_view("login1"))
