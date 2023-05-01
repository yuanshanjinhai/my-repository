# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.CreatDB_System import *

def GetProductNameList():
    r0 = db.session.query(System_Product.product_name).all()
    r_list = []
    for ir in r0:
        r_list.append((ir[0],ir[0]))
    return r_list

def GetProduct_id_by_product_name(product_name):
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name == product_name).first()[0]
    return product_id

def GetProduct_name_by_product_id(product_name):
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name==product_name).first()[0]
    return product_id

def GetCaseGroupIdByCaseGroupName(case_group_name):
    case_group_id = db.session.query(Test_Case_Group.id).filter(Test_Case_Group.case_group_name==case_group_name).first()[0]
    return case_group_id

if __name__ == '__main__':
    print( GetProduct_id_by_product_name("测试系统2") )