# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *

def UpdataInterfaceSingle(product_name,interface_id,interface_name,interface_order,interface_address,interface_method,interface_explain):
    product_id = GetProduct_id_by_product_name(product_name)
    d = db.session.query(Test_Interface).filter(Test_Interface.id==interface_id).first()
    d.prduct_id = product_id
    d.interface_name = interface_name

    old_interface_order = db.session.query(Test_Interface.interface_order).filter(Test_Interface.id==interface_id).first()[0]
    if interface_order == old_interface_order:
        pass
    elif interface_order > old_interface_order:
        interface_all_by_product = db.session.query(Test_Interface).filter(Test_Interface.product_id==product_id).all()
        for icg in interface_all_by_product:
            if icg.interface_order > old_interface_order and icg.interface_order <= interface_order:
                icg.interface_order -= 1
    elif interface_order < old_interface_order:
        interface_all_by_product = db.session.query(Test_Interface).filter(Test_Interface.product_id == product_id).all()
        for icg in interface_all_by_product:
            if icg.interface_order < old_interface_order and icg.interface_order >= interface_order:
                icg.interface_order += 1

    d.interface_order = interface_order
    d.interface_address = interface_address
    d.method = interface_method
    d.interface_explain = interface_explain
    db.session.commit()

if __name__ == '__main__':
    print(UpdataInterfaceSingle('测试系统1', '创建组', '结束组', '接口'))