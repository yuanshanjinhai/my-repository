# coding=utf-8
from GeneralDB.CreatDB import *
from GeneralDB.CreatDB_System import *

def GetPasswordByUsername(login_name):
    password = db.session.query(System_User.password).filter(System_User.user_login_name==login_name).first()[0]
    return password