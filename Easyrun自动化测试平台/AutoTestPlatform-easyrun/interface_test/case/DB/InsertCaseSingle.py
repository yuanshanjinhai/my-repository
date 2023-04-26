# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *
from sqlalchemy import and_,desc
import time

def InsertCaseSingle(product_name,case_group_name,interface_name,interface_address,case_name,is_urlencode_pwd,encrypt_decrypt_file,case_explain,header,body,expect_response):
    product_id = GetProduct_id_by_product_name(product_name)
    case_group_id = db.session.query(Test_Case_Group.id).filter(Test_Case_Group.case_group_name==case_group_name)
    interface_id = db.session.query(Test_Interface.id).filter(Test_Interface.interface_name==interface_name)
    is_relationed = 0

    case_order_max = db.session.query(Test_Case.case_order).filter(and_(Test_Case.product_id==product_id,Test_Case.
                                                                        case_group_id==case_group_id)).order_by(desc(Test_Case.case_order)).first()
    if case_order_max == None:
        case_order = 1
    else:
        case_order = case_order_max[0] + 1

    creat_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    update_time = None

    ins_insert = Insert_db()
    ins_insert.insert_test_case(product_id,case_group_id,interface_id,interface_address,is_relationed,case_name,case_order,is_urlencode_pwd,
                                encrypt_decrypt_file,case_explain,header,body,expect_response,creat_time,update_time)