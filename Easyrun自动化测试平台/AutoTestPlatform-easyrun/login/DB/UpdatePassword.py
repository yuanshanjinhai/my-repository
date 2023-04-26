# coding=utf-8
from GeneralDB.CreatDB import *
from GeneralDB.CreatDB_System import *
from GeneralTools.OtherTools import md5_encrypt

def UpdatePassword(login_name,new_password):
    new_password = md5_encrypt(new_password)
    update_object = db.session.query(System_User).filter(System_User.user_login_name==login_name).first()
    update_object.password = new_password
    db.session.commit()