# coding=utf-8
from GeneralDB.InsertDB_System import *
from GeneralDB.InsertDB_Invoice import *
from admin.user.DB import GetUserNameByUserId,GetUserIdByUserName
from admin.company.DB import GetCompanyNameByCompanyId
from admin.department.DB import GetDepartmentNameByDepartmentId
from admin.product.DB import GetProductNameByProductId
from admin.invoicetype.DB import GetInvoicetypeNameByInvoicetypeId

def GetInvoiceList():
    invoice_queryset = db.session.query(Invoice_invoice).all()
    invoice_list = []
    for i in invoice_queryset:
        user_id = i.user_id
        user_name = GetUserNameByUserId(user_id)
        company_id = i.company_id
        company_name = GetCompanyNameByCompanyId(company_id)
        department_id = i.department_id
        department_name = GetDepartmentNameByDepartmentId(department_id)
        product_id = i.product_id
        product_name = GetProductNameByProductId(product_id)
        invoicetype_id = i.invoicetype_id
        invoicetype_name = GetInvoicetypeNameByInvoicetypeId(invoicetype_id)
        invoice_amount = i.invoice_amount
        invoice_code = i.invoice_code
        invoice_explain = i.invoice_explain
        tem_dict = {'user_id':user_id,'user_name':user_name,'company_name':company_name,'department_name':
            department_name,'product_name':product_name,'invoicetype_name':invoicetype_name,'invoice_amount':
                    invoice_amount,'invoice_code':invoice_code,'invoice_explain':invoice_explain}
        invoice_list.append((tem_dict))
    return invoice_list

def GetInvoiceListByUserName(user_name):
    user_id = GetUserIdByUserName(user_name)
    invoice_queryset = db.session.query(Invoice_invoice).filter(Invoice_invoice.user_id==user_id).all()
    invoice_list = []
    for i in invoice_queryset:
        user_id = i.user_id
        user_name = GetUserNameByUserId(user_id)
        company_id = i.company_id
        company_name = GetCompanyNameByCompanyId(company_id)
        department_id = i.department_id
        department_name = GetDepartmentNameByDepartmentId(department_id)
        product_id = i.product_id
        product_name = GetProductNameByProductId(product_id)
        invoicetype_id = i.invoicetype_id
        invoicetype_name = GetInvoicetypeNameByInvoicetypeId(invoicetype_id)
        invoice_amount = i.invoice_amount
        invoice_code = i.invoice_code
        invoice_explain = i.invoice_explain
        tem_dict = {'user_id': user_id, 'user_name': user_name, 'company_name': company_name, 'department_name':
            department_name, 'product_name': product_name, 'invoicetype_name': invoicetype_name, 'invoice_amount':
                        invoice_amount, 'invoice_code': invoice_code, 'invoice_explain': invoice_explain}
        invoice_list.append((tem_dict))
    return invoice_list

def GetInvoiceListByInvoicetypeName(invoicetype_name):
    invoicetype_id_q = db.session.query(System_Invoicetype.id).filter(System_Invoicetype.invoicetype_name==invoicetype_name).first()
    invoicetype_id = invoicetype_id_q[0]
    invoice_queryset = db.session.query(Invoice_invoice).filter(Invoice_invoice.invoicetype_id == invoicetype_id).all()
    invoice_list = []
    for i in invoice_queryset:
        user_id = i.user_id
        user_name = GetUserNameByUserId(user_id)
        company_id = i.company_id
        company_name = GetCompanyNameByCompanyId(company_id)
        department_id = i.department_id
        department_name = GetDepartmentNameByDepartmentId(department_id)
        product_id = i.product_id
        product_name = GetProductNameByProductId(product_id)
        invoicetype_id = i.invoicetype_id
        invoicetype_name = GetInvoicetypeNameByInvoicetypeId(invoicetype_id)
        invoice_amount = i.invoice_amount
        invoice_code = i.invoice_code
        invoice_explain = i.invoice_explain
        tem_dict = {'user_id': user_id, 'user_name': user_name, 'company_name': company_name, 'department_name':
            department_name, 'product_name': product_name, 'invoicetype_name': invoicetype_name, 'invoice_amount':
                        invoice_amount, 'invoice_code': invoice_code, 'invoice_explain': invoice_explain}
        invoice_list.append((tem_dict))
    return invoice_list

