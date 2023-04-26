# coding=utf-8
from GeneralDB.CreatDB import *
from datetime import datetime

class System_Product(db.Model):
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

class System_User(db.Model):
    __tablename__ = "system_user"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    user_login_name = db.Column(db.String(30))
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(32))

    def __init__(self,user_login_name,user_name, password):
        self.user_login_name = user_login_name
        self.user_name = user_name
        self.password = password


class System_Role(db.Model):
    __tablename__ = "system_role"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    role_name = db.Column(db.String(50))

    def __init__(self,role_name):
        self.role_name = role_name


class System_Resource(db.Model):
    __tablename__ = "system_resource"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    resource_name = db.Column(db.String(50))

    def __init__(self,resource_name):
        self.resource_name = resource_name


class System_Role_Resource(db.Model):
    __tablename__ = "system_role_resource"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    role_id = db.Column(db.Integer)
    resource_id = db.Column(db.Integer)

    def __init__(self,role_id,resource_id):
        self.role_id = role_id
        self.resource_id = resource_id


class System_User_Role(db.Model):
    __tablename__ = "system_user_role"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    user_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)

    def __init__(self,user_id,role_id):
        self.user_id = user_id
        self.role_id = role_id


db.create_all()