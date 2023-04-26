# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.InserDB import *

def InsertRoleAndRoleResource(role_name,resource_list):
    ins_insert = Insert_db()
    ins_insert.insert_system_role(role_name)
    role_id = db.session.query(System_Role.id).filter(System_Role.role_name==role_name).first()[0]
    for ir in resource_list:
        resource_id = db.session.query(System_Resource.id).filter(System_Resource.resource_name==ir).first()[0]
        ins_insert.insert_system_role_resource(role_id,resource_id)