def GetInvoiceOneListByUserId(user_id):
    invoice_one_list_q = db.session.query(Invoice_invoice).filter(Invoice_invoice.user_id==user_id).first()
    user_id = invoice_one_list_q.user_id
    user_name = GetUserNameByUserId(user_id)
    company_id = invoice_one_list_q.company_id
    company_name = GetCompanyNameByCompanyId(company_id)
    department_id = invoice_one_list_q.department_id
    department_name = GetDepartmentNameByDepartmentId(department_id)
    product_id = invoice_one_list_q.product_id
    product_name = GetProductNameByProductId(product_id)
    invoicetype_id = invoice_one_list_q.invoicetype_id
    invoicetype_name = GetInvoicetypeNameByInvoicetypeId(invoicetype_id)
    invoice_amount = invoice_one_list_q.invoice_amount
    invoice_code = invoice_one_list_q.invoice_code
    invoice_explain = invoice_one_list_q.invoice_explain
    invoice_one_dict = {'user_id': user_id, 'user_name': user_name, 'company_name': company_name, 'department_name':
        department_name, 'product_name': product_name, 'invoicetype_name': invoicetype_name, 'invoice_amount':
         invoice_amount, 'invoice_code': invoice_code, 'invoice_explain': invoice_explain}
    return invoice_one_dict

def GetDepartmentIdByCompanyDepartmentName(company_id,department_name):
    department_tuple = db.session.query(System_Department.id).\
        filter(System_Department.department_name==department_name).all()
    for i in department_tuple:
        this_department_id = i[0]
        r_tuple = db.session.query(System_Company_Department.department_id).filter(System_Company_Department.company_id==company_id,System_Company_Department.department_id==this_department_id).first()
        if r_tuple != None:
            department_id = r_tuple[0]
            return department_id

def GetProductIdByProductName(product_name):
    r = db.session.query(System_Product.id).filter(System_Product.product_name==product_name).first()
    product_id = r[0]
    return product_id

def GetInvoicetypeIdByInvoicetypeName(invoicetype_name):
    r = db.session.query(System_Invoicetype.id).filter(System_Invoicetype.invoicetype_name==invoicetype_name).first()
    invoicetype_id = r[0]
    return invoicetype_id

def InsertInvoice(user_id,company_id,department_id,product_id,invoicetype_id,invoice_amount,invoice_code,invoice_explain):
    ins_insert = InsertDB_Invoice()
    ins_insert.insert_invoice_invoice(user_id,company_id,department_id,product_id,invoicetype_id,invoice_amount,invoice_code,invoice_explain)

def UpdateInvoice(invoice_id,company_id,department_id,product_id,invoicetype_id,invoice_amount,invoice_code,invoice_explain):
    # UpdateInvoice(invoice_id,company_id,department_id,product_id,invoicetype_id,invoice_amount,invoice_code,invoice_explain)
    update_queryset = db.session.query(Invoice_invoice).filter(Invoice_invoice.id==invoice_id).first()
    update_queryset.company_id = company_id
    update_queryset.department_id = department_id
    update_queryset.product_id = product_id
    update_queryset.invoicetype_id = invoicetype_id
    update_queryset.invoice_amount = invoice_amount
    update_queryset.invoice_code = invoice_code
    update_queryset.invoice_explain = invoice_explain
    db.session.commit()

def GetCompanyIdDepartmentIdByUserId(user_id):
    r_tuple = db.session.query(System_User.company_id,System_User.department_id).filter(System_User.id==user_id).first()
    return r_tuple

if __name__ == '__main__':
    print( GetInvoiceOneListByUserId(1))