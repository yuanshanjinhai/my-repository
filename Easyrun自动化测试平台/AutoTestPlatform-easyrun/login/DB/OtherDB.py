# coding=utf-8
from GeneralDB.CreatDB import *
from GeneralDB.CreatDB_System import *
from GeneralTools.OtherTools import md5_encrypt

def GetUserResourceList(user_login_name):
    user_resource_list = []
    if user_login_name == "admin":
        user_resource_list0 = db.session.query(System_Resource.resource_name).all()
        for iu in user_resource_list0:
            user_resource_list.append(iu.resource_name)
    else:
        user_id = db.session.query(System_User.id).filter(System_User.user_login_name==user_login_name).first()[0]
        role_id = db.session.query(System_User_Role.role_id).filter(System_User_Role.user_id==user_id).first()[0]
        resource_id_list = db.session.query(System_Role_Resource.resource_id).filter(System_Role_Resource.role_id==role_id).all()
        for ir in resource_id_list:
            resource_name = db.session.query(System_Resource.resource_name).filter(System_Resource.id==ir[0]).first()[0]
            user_resource_list.append(resource_name)
    if "interface-singlerun" in user_resource_list or 'interface-interface' in user_resource_list or 'interface-case_group' in user_resource_list or 'interface-global' in user_resource_list or 'interface-encypt_decypt' in user_resource_list or 'interface-case' in user_resource_list or 'interface-run' in user_resource_list or 'interface-result' in user_resource_list or 'interface-singlerun' in user_resource_list:
        user_resource_list.append('interface')
    if 'tools-creat_boundart' in user_resource_list or 'tools-str_len' in user_resource_list:
        user_resource_list.append("tools")
    if 'help-case_rule' in user_resource_list:
        user_resource_list.append('help')
    if 'admin-user' in user_resource_list or 'admin-role' in user_resource_list or 'admin-product' in user_resource_list:
        user_resource_list.append('admin')
    print('user_resource_list=',user_resource_list)
    return user_resource_list

def JudegeUserPassword(user_login_name,input_password):
    if user_login_name == "admin" and input_password == "123456":
        return 1
    DB_password = db.session.query(System_User.password).filter(System_User.user_login_name==user_login_name).first()
    if DB_password == None:
        return 0
    else:
        DB_password = DB_password[0]
    input_password = md5_encrypt(input_password)
    if DB_password == input_password:
        return 1
    else:
        return 0

def GetUserNameByUserLoginName(user_login_name):
    if user_login_name == "admin":
        return "超级管理员"
    user_name = db.session.query(System_User.user_name).filter(System_User.user_login_name==user_login_name).first()[0]
    return user_name

def judge_login_name_is_exis(login_name):
    login_name_list = []
    login_name_list0 = db.session.query(System_User.user_login_name).all()
    for i in login_name_list0:
        login_name_list.append(i[0])
    if login_name in login_name_list:
        return 1
    else:
        return 0

def judge_old_password(login_name,old_password):
    old_password = md5_encrypt(old_password)
    DB_old_password = db.session.query(System_User.password).filter(System_User.user_login_name==login_name).first()[0]
    if DB_old_password == old_password:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(GetUserResourceList('admin'))