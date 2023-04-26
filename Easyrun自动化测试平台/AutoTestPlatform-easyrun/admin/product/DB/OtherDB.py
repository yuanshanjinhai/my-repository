# coding = utf-8
from GeneralDB.CreatDB_System import *
from GeneralDB.CreatDB_Test import *

def CountProductData():
    r = db.session.query(System_Product).count()
    return r

def GetProductList(offset, limit):
    r = db.session.query(System_Product).offset(offset).limit(limit).all()
    return r

def SearchGetProductList(product_name, offset, limit):
    r = db.session.query(System_Product).filter(System_Product.product_name.like('%'+ product_name + '%')).offset(offset).limit(limit).all()
    return r

def GetProductName(product_id):
    product_name = db.session.query(System_Product.product_name).filter(System_Product.id==product_id).first()[0]
    return product_name

def GetProductAbbreviation(product_id):
    product_abbreviation = db.session.query(System_Product.product_abbreviation).filter(System_Product.id==product_id).first()[0]
    return product_abbreviation

def GetProductExplain(product_id):
    product_explain = db.session.query(System_Product.product_explain).filter(System_Product.id==product_id).first()[0]
    return product_explain

def JudgeProductNameIsRepeat(product_name):
    product_name_list = []
    product_name_r = db.session.query(System_Product.product_name).all()
    for ip in product_name_r:
        product_name_list.append(ip[0])
    if product_name not in product_name_list:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print( JudgeProductNameIsRepeat("测试系统3") )