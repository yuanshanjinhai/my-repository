# coding=utf-8
from GeneralDB.OtherDB import *
from sqlalchemy import and_,or_,desc
from GeneralDB.CreatDB_Test import *

def GetProductNameList_TestCaseList():
    r0 = db.session.query(System_Product.product_name).all()
    r_list = [("全部项目","全部项目")]
    for ir in r0:
        r_list.append((ir[0],ir[0]))
    return r_list

def GetProductNameList():
    r0 = db.session.query(System_Product.product_name).all()
    r_list = []
    for ir in r0:
        r_list.append((ir[0],ir[0]))
    return r_list

def GetCaseList(offset_, limit_):
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

def GetCaseList_product_name(product_name,offset_, limit_):
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

def GetCaseGroupList(product_name):
    if product_name == "全部项目":
        case_group_list0 = db.session.query(Test_Case_Group.case_group_name).all()
    else:
        product_id = db.session.query(System_Product.id).filter(System_Product.product_name==product_name).first()[0]
        case_group_list0 = db.session.query(Test_Case_Group.case_group_name).filter(Test_Case_Group.product_id==product_id).all()
    case_group_list = []
    for ic in case_group_list0:
        case_group_list.append((ic[0],ic[0]))
    return case_group_list

def GetInterfaceList(product_name):
    if product_name == "全部项目":
        interface_list0 = db.session.query(Test_Interface.interface_name).all()
    else:
        product_id = db.session.query(System_Product.id).filter(System_Product.product_name == product_name).first()[0]
        interface_list0 = db.session.query(Test_Interface.interface_name).filter(Test_Interface.product_id==product_id).all()
    interface_list = []
    for iin in interface_list0:
        interface_list.append((iin[0],iin[0]))
    return interface_list

def GetMefhod(product_name,interface):
    product_id = GetProduct_id_by_product_name(product_name)
    r = db.session.query(Test_Interface.method).filter(and_(Test_Interface.product_id==product_id,Test_Interface.interface_name==interface)).first()
    return r[0]

def GetInterfaceAddress(product_name,interface_name):
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name == product_name).first()[0]
    r = db.session.query(Test_Interface.interface_address).filter(and_(Test_Interface.product_id==product_id,Test_Interface.interface_name==interface_name)).first()
    return r[0]

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

def GetOneDataList(id):
    r = db.session.query(Test_Case).filter(Test_Case.id==id).all()[0]

    product_id = r.product_id
    product_name = db.session.query(System_Product.product_name).filter(System_Product.id==product_id).first()[0]

    case_group_id = r.case_group_id
    case_group_name = db.session.query(Test_Case_Group.case_group_name).filter(Test_Case_Group.id==case_group_id).first()[0]

    case_name = r.case_name

    interface_id = r.interface_id
    if interface_id == None:
        interface_name = None
    else:
        interface_name = db.session.query(Test_Interface.interface_name).filter(Test_Interface.id==interface_id).first()[0]

    method = db.session.query(Test_Interface.method).filter(Test_Interface.id==interface_id).first()
    if method != None:
        method = method[0]

    interface_address = r.interface_address

    case_order = r.case_order

    is_urlencode_pwd = r.is_urlencode_pwd

    encrypt_decrypt_file = r.encrypt_decrypt_file

    case_explain = r.case_explain

    header = r.header

    body = r.body

    expect_response = r.expect_response

    creat_time = r.creat_time
    update_time = r.update_time

    r1 = (product_name,case_group_name,interface_name,method,interface_address,case_name,case_order,is_urlencode_pwd,
          encrypt_decrypt_file,case_explain,header,body,expect_response,creat_time,update_time)
    return r1

def JudgeCaseNameIsRepeat(case_group_name,case_name):
    r = db.session.query(Test_Case.case_name).join(Test_Case_Group,Test_Case_Group.id==Test_Case.case_group_id).filter(Test_Case_Group.case_group_name==case_group_name).all()
    if r == None:
        return 1
    elif (case_name,) in r:
        return 0
    elif (case_name,)  not in r:
        return 1

def GetIsUrlencodePwd(case_id):
    r = db.session.query(Test_Case.is_urlencode_pwd).filter(Test_Case.id==case_id).first()[0]
    return r

