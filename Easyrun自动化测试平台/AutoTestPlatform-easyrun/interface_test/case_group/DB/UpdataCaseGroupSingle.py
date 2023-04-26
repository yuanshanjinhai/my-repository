# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *

def UpdataCaseGroupSingle(product_name,is_run, case_group_id,case_group_name,case_group_order,case_group_type,case_group_explain):
    product_id = GetProduct_id_by_product_name(product_name)
    d = db.session.query(Test_Case_Group).filter(Test_Case_Group.id==case_group_id).first()
    d.is_run = is_run
    d.product_id = product_id
    d.case_group_name = case_group_name
    d.case_group_id = case_group_id

    old_case_group_order = db.session.query(Test_Case_Group.case_group_order).filter(Test_Case_Group.id==case_group_id).first()[0]
    if case_group_order == old_case_group_order:
        pass
    elif case_group_order > old_case_group_order:
        case_group_all_by_product = db.session.query(Test_Case_Group).filter(Test_Case_Group.product_id==product_id).all()
        for icg in case_group_all_by_product:
            if icg.case_group_order > old_case_group_order and icg.case_group_order <= case_group_order:
                icg.case_group_order -= 1
    elif case_group_order < old_case_group_order:
        case_group_all_by_product = db.session.query(Test_Case_Group).filter(Test_Case_Group.product_id == product_id).all()
        for icg in case_group_all_by_product:
            if icg.case_group_order < old_case_group_order and icg.case_group_order >= case_group_order:
                icg.case_group_order += 1

    d.case_group_order = case_group_order
    d.case_group_type = case_group_type
    d.case_group_explain = case_group_explain
    db.session.commit()

if __name__ == '__main__':
    print(UpdataCaseGroupSingle('测试系统1', '创建组', '结束组', '接口'))