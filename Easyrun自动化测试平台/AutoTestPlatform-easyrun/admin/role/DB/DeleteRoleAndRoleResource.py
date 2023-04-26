# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.InserDB import *

def DeleteRoleAndRoleResource(role_id):
    db.session.query(System_Role).filter(System_Role.id==role_id).delete()
    db.session.commit()
    db.session.query(System_Role_Resource).filter(System_Role_Resource.role_id==role_id).delete()
    db.session.commit()

if __name__ == '__main__':
    pass