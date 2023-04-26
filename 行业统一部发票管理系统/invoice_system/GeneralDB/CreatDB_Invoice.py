# coding=utf-8
from GeneralDB.CreatDB import *
from datetime import datetime

class Invoice_invoice(db.Model): # 公司表
    __tablename__ = "invoice_invoice"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    user_id = db.Column(db.Integer)
    company_id = db.Column(db.Integer)
    department_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    invoicetype_id = db.Column(db.Integer)
    invoice_amount = db.Column(db.Integer)
    invoice_code = db.Column(db.String(30))
    invoice_explain = db.Column(db.String(1000)) # 备注说明
    creat_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, user_id,company_id, department_id,product_id,invoicetype_id,invoice_amount,invoice_code,invoice_explain,creat_time=datetime.now()):
        self.user_id = user_id
        self.company_id = company_id
        self.department_id = department_id
        self.product_id = product_id
        self.invoicetype_id = invoicetype_id
        self.invoice_amount = invoice_amount
        self.invoice_code = invoice_code
        self.invoice_explain = invoice_explain
        self.creat_time = creat_time


db.create_all()