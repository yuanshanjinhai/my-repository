# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
from admin.department.DB import GetCompanyIdByCompanyName
from invoice.invoice.DB import GetDepartmentIdByCompanyDepartmentName,GetProductIdByProductName,\
    GetInvoicetypeIdByInvoicetypeName,InsertInvoice,GetCompanyIdDepartmentIdByUserId,GetInvoiceList,\
    GetInvoiceListByUserName,GetInvoiceListByInvoicetypeName,GetInvoiceOneListByUserId,UpdateInvoice
import json

Blue_invoice = Blueprint("invoice",__name__)

class Invoice(MethodView):
    def get(self):
        user_name = request.args.get('user_name')
        invoicetype_name = request.args.get('invoicetype_name')
        if user_name == None and invoicetype_name == None:
            invoice_list = GetInvoiceList()
        if user_name != None and invoicetype_name == None:
            invoice_list = GetInvoiceListByUserName(user_name)
        if user_name == None and invoicetype_name != None:
            invoice_list = GetInvoiceListByInvoicetypeName(invoicetype_name)
        data1 = {"code": 1, "info": "success", "data": invoice_list}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        print("data_dict=",data_dict)
        user_id = int(data_dict['user_id'])
        product_name = data_dict['product_name']
        invoicetype_name = data_dict['invoicetype_name']
        invoice_amount = data_dict['invoice_amount']
        invoice_code = data_dict['invoice_code']
        invoice_explain = data_dict['invoice_explain']

        company_id = GetCompanyIdDepartmentIdByUserId(user_id)[0]
        department_id = GetCompanyIdDepartmentIdByUserId(user_id)[1]
        print('product_name=',product_name)
        product_id = GetProductIdByProductName(product_name)
        invoicetype_id = GetInvoicetypeIdByInvoicetypeName(invoicetype_name)

        InsertInvoice(user_id, company_id, department_id, product_id, invoicetype_id, invoice_amount, invoice_code,
                          invoice_explain)
        data1 = {"code": 1, "info": "success"}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_invoice.add_url_rule("/invoice/",view_func=Invoice.as_view("invoice1"))
# http://127.0.0.1:5002/invoice/invoice/
# http://127.0.0.1:5002/invoice/invoice?user_name=王睿昊
# {"user_id":1,"product_name":"发票管理系统","invoicetype_name":"交通","invoice_amount":500,"invoice_code":"jt123456","invoice_explain":"每天的交通费"}

class InvoiceEdet(MethodView):
    def get(self):
        user_id= int(request.args.get('user_id'))
        invoice_one_dict = GetInvoiceOneListByUserId(user_id)
        data1 = {"code": 1, "info": "success", "data": invoice_one_dict}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        invoice_id = int(data_dict['invoice_id'])
        user_id = int(data_dict['user_id'])
        product_name = data_dict['product_name']
        invoicetype_name = data_dict['invoicetype_name']
        invoice_amount = int(data_dict['invoice_amount'])
        invoice_code = data_dict['invoice_code']
        invoice_explain = data_dict['invoice_explain']

        company_id = GetCompanyIdDepartmentIdByUserId(user_id)[0]
        department_id = GetCompanyIdDepartmentIdByUserId(user_id)[1]
        product_id = GetProductIdByProductName(product_name)
        invoicetype_id = GetInvoicetypeIdByInvoicetypeName(invoicetype_name)

        UpdateInvoice(invoice_id, company_id, department_id, product_id, invoicetype_id, invoice_amount,
                      invoice_code, invoice_explain)
        data1 = {"code": 1, "info": "success"}
        data = json.dumps(data1, ensure_ascii=False)
        return data

Blue_invoice.add_url_rule("/invoice_edit/",view_func=InvoiceEdet.as_view("invoice2"))
# http://127.0.0.1:5002/invoice/invoice_edit?user_id=1
# http://127.0.0.1:5002/invoice/invoice_edit/
# {"invoice_id":1,"user_id":1,"product_name":"发票管理系统","invoicetype_name":"交通","invoice_amount":700,"invoice_code":"jt123456","invoice_explain":"每天的交通费啊"}