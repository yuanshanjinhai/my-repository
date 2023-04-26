# coding=utf-8
from GeneralDB.CreatDB import *
from GeneralDB.CreatDB_Invoice import *

class InsertDB_Invoice():
    def __init__(self):
        self.db=db

    def insert_invoice_invoice(self,user_id,company_id,department_id,product_id,invoicetype_id,invoice_amount,invoice_code,invoice_explain):
        this_data = Invoice_invoice(user_id,company_id, department_id,product_id,invoicetype_id,invoice_amount,invoice_code,invoice_explain)
        db.session.add(this_data)
        db.session.commit()
