# coding=utf-8
from GeneralDB.OtherDB import GetProduct_id_by_product_name
from GeneralDB.InserDB import *
from sqlalchemy import desc

def InsertInterfaceSingle(product_name,interface_name,interface_address,interface_method,interface_explain):
    product_id = GetProduct_id_by_product_name(product_name)
    max_interface_order_list = db.session.query(Test_Interface.interface_order).filter(
        Test_Interface.product_id == product_id).order_by(desc(Test_Interface.interface_order)).first()
    if max_interface_order_list == None:
        interface_order = 1
    else:
        interface_order = max_interface_order_list[0] + 1

    ins_insert = Insert_db()
    ins_insert.insert_test_interface(product_id,interface_name,interface_order,interface_address,interface_method,interface_explain)