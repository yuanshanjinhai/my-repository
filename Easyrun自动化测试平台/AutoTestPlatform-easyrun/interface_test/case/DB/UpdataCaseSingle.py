# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.CreatDB_Test import *

def UpdataCaseSingle(product_name,case_group_name,interface_name,interface_address,case_name,case_order,is_urlencode_pwd,encrypt_decrypt_file,case_explain,header,body,expect_response,case_id):
    product_id = GetProduct_id_by_product_name(product_name)
    case_group_id = db.session.query(Test_Case_Group.id).filter(Test_Case_Group.case_group_name == case_group_name)
    interface_id = db.session.query(Test_Interface.id).filter(Test_Interface.interface_name == interface_name)
    update_object = db.session.query(Test_Case).filter(Test_Case.id==case_id).first()
    update_object.product_id = product_id
    update_object.case_group_id = case_group_id
    update_object.interface_id = interface_id
    update_object.interface_address = interface_address
    update_object.case_name = case_name

    old_case_order = db.session.query(Test_Case.case_order).filter(Test_Case.id == case_id).first()[0]
    if case_order == old_case_order:
        pass
    elif case_order > old_case_order:
        case_all_by_product = db.session.query(Test_Case).filter(Test_Case.product_id == product_id).all()
        for icg in case_all_by_product:
            if icg.case_order > old_case_order and icg.case_order <= case_order:
                icg.case_order -= 1
    elif case_order < old_case_order:
        case_all_by_product = db.session.query(Test_Case).filter(Test_Case.product_id == product_id).all()
        for icg in case_all_by_product:
            if icg.case_order < old_case_order and icg.case_order >= case_order:
                icg.case_order += 1

    update_object.case_order = case_order
    update_object.is_urlencode_pwd = is_urlencode_pwd
    update_object.encrypt_decrypt_file = encrypt_decrypt_file
    update_object.case_explain = case_explain
    update_object.header = header
    update_object.body = body
    update_object.expect_response = expect_response
    db.session.commit()