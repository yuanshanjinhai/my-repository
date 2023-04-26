# coding=utf-8
from GeneralDB.CreatDB import *
from datetime import datetime

class System_Company(db.Model): # 公司表
    __tablename__ = "system_company"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    company_name = db.Column(db.String(50))
    company_abbreviation = db.Column(db.String(30)) # 项目简写
    company_explain = db.Column(db.String(1000)) # 备注说明
    creat_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, company_name,company_abbreviation, product_explain,creat_time=datetime.now()):
        self.company_name = company_name
        self.company_abbreviation = company_abbreviation
        self.product_explain = product_explain
        self.creat_time = creat_time


class System_Department(db.Model):
    __tablename__ = "system_department"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    department_name = db.Column(db.String(30))
    department_explain = db.Column(db.String(1000))  # 备注说明

    def __init__(self,department_name,department_explain):
        self.department_name = department_name
        self.department_explain = department_explain


class System_Company_Department(db.Model):
    __tablename__ = "system_company_department"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    company_id = db.Column(db.Integer)
    department_id = db.Column(db.Integer)

    def __init__(self,company_id,department_id):
        self.company_id = company_id
        self.department_id = department_id


class System_User(db.Model):
    __tablename__ = "system_user"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    user_login_name = db.Column(db.String(30))
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(32))
    company_id = db.Column(db.Integer)
    department_id = db.Column(db.Integer)

    def __init__(self,user_login_name,user_name, password,company_id,department_id):
        self.user_login_name = user_login_name
        self.user_name = user_name
        self.password = password
        self.company_id = company_id
        self.department_id = department_id


# class System_User_Company_Department(db.Model):
#     __tablename__ = "system_user_company_department"
#
#     id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
#     user_id = db.Column(db.Integer)
#     company_id = db.Column(db.Integer)
#     department_id = db.Column(db.Integer)
#
#     def __init__(self,user_id,company_id,department_id):
#         self.user_id = user_id
#         self.company_id = company_id
#         self.department_id = department_id


class System_Product(db.Model): #
    __tablename__ = "system_product"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    product_name = db.Column(db.String(50))
    product_abbreviation = db.Column(db.String(30)) # 项目简写
    product_explain = db.Column(db.String(1000))
    creat_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, product_name,product_abbreviation, product_explain,creat_time=datetime.now()):
        self.product_name = product_name
        self.product_abbreviation = product_abbreviation
        self.product_explain = product_explain
        self.creat_time = creat_time


class System_Invoicetype(db.Model):
    __tablename__ = "system_invoicetype"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    invoicetype_name = db.Column(db.String(30))

    def __init__(self,invoicetype_name):
        self.invoicetype_name = invoicetype_name


db.create_all()