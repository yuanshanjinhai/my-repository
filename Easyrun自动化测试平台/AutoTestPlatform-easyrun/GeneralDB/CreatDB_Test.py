# coding=utf-8
from GeneralDB.CreatDB import *
from datetime import datetime

class Test_Interface(db.Model):
    __tablename__="test_interface"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    product_id = db.Column(db.Integer)
    interface_name = db.Column(db.String(50))
    interface_order = db.Column(db.Integer)
    interface_address = db.Column(db.String(500))
    method = db.Column(db.Enum("POST", "GET"))
    interface_explain = db.Column(db.String(600))

    def __init__(self,product_id,interface_name,interface_order,interface_address,method,interface_explain):
        self.product_id = product_id
        self.interface_name=interface_name
        self.interface_order=interface_order
        self.interface_address=interface_address
        self.method=method
        self.interface_explain = interface_explain


class Test_Case_Group(db.Model):
    __tablename__ = "test_case_group"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    product_id = db.Column(db.Integer)
    is_run = db.Column(db.String(1))
    case_group_name = db.Column(db.String(100))
    case_group_order = db.Column(db.Integer)
    case_group_type = db.Column(db.Enum("起始组","并发组","结束组")) # 用例组类型
    case_group_explain = db.Column(db.String(800))

    def __init__(self,product_id,is_run,case_group_name,case_group_order,case_group_type,case_group_explain):
        self.product_id = product_id
        self.is_run = is_run
        self.case_group_name = case_group_name
        self.case_group_order = case_group_order
        self.case_group_type = case_group_type
        self.case_group_explain = case_group_explain


class Test_Global_Var(db.Model):
    __tablename__ = "test_global_var"

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    product_id = db.Column(db.Integer)
    global_var_name = db.Column(db.String(50))
    global_var_value = db.Column(db.String(300))
    is_auto_add = db.Column(db.Enum("是", "否"))
    global_var_explain = db.Column(db.String(500))

    def __init__(self,product_id,global_var_name,global_var_value,is_auto_add,global_var_explain):
        self.product_id = product_id
        self.global_var_name = global_var_name
        self.global_var_value = global_var_value
        self.is_auto_add = is_auto_add
        self.global_var_explain = global_var_explain


class Test_Encrypt_Decrypt(db.Model):
    __tablename__ = "test_encrypt_decrypt"

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    file_name = db.Column(db.String(50))
    file_name_explain = db.Column(db.String(500))

    def __init__(self,file_name,file_name_explain):
        self.file_name = file_name
        self.file_name_explain = file_name_explain


class Test_Case(db.Model):
    __tablename__="test_case"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    product_id = db.Column(db.Integer)
    case_group_id = db.Column(db.Integer)
    interface_id = db.Column(db.Integer)
    interface_address = db.Column(db.Text)
    is_relationed = db.Column(db.Integer)
    case_name = db.Column(db.String(100))
    case_order = db.Column(db.Integer)
    is_urlencode_pwd = db.Column(db.Integer)
    encrypt_decrypt_file = db.Column(db.String(50))
    case_explain = db.Column(db.String(500))
    header = db.Column(db.Text)
    body = db.Column(db.Text)
    expect_response = db.Column(db.Text)
    creat_time = db.Column(db.String(20))
    update_time = db.Column(db.String(20))

    def __init__(self,product_id,case_group_id,interface_id,interface_address,is_relationed,case_name,case_order,is_urlencode_pwd,encrypt_decrypt_file,case_explain,header,body,expect_response,creat_time,update_time):
        self.product_id = product_id
        self.case_group_id = case_group_id
        self.interface_id = interface_id
        self.interface_address = interface_address
        self.is_relationed = is_relationed
        self.case_name = case_name
        self.case_order = case_order
        self.is_urlencode_pwd = is_urlencode_pwd
        self.encrypt_decrypt_file = encrypt_decrypt_file
        self.case_explain = case_explain
        self.header = header
        self.body = body
        self.expect_response = expect_response
        self.creat_time = creat_time
        self.update_time = update_time

class Test_relation(db.Model):
    __tablename__ = "test_relation"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    product_id = db.Column(db.Integer)
    case_group_id = db.Column(db.Integer)
    case_id = db.Column(db.Integer)
    relation_name = db.Column(db.String(50))
    relation_field = db.Column(db.String(15))
    json_path = db.Column(db.Text)

    def __init__(self,product_id,case_group_id,case_id,relation_name,relation_field,json_path):
        self.product_id = product_id
        self.case_group_id = case_group_id
        self.case_id = case_id
        self.relation_name = relation_name
        self.relation_field = relation_field
        self.json_path = json_path

class Test_run_result(db.Model):
    __tablename__ = "test_run_result"

    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    case_id = db.Column(db.Integer)
    actual_response = db.Column(db.Text)
    run_time = db.Column(db.DateTime, default=datetime.now)
    is_pass = db.Column(db.Enum("是", "否"))

    def __init__(self,case_id,actual_response,run_time,is_pass):
        self.case_id = case_id
        self.actual_response = actual_response
        self.run_time = run_time
        self.is_pass = is_pass


db.create_all()