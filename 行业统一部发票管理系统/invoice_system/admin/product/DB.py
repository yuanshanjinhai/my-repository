# coding=utf-8
from GeneralDB.InsertDB_System import *

def InsertProduc(product_name,product_abbreviation,product_explain):
    ins_insert = InsertDB_System()
    ins_insert.insert_system_product(product_name,product_abbreviation,product_explain)

def GetProductList():
    r_list = db.session.query(System_Product.product_name,System_Product.product_abbreviation,System_Product.product_explain).all()
    product_list = []
    for i in r_list:
        tem_dict = {"product_name":i[0],"product_abbreviation":i[1],"product_explain":i[2]}
        product_list.append(tem_dict)
    return product_list

def GetProductListByProductName(product_name):
    r_tuple = db.session.query(System_Product.product_name,System_Product.product_abbreviation,System_Product.product_explain).filter(System_Product.product_name==product_name).first()
    r_dict = {"product_name":r_tuple[0],"product_abbreviation":r_tuple[1],"product_explain":r_tuple[2]}
    return r_dict

def GetProductOneByProductId(product_id):
    r_tuple = db.session.query(System_Product.product_name,System_Product.product_abbreviation,System_Product.product_explain).filter(System_Product.id==product_id).first()
    r_dict = {"product_id":product_id,"product_name": r_tuple[0], "product_abbreviation": r_tuple[1], "product_explain": r_tuple[2]}
    return r_dict

def GetProductNameByProductId(product_id):
    product_name_q = db.session.query(System_Product.product_name).filter(System_Product.id==product_id).first()
    product_name = product_name_q[0]
    return product_name

def UpdateProduct(product_id,product_name,product_abbreviation,product_explain):
    up_queryset = db.session.query(System_Product).filter(System_Product.id==product_id).first()
    up_queryset.product_name = product_name
    up_queryset.product_abbreviation = product_abbreviation
    up_queryset.product_explain = product_explain
    db.session.commit()

if __name__ == '__main__':
    print( GetProductNameByProductId(1) )