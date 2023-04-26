# coding = utf-8
from GeneralDB.CreatDB_System import *
from GeneralDB.InserDB import *

def InsertProduct(product_name,product_abbreviation,product_explain):
    ins_insert = Insert_db()
    ins_insert.insert_system_product(product_name,product_abbreviation,product_explain)