# coding = utf-8
from GeneralDB.OtherDB import *
from GeneralDB.CreatDB_Test import *
from sqlalchemy import and_

def CountRoleData():
    r = db.session.query(System_Role).count()
    return r

def GetRoleList(offset_,limit_):
    r_list = []
    role_list = db.session.query(System_Role).offset(offset_).limit(limit_).all()
    for ir in role_list:
        tem_resource_name_str = ""
        resource_id_list = db.session.query(System_Role_Resource.resource_id).filter(System_Role_Resource.role_id==ir.id).all()
        for i_resource_id in resource_id_list:
            resource_name = db.session.query(System_Resource.resource_name).filter(System_Resource.id==i_resource_id[0]).first()[0]
            tem_resource_name_str += resource_name+"；"
        role_name_tem_resource_name_str_tupe = (ir.id,ir.role_name,tem_resource_name_str[0:-1])
        r_list.append(role_name_tem_resource_name_str_tupe)
    return r_list

def SearchRoleList(role_name,offset_,limit_):
    r_list = []
    role_list = db.session.query(System_Role).filter(System_Role.role_name.like('%'+ role_name + '%')).offset(offset_).limit(limit_).all()
    for ir in role_list:
        tem_resource_name_str = ""
        resource_id_list = db.session.query(System_Role_Resource.resource_id).filter(
            System_Role_Resource.role_id == ir.id).all()
        for i_resource_id in resource_id_list:
            resource_name = \
            db.session.query(System_Resource.resource_name).filter(System_Resource.id == i_resource_id[0]).first()[0]
            tem_resource_name_str += resource_name + "；"
        role_name_tem_resource_name_str_tupe = (ir.id, ir.role_name, tem_resource_name_str[0:-1])
        r_list.append(role_name_tem_resource_name_str_tupe)
    return r_list

def GetAllResourceStr():
    r_str = ""
    r = db.session.query(System_Resource.resource_name).all()
    for ir in r:
        r_str += ir[0] + "；"
    return r_str[0:-1]

def GetAllResourceStrByRoleId(role_id):
    r_str = ""
    resource_id_list = db.session.query(System_Role_Resource.resource_id).join(System_Role,System_Role.id==System_Role_Resource.role_id).filter(System_Role_Resource.role_id==role_id).all()
    for ir in resource_id_list:
        resource_name = db.session.query(System_Resource.resource_name).filter(System_Resource.id==ir[0]).first()[0]
        r_str += resource_name + "；"
    return r_str[0:-1]

def GetRoleNameList():
    role_name_list = []
    r_list = db.session.query(System_Role.role_name).all()
    for ir in r_list:
        role_name_list.append(ir[0])
    return role_name_list

def GetRoleName(role_id):
    r = db.session.query(System_Role.role_name).filter(System_Role.id==role_id).first()[0]
    return r

def GetAllResourceList():
    r_list = []
    r = db.session.query(System_Resource.resource_name).all()
    for ir in r:
        r_list.append(ir[0])
    return r_list


if __name__ == '__main__':
    print( GetRoleNameList() )