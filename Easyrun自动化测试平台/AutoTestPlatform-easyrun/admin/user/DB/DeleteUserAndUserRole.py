# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.InserDB import *

def DeleteUserAndUserRole(user_id):
    db.session.query(System_User).filter(System_User.id==user_id).delete()
    db.session.commit()
    db.session.query(System_User_Role).filter(System_User_Role.user_id==user_id).delete()
    db.session.commit()