# coding=utf-8
from GeneralDB.OtherDB import *
from sqlalchemy import and_
from GeneralDB.CreatDB_Test import *

def GetGlobalVarValue(product_id,global_var_name):
    print('product_id=',product_id,type(product_id))
    print('global_var_name=',global_var_name,type(global_var_name))
    global_var_tuple = db.session.query(Test_Global_Var.global_var_value,Test_Global_Var.is_auto_add).filter(and_(Test_Global_Var.product_id==product_id,Test_Global_Var.global_var_name==global_var_name)).first()

    global_var_value = global_var_tuple[0]
    if global_var_tuple[1] == '是':
        global_var_value = int(global_var_value)
        update_object = db.session.query(Test_Global_Var.is_auto_add).filter(and_(Test_Global_Var.product_id==product_id,Test_Global_Var.global_var_name==global_var_name)).first()
        update_object.global_var_value = str(global_var_value + 1)
        db.session.commit()
        global_var_value = str(global_var_value)
    return global_var_value

if __name__ == '__main__':
    print(GetGlobalVarValue(2, 'G1'))