def GetEncryptDecryptFile(case_id):
    r = db.session.query(Test_Case.encrypt_decrypt_file).filter(Test_Case.id==case_id).first()[0]
    return r

def JudgeProducNameIsExist(product_name):
    product_name_list = []
    product_name_list0 = db.session.query(System_Product.product_name).all()
    for ip in product_name_list0:
        product_name_list.append(ip[0])
    if product_name in product_name_list:
        return 1
    else:
        return 0

def GetProductIdByProductName(product_name):
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name == product_name).first()[0]
    return product_id

def JudgeCaseGroupIsExist(product_id,case_group_name):
    case_group_group_list = []
    case_group_list0 = db.session.query(Test_Case_Group.case_group_name).join(System_Product,System_Product.id==Test_Case_Group.product_id).filter(System_Product.id==product_id).all()
    for ic in case_group_list0:
        case_group_group_list.append(ic[0])
    if case_group_name in case_group_group_list:
        return 1
    else:
        return 0

def GetCaseGroupId(product_id,case_group_name):
    case_group_id = db.session.query(Test_Case_Group.id).filter(and_(Test_Case_Group.product_id==product_id,Test_Case_Group.case_group_name==case_group_name)).first()[0]
    return case_group_id

def JudgeInterfaceNameIsExist(product_id,interface_name):
    interface_name_list = []
    r = db.session.query(Test_Interface.interface_name).filter(Test_Interface.product_id==product_id).all()
    for ir in r:
        interface_name_list.append(ir[0])
    if interface_name in interface_name_list:
        return 1
    else:
        return 0

def GetInterfaceIdByInterfaceName(product_id,interface_name):
    r = db.session.query(Test_Interface.id).filter(and_(Test_Interface.product_id==product_id,Test_Interface.interface_name==interface_name)).first()[0]
    return r

def JudgeEncryptDecryptFileIsExist(encrypt_decrypt_file):
    print("encrypt_decrypt_file=",encrypt_decrypt_file)
    encrypt_decrypt_file_list = []
    r = db.session.query(Test_Encrypt_Decrypt.file_name).all()
    for ir in r:
        encrypt_decrypt_file_list.append(ir[0])
    print("encrypt_decrypt_file_list=",encrypt_decrypt_file_list)
    if encrypt_decrypt_file in encrypt_decrypt_file_list:
        return 1
    else:
        return 0

def JudgeGlobalNameIsExist(global_name0):
    global_name_list = []
    r = db.session.query(Test_Global_Var.global_var_name).all()
    for ir in r:
        global_name_list.append(ir[0])
    if global_name0 in global_name_list:
        return 1
    else:
        return 0

def GetCaseGroupOrder(product_id,case_group_name):
    case_group_order = db.session.query(Test_Case_Group.case_group_order).filter(and_(Test_Case_Group.product_id==product_id,Test_Case_Group.case_group_name==case_group_name)).first()
    if case_group_order == None:
        return None
    else:
        case_group_order = case_group_order[0]
    return case_group_order

def GetRelationListByCaseId(case_id):
    relation_list = []
    relation_list0 = db.session.query(Test_relation).filter(Test_relation.case_id==case_id).all()

    for ir in relation_list0:
        tem_dict = {}
        product_id = ir.product_id
        product_name = db.session.query(System_Product.product_name).filter(System_Product.id==product_id).first()[0]
        tem_dict['product_name'] = product_name

        case_group_name = db.session.query(Test_Case_Group.case_group_name).join(Test_Case,Test_Case_Group.id==Test_Case.case_group_id).filter(Test_Case.id==case_id).first()[0]
        tem_dict['case_group_name'] = case_group_name

        tem_dict['interface_name'] = ""

        tem_dict['interface_address'] = ""
        case_name = db.session.query(Test_Case.case_name).filter(Test_Case.id==case_id).first()[0]
        tem_dict['case_name'] = case_name
        case_order = db.session.query(Test_Case.case_order).filter(Test_Case.id==case_id).first()[0]
        tem_dict['case_order'] = case_order
        tem_dict['is_urlencode_pwd'] = ""
        tem_dict['encrypt_decrypt_file'] = ""
        tem_dict['case_explain'] = ""

        relation_field = ir.relation_field
        json_path = ir.json_path
        if relation_field == "header":
            tem_dict['header'] = json_path
            tem_dict['body'] = ""
            tem_dict['expect_response'] = ""

        if relation_field == "body":
            tem_dict['body'] = json_path
            tem_dict['header'] = ""
            tem_dict['expect_response'] = ""

        if relation_field == "expect_response":
            tem_dict['expect_response'] = json_path
            tem_dict['body'] = ""
            tem_dict['header'] = ""

        relation_list.append(tem_dict)

    return relation_list

