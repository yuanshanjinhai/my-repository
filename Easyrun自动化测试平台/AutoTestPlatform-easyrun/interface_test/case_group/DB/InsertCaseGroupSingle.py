# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *
from sqlalchemy import desc

def InsertCaseGroupSingle(product_name,is_run,case_group_name,case_group_type,case_group_explain):
    product_id = GetProduct_id_by_product_name(product_name)
    if case_group_type == "起始组":
        case_group_order = 0
    elif case_group_type == "结束组":
        case_group_order = 999
    elif case_group_type == "并发组":
        case_group_order_list = db.session.query(Test_Case_Group.case_group_order).filter(
            Test_Case_Group.product_id == product_id).order_by(desc(Test_Case_Group.case_group_order)).all()
        if case_group_order_list == []:
            case_group_order = 1
        elif case_group_order_list[0] == (999,):
            case_group_order = case_group_order_list[1][0] + 1
        elif case_group_order_list[0] != (999,):
            case_group_order = case_group_order_list[0][0] + 1
    ins_insert = Insert_db()
    ins_insert.insert_test_case_group(product_id,is_run,case_group_name,case_group_order,case_group_type,case_group_explain)

if __name__ == '__main__':
    print(InsertCaseGroupSingle('测试系统1', '创建组', '结束组', '接口'))