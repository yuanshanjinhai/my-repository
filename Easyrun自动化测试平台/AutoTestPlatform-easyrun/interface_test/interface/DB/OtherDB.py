# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.CreatDB_Test import *
from sqlalchemy import and_

def CountInterfaceData():
    r = db.session.query(Test_Interface).count()
    return r

def CountInterfaceData_product_name(product_name):
    product_id = GetProduct_id_by_product_name(product_name)
    r = db.session.query(Test_Interface).filter(Test_Interface.product_id==product_id).count()
    return r

def GetInterfaceList(offset, limit):
    r = db.session.query(Test_Interface.id, System_Product.product_name, Test_Interface.interface_name,
                         Test_Interface.interface_order, Test_Interface.interface_address,
                          Test_Interface.interface_explain).join(System_Product,System_Product.id==Test_Interface.product_id).order_by(
        System_Product.id).order_by(Test_Interface.interface_order).offset(offset).limit(limit).all()
    return r

def GetInterfaceList_product_name(product_name,offset,limit):
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name==product_name).first()[0]
    r = db.session.query(Test_Interface.id, System_Product.product_name, Test_Interface.interface_name,
                         Test_Interface.interface_order, Test_Interface.interface_address,
                         Test_Interface.interface_explain).join(System_Product,
                                                                System_Product.id == Test_Interface.product_id).filter(
        Test_Interface.product_id == product_id).order_by(Test_Interface.interface_order).offset(offset).limit(
        limit).all()
    return r

def JudgeInterfaceNameIsRepeat_NC(product_name, interface_name): # 判断接口名称是否重复(新增和复制新增时使用）
    product_id = GetProduct_id_by_product_name(product_name)
    case_interface_list0 = db.session.query(Test_Interface.interface_name).filter(Test_Interface.product_id == product_id).all()
    case_interface_list = list(map(lambda x: x[0], case_interface_list0))
    if interface_name in case_interface_list:
        return 0
    else:
        return 1

def JudgeInterfaceNameIsRepeat_E(product_name, interface_name): # 判断接口名称是否重复（编辑时使用）
    product_id = GetProduct_id_by_product_name(product_name)
    case_interface_list0 = db.session.query(Test_Interface.interface_name).filter(
        and_(Test_Interface.product_id == product_id, Test_Interface.interface_name != interface_name)).all()
    case_interface_list = list(map(lambda x: x[0], case_interface_list0))
    if interface_name in case_interface_list:
        return 0
    else:
        return 1

def DeleteInterface(interface_id):
    db.session.query(Test_Interface).filter(Test_Interface.id == interface_id).delete()
    db.session.commit()

def GetInterfaceNameByInterfaceId(interface_id):
    interface_name = db.session.query(Test_Interface.interface_name).filter(Test_Interface.id==interface_id).first()[0]
    return interface_name

def GetInterfaceOrderByInterfaceId(interface_id):
    interface_order = db.session.query(Test_Interface.interface_order).filter(Test_Interface.id==interface_id).first()[0]
    return interface_order

def GetInterfaceAddressByInterfaceId(interface_id):
    interface_address = db.session.query(Test_Interface.interface_address).filter(Test_Interface.id==interface_id).first()[0]
    return interface_address

def GetMethodByInterfaceId(interface_id):
    method = db.session.query(Test_Interface.method).filter(Test_Interface.id==interface_id).first()[0]
    return method

def GetInterfaceExplainByInterfaceId(interface_id):
    interface_explin = db.session.query(Test_Interface.interface_explain).filter(Test_Interface.id==interface_id).first()[0]
    return interface_explin

if __name__ == '__main__':
    print( GetInterfaceList(5, 5) )
