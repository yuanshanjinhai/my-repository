# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
import json
from admin.invoicetype.DB import GetInvoicetype,GetInvoicetypeByInvoicetypeName,InsertInvoicetype,\
    GetInvoicetypeByInvoicetypeId,UpdateInvoicetype

Blue_invoicetype = Blueprint("invoicetype",__name__)

class Invoicetype(MethodView):
    def get(self):
        invoicetype_name = request.args.get('invoicetype_name')
        if invoicetype_name == None:
            invoicetype_list = GetInvoicetype()
        else:
            invoicetype_list = GetInvoicetypeByInvoicetypeName(invoicetype_name)
        data1 = {"code": 1, "info": "success", "data": invoicetype_list}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        if 'invoicetype_name' not in data_dict:
            data1 = {"code": 0, "info": "发票类型名称不能为空"}
        else:
            invoicetype_name = data_dict['invoicetype_name']
            InsertInvoicetype(invoicetype_name)
            data1 = {"code": 1, "info": "success"}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_invoicetype.add_url_rule("/invoicetype/",view_func=Invoicetype.as_view("invoicetype1"))
# http://127.0.0.1:5002/invoice/invoicetype/
# http://127.0.0.1:5002/invoice/invoicetype?invoice_type_name=交
# {"invoicetype_name":"差旅"}

class InvoicetypeEdit(MethodView):
    def get(self):
        invoicetype_id = request.args.get('invoicetype_id')
        if invoicetype_id == None:
            data1 = {"code": 0, "info": "缺少参数"}
        else:
            invoicetype_id = int(invoicetype_id)
            invoicetype_one_dict = GetInvoicetypeByInvoicetypeId(invoicetype_id)
            data1 = {"code": 1, "info": "success", "data": invoicetype_one_dict}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        if 'invoicetype_id' in data_dict and 'invoicetype_name' in data_dict:
            invoicetype_id = data_dict['invoicetype_id']
            invoicetype_name = data_dict['invoicetype_name']
            invoicetype_id = int(invoicetype_id)
            UpdateInvoicetype(invoicetype_id, invoicetype_name)
            data1 = {"code": 1, "info": "success"}
        else:
            data1 = {"code": 0, "info": "缺少参数"}
        data = json.dumps(data1, ensure_ascii=False)
        return data

Blue_invoicetype.add_url_rule("/invoicetype_edit/",view_func=InvoicetypeEdit.as_view("invoicetype2"))