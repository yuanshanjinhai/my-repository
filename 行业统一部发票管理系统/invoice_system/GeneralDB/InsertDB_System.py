# coding=utf-8
from GeneralDB.CreatDB import *
from GeneralDB.CreatDB_System import *

class InsertDB_System():
    def __init__(self):
        self.db=db

    def insert_system_company(self,company_name,company_abbreviation,company_explain):
        this_data = System_Company(company_name,company_abbreviation,company_explain)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_department(self,department_name,department_explain):
        this_data = System_Department(department_name,department_explain)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_company_department(self,company_id,department_id):
        this_data = System_Company_Department(company_id,department_id)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_user(self,user_login_name,user_name,password,company_id,department_id):
        this_data = System_User(user_login_name,user_name,password,company_id,department_id)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_product(self,product_name,product_abbreviation,product_explain):
        this_data = System_Product(product_name,product_abbreviation,product_explain)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_invoice_type(self,invoicetype_name):
        this_data = System_Invoicetype(invoicetype_name)
        db.session.add(this_data)
        db.session.commit()

if __name__ == '__main__':
    ins_insert = InsertDB_System()
    # ins_insert.insert_system_department('开发部', '开发人员的部门')
    # ins_insert.insert_system_department('测开部', '测开人员的部门')
    # ins_insert.insert_system_department('财务部', '财务人员的部门')

    # ins_insert.insert_system_company('百度', 'bd', '百度集团')
    # ins_insert.insert_system_company('阿里', 'al', '阿里集团')
    # ins_insert.insert_system_company('腾讯', 'tx', '腾讯集团')

    # ins_insert.insert_system_company_department(1,1)
    # ins_insert.insert_system_company_department(1,2)
    # ins_insert.insert_system_company_department(1, 3)
    # ins_insert.insert_system_company_department(2, 4)
    # ins_insert.insert_system_company_department(2, 5)
    # ins_insert.insert_system_company_department(2, 6)
    # ins_insert.insert_system_company_department(3, 7)
    # ins_insert.insert_system_company_department(3, 8)
    # ins_insert.insert_system_company_department(3, 9)

    # ins_insert.insert_system_invoice_type('餐饮')
    # ins_insert.insert_system_invoice_type('交通')
    # ins_insert.insert_system_invoice_type('住宿')
    # ins_insert.insert_system_invoice_type('其他')
