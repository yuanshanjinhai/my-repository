# coding=utf-8
# coding=utf-8
from GeneralDB.InsertDB_System import *

def GetUeridByUserLoginName(user_login_name):
    r = db.session.query(System_User.id).filter(System_User.user_login_name==user_login_name).first()
    user_id = r[0]
    return user_id