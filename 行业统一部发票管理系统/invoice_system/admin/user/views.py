# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
import json
from GeneralTools.md5_encrypt import *
from admin.user.DB import GetUserloginnameList,GetUserList,InsertUser
from admin.department.DB import GetDepartmentIdByDepartmentName
from GeneralDB.OtherDB import GetCompanyIdByCompanytName

Blue_user = Blueprint("user",__name__)

class User(MethodView):
    def get(self):
        user_list = GetUserList()
        data0 = user_list
        data1 = {"code": 1, "info": "success", "data": data0}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        print('data_dict=',data_dict)
        user_login_name = data_dict['user_login_name']
        user_name = data_dict['user_name']
        password = data_dict['password']
        company_name = data_dict['company_name']
        department_name = data_dict['department_name']
        if GetUserloginnameList(user_login_name) == 0:
            data1 = {"code": 0, "info": "用户登录名重复"}
            data = json.dumps(data1, ensure_ascii=False)
            return data
        if len(password) < 6:
            data1 = {"code": 0, "info": "密码位数不能小于6位"}
            data = json.dumps(data1, ensure_ascii=False)
            return data
        if company_name == None or department_name == None:
            data1 = {"code": 0, "info": "所属公司或所在部门为空"}
            data = json.dumps(data1, ensure_ascii=False)
            return data
        password = md5_encrypt(password)
        company_id = GetCompanyIdByCompanytName(company_name)
        department_id = GetDepartmentIdByDepartmentName(department_name)
        print('company_id=',company_id,type(company_id))
        print('department_id=',department_id,type(department_id))
        InsertUser(user_login_name, user_name, password,company_id,department_id)
        data0 = {"user_login_name":user_login_name,"user_name":user_name}
        data1 = {"code": 1, "info": "success","data":data0}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_user.add_url_rule("/user/",view_func=User.as_view("user1"))
# http://127.0.0.1:5002/invoice/user/
# post: {"user_login_name":"guolin","user_name":"郭霖","password":"123456","company_name":'腾讯',"department_name":"测开部}