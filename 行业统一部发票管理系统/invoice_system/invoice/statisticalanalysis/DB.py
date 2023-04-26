# coding=utf-8
from GeneralDB.InsertDB_System import *
from GeneralDB.InsertDB_Invoice import *

def GetAllInfo(user_id,company_id,department_id,product_id,invoicetype_id):
    user_name = db.session.query(System_User.user_name).filter(System_User.id==user_id).first()[0]
    company_name = db.session.query(System_Company.company_name).filter(System_Company.id==company_id).first()[0]
    department_name = db.session.query(System_Department.department_name).filter(System_Department.id==department_id).first()[0]
    product_name = db.session.query(System_Product.product_name).filter(System_Product.id==product_id).first()[0]
    invoicetype_name = db.session.query(System_Invoicetype.invoicetype_name).filter(System_Invoicetype.id==invoicetype_id).first()[0]
    r_dict = {'user_name':user_name,'company_name':company_name,'department_name':department_name,
              'product_name':product_name,'invoicetype_name':invoicetype_name}
    return r_dict

def GetQueryRuslt(user_id,invoicetype_id,time_start,time_end):
    time_start += ' 00: 00:00'
    time_end += ' 00: 00:00'
    # 1000
    if user_id != None and invoicetype_id == None and time_start == None and time_end == None:
        query_r = db.session.query(Invoice_invoice).filter(Invoice_invoice.user_id==user_id).all()
    # 0100
    if user_id == None and invoicetype_id != None and time_start == None and time_end == None:
        query_r = db.session.query(Invoice_invoice).filter(Invoice_invoice.invoicetype_id==invoicetype_id).all()
    # 0011
    if user_id == None and invoicetype_id == None and time_start != None and time_end != None:
        query_r = db.session.query(Invoice_invoice).filter(Invoice_invoice.creat_time>=time_start,Invoice_invoice.creat_time<=time_end).all()
    # 1100
    if user_id != None and invoicetype_id != None and time_start == None and time_end == None:
        query_r = db.session.query(Invoice_invoice).filter(Invoice_invoice.user_id==user_id,Invoice_invoice.invoicetype_id==invoicetype_id).all()

    r_list = []
    for i in query_r:
        user_id = i.user_id
        company_id = i.company_id
        department_id = i.department_id
        product_id = i.product_id
        invoicetype_id = i.invoicetype_id
        info_dict = GetAllInfo(user_id, company_id, department_id, product_id, invoicetype_id)
        user_name = info_dict['user_name']
        company_name = info_dict['company_name']
        department_name = info_dict['department_name']
        product_name = info_dict['product_name']
        invoicetype_name = info_dict['invoicetype_name']
        invoice_amount = i.invoice_amount
        invoice_code = i.invoice_code
        invoice_explain = i.invoice_explain
        tem_dict = {'user_name':user_name,'company_name':company_name,'department_name':department_name,
              'product_name':product_name,'invoicetype_name':invoicetype_name,'invoice_amount':invoice_amount,
                    'invoice_code':invoice_code,'invoice_explain':invoice_explain}
        r_list.append(tem_dict)
    return r_list

if __name__ == '__main__':
    print(GetQueryRuslt(1,2,None,None))