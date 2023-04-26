# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.InserDB import *

def UpdateUserAndUserRole(new_password, user_login_name, user_name, role):
    update_user = db.session.query(System_User).filter(System_User.user_login_name==user_login_name).first()
    update_user.user_login_name = user_login_name
    update_user.user_name = user_name
    if new_password != 0:
        update_user.password = new_password
    db.session.commit()

    user_id = db.session.query(System_User.id).filter(System_User.user_login_name==user_login_name).first()[0]
    role_id = db.session.query(System_Role.id).filter(System_Role.role_name==role).first()[0]
    update_user_role = db.session.query(System_User_Role).filter(System_User_Role.user_id==user_id).first()
    update_user_role.role_id = role_id
    db.session.commit()