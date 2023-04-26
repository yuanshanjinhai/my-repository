# coding=utf-8
from GeneralDB.InsertDB_System import *

def GetInvoicetype():
    invoicetype_list0 = db.session.query(System_Invoicetype.id,System_Invoicetype.system_invoice_type_name).all()
    invoicetype_list = []
    for i in invoicetype_list0:
        tem_dic = {'invoice_Type_id':i[0],'system_invoice_type_name':i[1]}
        invoicetype_list.append(tem_dic)
    return invoicetype_list

def GetInvoicetypeByInvoicetypeId(invoicetype_id):
    r = db.session.query(System_Invoicetype).filter(System_Invoicetype.id==invoicetype_id).first()
    invoicetype_one_dict = {"invoicetype_id":r.id,'system_invoice_type_name':r.system_invoice_type_name}
    return invoicetype_one_dict

def GetInvoicetypeByInvoicetypeName(invoicetype_name):
    this_like = "%" + invoicetype_name + "%"
    invoicetype_list0 = db.session.query(System_Invoicetype.id,System_Invoicetype.system_invoice_type_name).\
        filter(System_Invoicetype.system_invoice_type_name.like(this_like)).all()
    invoicetype_list = []
    for i in invoicetype_list0:
        invoicetype_list.append({'invoicetype_id':i[0],'system_invoice_type_name':i[1]})
    return invoicetype_list

def GetInvoicetypeNameByInvoicetypeId(invoicetype_id):
    invoicetype_name_q = db.session.query(System_Invoicetype.invoicetype_name).filter(System_Invoicetype.id==invoicetype_id).first()
    invoicetype_name = invoicetype_name_q[0]
    return invoicetype_name

def InsertInvoicetype(system_invoice_type_name):
    ins_insert = InsertDB_System()
    ins_insert.insert_system_invoice_type(system_invoice_type_name)

def UpdateInvoicetype(invoicetype_id,system_invoice_type_name):
    obj = db.session.query(System_Invoicetype).filter(System_Invoicetype.id==invoicetype_id).first()
    obj.system_invoice_type_name = system_invoice_type_name
    db.session.commit()

if __name__ == '__main__':
    print( GetInvoicetypeNameByInvoicetypeId(2) )