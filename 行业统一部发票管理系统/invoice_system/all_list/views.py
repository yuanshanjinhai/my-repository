# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
import json
from all_list.DB import GetUserList,GetInvoicetypeList

Blue_alllist = Blueprint("alllist",__name__)

class UserList(MethodView):
    def get(self):
        user_list = GetUserList()
        data1 = {"code": 1, "info": "success", "data": user_list}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_alllist.add_url_rule("/user_list/",view_func=UserList.as_view("alllist1"))
# http://127.0.0.1:5002/invoice/user_list/

class Invoicetype_list(MethodView):
    def get(self):
        invoicetype_list = GetInvoicetypeList()
        data1 = {"code": 1, "info": "success", "data": invoicetype_list}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_alllist.add_url_rule("/invoicetype_list/",view_func=Invoicetype_list.as_view("alllist2"))
# http://127.0.0.1:5002/invoice/invoicetype_list/