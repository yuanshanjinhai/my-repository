# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.InserDB import *
from GeneralTools.OtherTools import md5_encrypt

def InsertUserAndUserRole(user_login_name,user_name,role):
    password_str = md5_encrypt("123456")
    ins_insert = Insert_db()
    ins_insert.insert_system_user(user_login_name,user_name,password_str)
    user_id = db.session.query(System_User.id).filter(System_User.user_name==user_name).first()[0]
    role_id = db.session.query(System_Role.id).filter(System_Role.role_name==role).first()[0]
    ins_insert.insert_system_user_role(user_id, role_id)

