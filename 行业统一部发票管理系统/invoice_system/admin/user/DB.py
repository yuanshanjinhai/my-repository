# coding=utf-8
from GeneralDB.InsertDB_System import *

def InsertUser(user_login_name,user_name,password,company_id,department_id):
    ins_insert = InsertDB_System()
    ins_insert.insert_system_user(user_login_name,user_name,password,company_id,department_id)

def GetUserloginnameList(user_login_name):
    user_login_name_object = db.session.query(System_User.user_login_name).all()
    if user_login_name_object == []:
        return 1
    user_login_name_list = []
    for i in user_login_name_object:
        user_login_name_list.append(i[0])
    if user_login_name not in user_login_name_list:
        return 1
    return 0

def GetUserList():
    user_list0 = db.session.query(System_User.user_login_name,System_User.user_name).all()
    user_list = []
    tem_dict = {}
    for i in user_list0:
        tem_dict['user_login_name'] = i[0]
        tem_dict['user_name'] = i[1]
        user_list.append(tem_dict)
        tem_dict = {}
    return user_list

def GetUserNameByUserId(user_id):
    user_name_q = db.session.query(System_User.user_name).filter(System_User.id==user_id).first()
    user_name = user_name_q[0]
    return user_name

def GetUserIdByUserName(user_name):
    user_id_q = db.session.query(System_User.id).filter(System_User.user_name==user_name).first()
    user_id = user_id_q[0]
    return user_id

if __name__ == '__main__':
    print( GetUserIdByUserName('王睿昊') )