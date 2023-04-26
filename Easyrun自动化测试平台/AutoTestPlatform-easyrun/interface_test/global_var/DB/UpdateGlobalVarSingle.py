# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *

def UpdataGlobalVarSingle(product_name,global_var_id,global_var_name,global_var_value,is_auto_add,global_var_explain):
    product_id = GetProduct_id_by_product_name(product_name)
    d = db.session.query(Test_Global_Var).filter(Test_Global_Var.id==global_var_id).first()
    d.prduct_id = product_id
    d.global_var_name = global_var_name
    d.global_var_value = global_var_value
    d.is_auto_add = is_auto_add
    d.global_var_explain = global_var_explain
    db.session.commit()

if __name__ == '__main__':
    pass