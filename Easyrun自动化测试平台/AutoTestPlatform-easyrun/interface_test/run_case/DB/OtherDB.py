# coding=utf-8
from GeneralDB.OtherDB import *
from sqlalchemy import and_
from GeneralDB.CreatDB_Test import *

def GetProductNameList_Case_run():
    r0 = db.session.query(System_Product.product_name).all()
    r_list = [("全部项目", "全部项目")]
    for ir in r0:
        r_list.append((ir[0], ir[0]))
    return r_list

def CountCaseData():
    r = db.session.query(Test_Case).count()
    return r

def CountCaseData_product_name(product_name):
    if product_name == "全部项目":
        r = db.session.query(Test_Case).count()
    else:
        product_id = GetProduct_id_by_product_name(product_name)
        r = db.session.query(Test_Case).filter(Test_Case.product_id == product_id).count()
    return r

def GetCaseRunList(offset_, limit_):
    r0 = db.session.query(Test_Case).join(Test_Case_Group,Test_Case.case_group_id==Test_Case_Group.id).order_by(Test_Case.product_id).order_by(Test_Case_Group.case_group_order).order_by(Test_Case.case_order).offset(offset_).limit(limit_).all()
    r = []
    for ir in r0:
        id = ir.id
        product_name = db.session.query(System_Product.product_name).filter(System_Product.id == ir.product_id).first()[0]
        if len(product_name) > 10:
            product_name = product_name[0:11] + "..."

        case_group_name = db.session.query(Test_Case_Group.case_group_name).filter(Test_Case_Group.id == ir.case_group_id).first()[0]
        if len(case_group_name) > 10:
            case_group_name = case_group_name[0:11] + "..."

        case_order = ir.case_order

        if ir.interface_id != None:
            interface_name = db.session.query(Test_Interface.interface_name).filter(Test_Interface.id == ir.interface_id).first()[0]
            if len(interface_name) > 10:
                interface_name = interface_name[0:11] + "..."
        else:
            interface_name = ""

        case_name = ir.case_name
        if case_name != None and len(case_name) > 10:
            case_name = case_name[0:11] + "..."

        if ir.interface_address != None:
            interface_address = ir.interface_address
            if len(interface_address) > 100:
                interface_address = interface_address[0:101] + "..."
        else:
            interface_address = ""

        body = ir.body
        if body != None and len(body) > 100:
            body = body[0:101] + "..."

        expect_response = ir.expect_response
        if expect_response != None and len(expect_response) > 100:
            expect_response = expect_response[0:101] + "..."

        tem_tuple = (id, product_name, case_group_name, case_order, interface_name, case_name, interface_address,body, expect_response)

        r.append(tem_tuple)

    return r

def GetCaseRunList_product_name(product_name,offset_, limit_):
    if product_name == "全部项目":
        r0 = db.session.query(Test_Case).join(Test_Case_Group, Test_Case.case_group_id == Test_Case_Group.id).order_by(
            Test_Case.product_id).order_by(Test_Case_Group.case_group_order).order_by(Test_Case.case_order).offset(
            offset_).limit(limit_).all()
    else:
        product_id = db.session.query(System_Product.id).filter(System_Product.product_name == product_name).first()[0]
        r0 = db.session.query(Test_Case).join(Test_Case_Group,Test_Case.case_group_id==Test_Case_Group.id).filter(Test_Case.product_id == product_id).order_by(
        Test_Case_Group.case_group_order).order_by(Test_Case.case_order).offset(offset_).limit(limit_).all()
    r = []
    for ir in r0:
        id = ir.id
        product_name = db.session.query(System_Product.product_name).filter(System_Product.id == ir.product_id).first()[
            0]
        if len(product_name) > 10:
            product_name = product_name[0:11] + "..."

        case_group_name = db.session.query(Test_Case_Group.case_group_name).filter(Test_Case_Group.id == ir.case_group_id).first()[0]
        if len(case_group_name) > 10:
            case_group_name = case_group_name[0:11] + "..."

        case_order = ir.case_order

        interface_id = ir.interface_id
        if interface_id != None:
            interface_name = db.session.query(Test_Interface.interface_name).filter(Test_Interface.id == interface_id).first()[0]
            if interface_name != None and len(interface_name) > 10:
                interface_name = interface_name[0:11] + "..."
        else:
            interface_name = None

        case_name = ir.case_name
        if case_name != None and len(case_name) > 10:
            case_name = case_name[0:11] + "..."

        interface_address = ir.interface_address
        if interface_address != None and len(interface_address) > 100:
            interface_address = interface_address[0:101] + "..."

        body = ir.body
        if body != None and len(body) > 100:
            body = body[0:101] + "..."

        expect_response = ir.expect_response
        if expect_response != None and len(expect_response) > 100:
            expect_response = expect_response[0:101] + "..."

        tem_tuple = (id, product_name, case_group_name, case_order, interface_name, case_name, interface_address, body, expect_response)
        r.append(tem_tuple)
    return r

def GetMethod(interface_id):
    method = db.session.query(Test_Interface.method).filter(Test_Interface.id==interface_id).first()[0]
    return method

def GetRelationField(case_id,relation_name):
    relation_field = db.session.query(Test_relation.relation_field).filter(and_(Test_relation.case_id==case_id,Test_relation.relation_name==relation_name)).first()[0]
    return relation_field

def GetJsonPath(case_id,relation_name):
    json_path = db.session.query(Test_relation.json_path).filter(and_(Test_relation.case_id==case_id,Test_relation.relation_name==relation_name)).first()[0]
    return json_path

def GetRelationValue(case_id,relation_field,json_path):
    actual_response_str = db.session.query(Test_run_result.actual_response).filter(Test_run_result.case_id==case_id).first()[0]
    relation_value = eval(actual_response_str + json_path)
    return relation_value

if __name__ == '__main__':
    actual_response_str='{"a":1,"b":2}'
    json_path = '["a"]'
    relation_value = eval(actual_response_str +  json_path)
    print(relation_value)