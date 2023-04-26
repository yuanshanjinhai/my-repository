# coding = utf-8
from GeneralDB.CreatDB_System import *

def UpdateProduct(product_id, product_name, product_abbreviation, product_explain):
    update_data = db.session.query(System_Product).filter(System_Product.id==product_id).first()
    update_data.product_name = product_name
    update_data.product_abbreviation = product_abbreviation
    update_data.product_explain = product_explain
    db.session.commit()