def GetCaseGroup0RelationNameList():
    r = []
    r0 = db.session.query(Test_relation.relation_name).filter(Test_relation.case_group_id==0).all()
    for ir in r0:
        r.append(ir[0])
    return r

def GetCaseGroupList(product_name):
    if product_name == '全部项目':
        r = None
    product_id = GetProduct_id_by_product_name(product_name)
    r = []
    r0 = db.session.query(Test_Case_Group.case_group_name).filter(Test_Case_Group.product_id==product_id).all()
    for ir in r0:
        r.append((ir[0],ir[0]))
    print('r=',r)
    return r

def GetRelationNameList(product_name,case_group_id):
    product_id = GetProduct_id_by_product_name(product_name)
    rlist = []
    case_group_relation_name_list0 = db.session.query(Test_relation.relation_name).filter(or_(Test_relation.product_id==product_id,Test_relation.case_group_id==0,and_(Test_relation.product_id==product_id,Test_relation.case_group_id==case_group_id))).all()
    for ic in case_group_relation_name_list0:
        rlist.append(ic[0])
    return rlist

def GetRelationedHeader(product_id,case_group_id):
    relationed_header = db.session.query(Test_Case.header).filter(and_(Test_Case.product_id==product_id,Test_Case.case_group_id==case_group_id)).first()[0]
    return relationed_header

def GetRelationedBody(product_id,case_group_id):
    relationed_body = db.session.query(Test_Case.body).filter(and_(Test_Case.product_id==product_id,Test_Case.case_group_id==case_group_id)).first()[0]
    return relationed_body

def GetRelationedExpectEesponse(product_id,case_group_id):
    relationed_expect_response = db.session.query(Test_Case.expect_response).filter(and_(Test_Case.product_id==product_id,Test_Case.case_group_id==case_group_id)).first()[0]
    return relationed_expect_response

def GetGlobalVarNameList(product_name):
    product_id = GetProduct_name_by_product_id(product_name)
    global_var_list0 = db.session.query(Test_Global_Var.global_var_name).filter(Test_Global_Var.product_id==product_id).all()
    global_var_list = []
    for ig in global_var_list0:
        global_var_list.append(ig[0])
    return global_var_list

def JudgeCaseIsRelationed(case_id):
    case_name = db.session.query(Test_Case.case_name).filter(Test_Case.id==case_id).first()[0]
    if "$" in case_name:
        return 0
    case_order = db.session.query(Test_Case.case_order).filter(Test_Case.id==case_id).first()[0]
    product_id = db.session.query(Test_Case.product_id).filter(Test_Case.id==case_id).first()[0]
    case_group_id = db.session.query(Test_Case.case_group_id).filter(Test_Case.id==case_id).first()[0]
    case_order_max = db.session.query(Test_Case.case_order).filter(and_(Test_Case.product_id==product_id,Test_Case.case_group_id==case_group_id)).order_by(desc(Test_Case.case_order)).first()[0]
    if case_order == case_order_max:
        return 0
    if case_order <= case_order_max:
        case_name = db.session.query(Test_Case.case_name).filter(and_(Test_Case.product_id==product_id,Test_Case.case_group_id==case_group_id,Test_Case.case_order==case_order+1)).first()[0]
        if "$" in case_name:
            return 1
    return 0

def GetProductIdByCaseId(case_id):
    r = db.session.query(Test_Case.product_id).filter(Test_Case.id==case_id).first()
    product_id = r[0]
    return product_id

if __name__ == '__main__':
    # r = GetRelationNameList(98,2)

    print( GetProductIdByCaseId(7) )