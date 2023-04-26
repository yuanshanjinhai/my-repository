# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *
from sqlalchemy import and_,desc
from interface_test.case.DB.OtherDB import GetRelationListByCaseId
from interface_test.case.tools.other_tools import get_urlencode_value2

def GetCaseByDB(product_name):
    rlist = []
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name==product_name).first()[0]
    relation_name_list = []
    relation_name_r = db.session.query(Test_relation.relation_name).filter(Test_relation.product_id==product_id).all()
    for ire in relation_name_r:
        relation_name_list.append(ire[0])
    case_r = db.session.query(Test_Case).filter(Test_Case.product_id==product_id).all()
    for ic in range(0,len(case_r)):
        tem_dict = {}
        case_id = case_r[ic].id
        tem_dict['case_id'] = case_id

        tem_dict["product_name"] = product_name

        case_group_id = case_r[ic].case_group_id
        case_group_name = db.session.query(Test_Case_Group.case_group_name).filter(Test_Case_Group.id==case_group_id).first()[0]
        tem_dict['case_group_name'] = case_group_name

        interface_id = case_r[ic].interface_id
        interface_name = db.session.query(Test_Interface.interface_name).filter(Test_Interface.id==interface_id).first()
        if interface_name != None:
            interface_name = interface_name[0]
        else:
            interface_name = ""
        tem_dict['interface_name'] = interface_name

        interface_address = case_r[ic].interface_address
        tem_dict['interface_address'] = interface_address

        case_name = case_r[ic].case_name
        tem_dict['case_name'] = case_name

        case_order = case_r[ic].case_order
        tem_dict['case_order'] = case_order

        method = db.session.query(Test_Interface.method).filter(Test_Interface.id==interface_id).first()
        if method != None:
            method = method[0]
        else:
            method = ""
        tem_dict['method'] = method

        is_urlencode_pwd = case_r[ic].is_urlencode_pwd
        if is_urlencode_pwd != None:
            is_urlencode_pwd = get_urlencode_value2(str(is_urlencode_pwd))
        else:
            is_urlencode_pwd = ""
        tem_dict['is_urlencode_pwd'] = is_urlencode_pwd

        encrypt_decrypt_file = case_r[ic].encrypt_decrypt_file
        if encrypt_decrypt_file != None:
            encrypt_decrypt_file = encrypt_decrypt_file[0]
        else:
            encrypt_decrypt_file = ""
        tem_dict['encrypt_decrypt_file'] = encrypt_decrypt_file

        case_explain = case_r[ic].case_explain
        if case_explain != None:
            pass
        else:
            case_explain = ""
        tem_dict['case_explain'] = case_explain

        header = case_r[ic].header
        if header != None:
            pass
        else:
            header = ""
        tem_dict['header'] = header

        body = case_r[ic].body
        if body != None:
            pass
        else:
            body = ""
        tem_dict['body'] = body

        expect_response = case_r[ic].expect_response
        if expect_response != None:
            pass
        else:
            expect_response = ""
        tem_dict['expect_response'] = expect_response

        rlist.append(tem_dict)

    return rlist

if __name__ == '__main__':
    relation_list = GetCaseByDB('测试系统1')
    print(relation_list)