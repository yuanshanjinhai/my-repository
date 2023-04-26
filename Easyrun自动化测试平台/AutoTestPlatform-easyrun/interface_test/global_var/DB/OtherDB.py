# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *
from sqlalchemy import and_

def CountGlobalVarData():
    r = db.session.query(Test_Global_Var).count()
    return r

def CountGlobalVarData_product_name(product_name):
    product_id = GetProduct_id_by_product_name(product_name)
    r = db.session.query(Test_Global_Var).filter(Test_Global_Var.product_id==product_id).count()
    return r

def GetGlobalVarList(offset, limit):
    r = db.session.query(Test_Global_Var.id, System_Product.product_name, Test_Global_Var.global_var_name,
                         Test_Global_Var.global_var_value, Test_Global_Var.is_auto_add, Test_Global_Var.global_var_explain
                         ).join(System_Product,System_Product.id == Test_Global_Var.product_id).order_by(Test_Global_Var.
                         product_id).order_by(Test_Global_Var.global_var_name).offset(offset).limit(limit).all()
    return r

def GetGlobalVarList_product_name(product_name,offset,limit):
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name==product_name).first()[0]
    r = db.session.query(Test_Global_Var.id, System_Product.product_name, Test_Global_Var.global_var_name,
                         Test_Global_Var.global_var_value,Test_Global_Var.global_var_explain).join(System_Product,
                         System_Product.id == Test_Global_Var.product_id).filter(Test_Global_Var.product_id ==
                         product_id).offset(offset).limit(limit).all()
    return r

def GetGlobalVarNameByGlobalVarId(global_var_id):
    global_var_name = db.session.query(Test_Global_Var.global_var_name).filter(Test_Global_Var.id==global_var_id).first()[0]
    return global_var_name

def JudgeGlobalVarNameIsRepeat_NC(product_name, global_var_name): # 判断全局变量名称是否重复(新增和复制新增时使用）
    product_id = GetProduct_id_by_product_name(product_name)
    case_global_var_list0 = db.session.query(Test_Global_Var.global_var_name).filter(Test_Global_Var.product_id == product_id).all()
    case_global_var_list = list(map(lambda x: x[0], case_global_var_list0))
    if global_var_name in case_global_var_list:
        return 0
    else:
        return 1

def JudgeGlobalVarNameIsRepeat_E(product_name, global_var_name): # 判断全局变量名称是否重复（编辑时使用）
    product_id = GetProduct_id_by_product_name(product_name)
    case_global_var_list0 = db.session.query(Test_Global_Var.global_var_name).filter(
        and_(Test_Global_Var.product_id == product_id, Test_Global_Var.global_var_name != global_var_name)).all()
    case_global_var_list = list(map(lambda x: x[0], case_global_var_list0))
    if global_var_name in case_global_var_list:
        return 0
    else:
        return 1

def GetIGlobalVarValueByGlobalVarId(global_var_id):
    global_var_value = db.session.query(Test_Global_Var.global_var_value).filter(Test_Global_Var.id==global_var_id).first()[0]
    return global_var_value

def GetIsAutoAddByGlobalVarId(global_var_id):
    is_auto_add = db.session.query(Test_Global_Var.is_auto_add).filter(Test_Global_Var.id==global_var_id).first()[0]
    return is_auto_add

def GetGlobalVarExplainByGlobalVarId(global_var_id):
    global_var_explain = db.session.query(Test_Global_Var.global_var_explain).filter(Test_Global_Var.id==global_var_id).first()[0]
    return global_var_explain

def DeleteGlobalVar(global_var_id):
    db.session.query(Test_Global_Var).filter(Test_Global_Var.id == global_var_id).delete()
    db.session.commit()

if __name__ == '__main__':
    print(  GetGlobalVarList(0, 5) )