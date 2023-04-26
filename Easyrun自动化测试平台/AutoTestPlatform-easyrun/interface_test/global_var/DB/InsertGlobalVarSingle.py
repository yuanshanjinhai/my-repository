# coding=utf-8
from GeneralDB.OtherDB import GetProduct_id_by_product_name
from GeneralDB.InserDB import *
from sqlalchemy import desc

def InsertGlobalVarSingle(product_name,global_var_name,global_var_value,is_auto_add,global_var_explain):
    product_id = GetProduct_id_by_product_name(product_name)

    ins_insert = Insert_db()
    ins_insert.insert_test_global_var(product_id,global_var_name,global_var_value,is_auto_add,global_var_explain)