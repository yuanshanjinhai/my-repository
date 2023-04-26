# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.OtherDB import *
from sqlalchemy import and_

def GetCaseGroupList(offset_, limit_):
    r = db.session.query(Test_Case_Group.id, Test_Case_Group.is_run, System_Product.product_name, Test_Case_Group.case_group_name, Test_Case_Group.case_group_order,
                         Test_Case_Group.case_group_type, Test_Case_Group.case_group_explain).join(System_Product,System_Product.id==Test_Case_Group.
                         product_id).order_by(System_Product.id).order_by(Test_Case_Group.case_group_order).offset(offset_).limit(limit_).all()
    return r

def GetCaseGroupList_product_name(product_name,offset_,limit_):
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name==product_name).first()[0]
    r = db.session.query(Test_Case_Group.id, Test_Case_Group.is_run,System_Product.product_name, Test_Case_Group.case_group_name, Test_Case_Group.case_group_order,
                         Test_Case_Group.case_group_type, Test_Case_Group.case_group_explain).join(System_Product,System_Product.id==Test_Case_Group.
                         product_id).filter(Test_Case_Group.product_id == product_id).order_by(Test_Case_Group.case_group_order).offset(offset_).limit(limit_).all()
    return r

def CountCaseGroupData():
    r = db.session.query(Test_Case_Group).count()
    return r

def CountCaseGroupData_product_name(product_name):
    product_id = GetProduct_id_by_product_name(product_name)
    r = db.session.query(Test_Case_Group).filter(Test_Case_Group.product_id==product_id).count()
    return r

def JudgeQishizuIsOnly(product_name):
    product_id = GetProduct_id_by_product_name(product_name)
    qishizu = db.session.query(Test_Case_Group.case_group_type).filter(and_(Test_Case_Group.product_id==product_id,Test_Case_Group.case_group_type=="起始组")).first()
    if qishizu == None:
        return 1
    else:
        return 0

def JudgeJieshuzuIsOnly(product_name):
    product_id = GetProduct_id_by_product_name(product_name)
    jieshuzu = db.session.query(Test_Case_Group.case_group_type).filter(and_(Test_Case_Group.product_id==product_id,Test_Case_Group.case_group_type=="结束组")).first()
    if jieshuzu == None:
        return 1
    else:
        return 0

def JudgeQishizuIsOnly_Edit(input_case_group_type,case_group_id,product_name):
    exist__case_group_type = db.session.query(Test_Case_Group.case_group_type).filter(Test_Case_Group.id==case_group_id).first()[0]
    if exist__case_group_type == input_case_group_type:
        return 1
    if exist__case_group_type != input_case_group_type:
        product_id = GetProduct_id_by_product_name(product_name)
        qishizu = db.session.query(Test_Case_Group.case_group_type).filter(and_(Test_Case_Group.product_id == product_id, Test_Case_Group.case_group_type == "起始组")).first()
    if qishizu == None:
        return 1
    else:
        return 0

def JudgejieshuzuIsOnly_Edit(input_case_group_type,case_group_id,product_name):
    exist__case_group_type = db.session.query(Test_Case_Group.case_group_type).filter(Test_Case_Group.id == case_group_id).first()[0]
    if exist__case_group_type == input_case_group_type:
        return 1
    if exist__case_group_type != input_case_group_type:
        product_id = GetProduct_id_by_product_name(product_name)
        jieshuzu = db.session.query(Test_Case_Group.case_group_type).filter(and_(Test_Case_Group.product_id == product_id, Test_Case_Group.case_group_type == "结束组")).first()
    if jieshuzu == None:
        return 1
    else:
        return 0

def JudgeCaseGroupNameIsRepeat_NC(product_name,case_group_name): # 判断用例组名称是否重复（新增和复制新增时使用）
    product_id = GetProduct_id_by_product_name(product_name)
    case_group_name_list0 = db.session.query(Test_Case_Group.case_group_name).filter(Test_Case_Group.product_id==product_id).all()
    case_group_name_list = list(map(lambda x:x[0],case_group_name_list0))
    if case_group_name in case_group_name_list:
        return 0
    else:
        return 1

def JudgeCaseGroupNameIsRepeat_E(product_name,case_group_name): # 判断用例组名称是否重复（编辑时使用）
    product_id = GetProduct_id_by_product_name(product_name)
    case_group_name_list0 = db.session.query(Test_Case_Group.case_group_name).filter(
        and_(Test_Case_Group.product_id == product_id, Test_Case_Group.case_group_name != case_group_name)).all()
    case_group_name_list = list(map(lambda x: x[0], case_group_name_list0))
    if case_group_name in case_group_name_list:
        return 0
    else:
        return 1

def GetCaseGroupNameByCaseGroupId(case_group_id):
    case_group_name = db.session.query(Test_Case_Group.case_group_name).filter(Test_Case_Group.id==case_group_id).first()[0]
    return case_group_name

def GetCaseGroupOrder(case_group_id):
    case_group_order = db.session.query(Test_Case_Group.case_group_order).filter(Test_Case_Group.id==case_group_id).first()[0]
    return case_group_order

def GetCaseGroupType(case_group_id):
    case_group_type = db.session.query(Test_Case_Group.case_group_type).filter(Test_Case_Group.id==case_group_id).first()[0]
    return case_group_type

def GetCaseGroupExplain(case_group_id):
    case_group_explain = db.session.query(Test_Case_Group.case_group_explain).filter(Test_Case_Group.id == case_group_id).first()[0]
    return case_group_explain

def DeleteCaseGroup(case_group_id):
    db.session.query(Test_Case_Group).filter(Test_Case_Group.id==case_group_id).delete()
    db.session.commit()

def GetCaseGroupTypeByCaseGroupId(case_group_id):
    case_group_type = db.session.query(Test_Case_Group.case_group_type).filter(Test_Case_Group.id==case_group_id).first()[0]
    return case_group_type

if __name__ == '__main__':
    r0=GetCaseGroupList(0, 5)
    print(r0)