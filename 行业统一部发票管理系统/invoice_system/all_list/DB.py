# coding=utf-8
from GeneralDB.InsertDB_System import *

def GetUserList():
    user_r = db.session.query(System_User.id,System_User.user_name).all()
    user_list = []
    for i in user_r:
        tem_dict = {'user_id':i[0],'user_name':i[1]}
        user_list.append(tem_dict)
    return user_list

def GetInvoicetypeList():
    r = db.session.query(System_Invoicetype.id,System_Invoicetype.invoicetype_name).all()
    invoicetype_list = []
    for i in r:
        tem_dict = {'invoicetype_id':i.id,'invoicetype_name':i.invoicetype_name}
        invoicetype_list.append(tem_dict)
    return invoicetype_list

if __name__ == '__main__':
    print(GetInvoicetypeList())