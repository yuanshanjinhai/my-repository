# coding = utf-8
from GeneralDB.CreatDB_System import *
from GeneralDB.CreatDB_Test import *

def CountUserData():
    r = db.session.query(System_User).count()
    return r

def GetUserList(offset_, limit_):
    user_list = []
    user_list0 = db.session.query(System_User.id,System_User.user_login_name,System_User.user_name).offset(offset_).limit(limit_).all()
    for iu in user_list0:
        user_id = iu.id
        role_id = db.session.query(System_User_Role.role_id).filter(System_User_Role.user_id==user_id).first()[0]
        role_name = db.session.query(System_Role.role_name).filter(System_Role.id==role_id).first()[0]
        user_list.append( (user_id,iu.user_login_name,iu.user_name,role_name) )
    return user_list

def SearchGetUserList(user_name, offset_, limit_):
    user_list = []
    user_list0 = db.session.query(System_User.id, System_User.user_login_name, System_User.user_name).filter(
        System_User.user_name.like("%" + user_name + "%")).offset(offset_).limit(limit_).all()
    for iu in user_list0:
        user_id = iu.id
        role_id = db.session.query(System_User_Role.role_id).filter(System_User_Role.user_id == user_id).first()[0]
        role_name = db.session.query(System_Role.role_name).filter(System_Role.id == role_id).first()[0]
        user_list.append((user_id, iu.user_login_name, iu.user_name, role_name))
    return user_list

def GetRoleList_():
    role_list = []
    r = db.session.query(System_Role.role_name).all()
    for i in r:
        role_list.append((i[0],i[0]))
    return role_list

def GetRole(user_id):
    role_id = db.session.query(System_User_Role.role_id).filter(System_User_Role.user_id==user_id).first()[0]
    role_name = db.session.query(System_Role.role_name).filter(System_Role.id==role_id).first()[0]
    # role_name = db.session.query(System_Role.role_name).join(System_Role,System_Role.id==System_User_Role.role_id).filter(System_User_Role.user_id==user_id).first()[0]
    return role_name

def GetUserLoginName(user_id):
    user_login_name = db.session.query(System_User.user_login_name).filter(System_User.id==user_id).first()[0]
    return user_login_name

def GetUserName(user_id):
    user_name = db.session.query(System_User.user_name).filter(System_User.id==user_id).first()[0]
    return user_name

def JudgeUserNameIsRepead(user_login_name):
    r_list = []
    user_list = db.session.query(System_User.user_login_name).all()
    for iu in user_list:
        r_list.append(iu[0])
    if user_login_name in r_list:
        return 0
    else:
        return 1

if __name__ == '__main__':
    print( GetUserList(0, 5) )