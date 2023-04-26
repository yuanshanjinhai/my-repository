# coding = utf-8
from GeneralDB.CreatDB_System import *

def DeleteProduct(product_id):
    db.session.query(System_Product).filter(System_Product.id==product_id).delete()
    db.session.commit()