# coding=utf-8
from GeneralDB.OtherDB import *
from sqlalchemy import and_
from GeneralDB.CreatDB_Test import *

def GlobalAdd(product_name):
    product_id = GetProduct_id_by_product_name(product_name)
    global_var_id_list = db.session.query(Test_Global_Var.id).filter(and_(Test_Global_Var.product_id==product_id,Test_Global_Var.is_auto_add=="是")).all()
    for ir in global_var_id_list:
        global_var_id = ir[0]
        this_data = db.session.query(Test_Global_Var).filter(Test_Global_Var.id==global_var_id).first()
        this_data.global_var_value = int(this_data.global_var_value)+1
    db.session.commit()
    return 1

if __name__ == '__main__':
    r= GlobalAdd(1)
    print(r)