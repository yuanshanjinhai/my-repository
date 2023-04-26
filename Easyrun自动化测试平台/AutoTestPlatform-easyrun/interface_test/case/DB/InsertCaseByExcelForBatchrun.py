# coding=utf-8
from GeneralTools.ExcelAllSheet import *
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *
from sqlalchemy import and_,desc
from interface_test.case.tools.other_tools import get_urlencode_value
import time

def InsertCaseByExcelForBatchrun(product_name,upload_case_list):
    product_id = db.session.query(System_Product.id).filter(System_Product.product_name == product_name).first()[0]
    db.session.query(Test_Case).filter(Test_Case.product_id == product_id).delete()
    db.session.query(Test_relation).filter(Test_relation.product_id==product_id).delete()
    db.session.commit()

    ins_insert = Insert_db()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for ir in range(0,len(upload_case_list)):
        if "$" not in upload_case_list[ir]["case_name"]:
            product_name = upload_case_list[ir]["product_name"]
            product_id = db.session.query(System_Product.id).filter(System_Product.product_name==product_name).first()[0]
            case_group_name = upload_case_list[ir]["case_group_name"]
            case_group_id = db.session.query(Test_Case_Group.id).filter(Test_Case_Group.case_group_name==case_group_name).first()[0]
            interface_name = upload_case_list[ir]["interface_name"]
            interface_id = db.session.query(Test_Interface.id).filter(Test_Interface.interface_name==interface_name).first()[0]
            interface_address = upload_case_list[ir]["interface_address"]
            is_relationed = upload_case_list[ir]["is_relationed"]

            case_name = upload_case_list[ir]["case_name"]
            if case_name == "None":
                case_name = None

            case_order = int(upload_case_list[ir]["case_order"])

            is_urlencode_pwd = upload_case_list[ir]["is_urlencode_unurlencode"]
            is_urlencode_pwd = get_urlencode_value(is_urlencode_pwd)

            encrypt_decrypt_file = upload_case_list[ir]["encrypt_decrypt_file"]
            if encrypt_decrypt_file == "None":
                encrypt_decrypt_file = None

            case_explain = upload_case_list[ir]["case_explain"]
            if case_explain == "None":
                case_explain = None

            header = upload_case_list[ir]["header"]
            if header == "None":
                header = None

            body = upload_case_list[ir]["body"]
            if body == "None":
                body = None

            expect_response = upload_case_list[ir]["expect_response"]
            if expect_response == "None":
                expect_response = None

            creat_time = now_time
            update_time = None


        if "$" in upload_case_list[ir]["case_name"]:
            product_name = upload_case_list[ir]["product_name"]
            product_id = db.session.query(System_Product.id).filter(System_Product.product_name == product_name).first()[0]
            is_relationed = upload_case_list[ir]["is_relationed"]
            case_name = upload_case_list[ir]["case_name"]
            relation_name = case_name
            case_group_name = upload_case_list[ir]["case_group_name"]
            case_group_id = db.session.query(Test_Case_Group.id).filter(Test_Case_Group.case_group_name == case_group_name).first()[0]
            interface_id = None
            interface_address = None

            case_order = int(upload_case_list[ir]["case_order"])
            is_urlencode_pwd = None
            encrypt_decrypt_file = None
            case_explain = None

            update_time = None
            if upload_case_list[ir]["header"] != "None":
                header = upload_case_list[ir]["header"]
                relation_field = "header"
                json_path = upload_case_list[ir]["header"]
            else:
                header = None

            if upload_case_list[ir]["body"] != "None":
                body = upload_case_list[ir]["body"]
                relation_field = "body"
                json_path = upload_case_list[ir]["body"]
            else:
                body = None

            if upload_case_list[ir]["expect_response"] != "None":
                expect_response = upload_case_list[ir]["expect_response"]
                relation_field = "expect_response"
                json_path = upload_case_list[ir]["expect_response"]
            else:
                expect_response = None

            creat_time = now_time

            data_shuliang = db.session.query(Test_Case).count()
            for ird in range(0,data_shuliang):
                case_result = db.session.query(Test_Case.id,Test_Case.case_name).filter(Test_Case.product_id==product_id).order_by(desc(Test_Case.id)).offset(ird).first()
                case_name_relation = case_result[1]
                if "$" not in case_name_relation:
                    case_id_relation = case_result[0]
                    break

            ins_insert.insert_test_relation(product_id,case_group_id,case_id_relation,relation_name,relation_field,json_path)
        ins_insert.insert_test_case(product_id, case_group_id, interface_id, interface_address, is_relationed,case_name, case_order, is_urlencode_pwd,
                                    encrypt_decrypt_file, case_explain, header, body, expect_response, creat_time,update_time)

if __name__ == '__main__':
    data_shuliang = db.session.query(Test_Case).count()
    for ird in range(0, data_shuliang):
        print('ird=',ird)
        case_result = db.session.query(Test_Case.id, Test_Case.case_name).filter(Test_Case.product_id == 1).order_by(desc(Test_Case.id)).offset(ird).first()
        print('case_result=',case_result)
        case_name = case_result[1]
        # if case_name == None or "$" not in case_name:
        #     case_id = case_result[0]
        #     break