# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.InserDB import *

def UpdateRoleAndRoleResource(role_id,role_name,resource_list):
    update_role = db.session.query(System_Role).filter(System_Role.id == role_id).first()
    update_role.role_name = role_name
    db.session.commit()

    db.session.query(System_Role_Resource).filter(System_Role_Resource.role_id==role_id).delete()
    db.session.commit()
    for ir in resource_list:
        resource_id = db.session.query(System_Resource.id).filter(System_Resource.resource_name==ir).first()[0]
        add_data = System_Role_Resource(role_id,resource_id)
        db.session.add(add_data)
    db.session.commit()

if __name__ == '__main__':
    E_R_list = db.session.query(System_Role_Resource.id).filter(System_Role_Resource.role_id == 1).all()
    print(E_R_list)