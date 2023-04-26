# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.OtherDB import *
from GeneralDB.InserDB import *

def CountEncryptDecryptData():
    r = db.session.query(Test_Encrypt_Decrypt).count()
    return r

def CountEncryptDecryptData():
    r = db.session.query(Test_Encrypt_Decrypt).count()
    return r

def GetEncryptDecryptList(offset, limit):
    r = db.session.query(Test_Encrypt_Decrypt.id, Test_Encrypt_Decrypt.file_name).order_by(
        Test_Encrypt_Decrypt.id).offset(offset).limit(limit).all()
    return r

# def GetEncryptDecryptList(offset,limit):
#     r = db.session.query(Test_Encrypt_Decrypt.id,Test_Encrypt_Decrypt.file_name).offset(offset).limit(limit).all()
#     return r

def DeleteEncryptDecrypt(encrypt_decrypt_id):
    db.session.query(Test_Encrypt_Decrypt).filter(Test_Encrypt_Decrypt.id == encrypt_decrypt_id).delete()
    db.session.commit()

def GetFileNameByEncryptDecrypt(encrypt_decrypt_id):
    file_name = db.session.query(Test_Encrypt_Decrypt.file_name).filter(Test_Encrypt_Decrypt.id==encrypt_decrypt_id).first()[0]
    return file_name

def GetProductNameByEncryptDecrypt(encrypt_decrypt_id):
    product_id = db.session.query(Test_Encrypt_Decrypt.product_id).filter(Test_Encrypt_Decrypt.id==encrypt_decrypt_id).first()[0]
    product_name = db.session.query(System_Product.product_name).filter(System_Product.id==product_id).first()[0]
    # product_name = db.session.query(System_Product.product_name).join(System_Product,System_Product.id==Test_Encrypt_Decrypt.
    #                product_id).filter(Test_Encrypt_Decrypt.id==encrypt_decrypt_id).first()[0]
    return product_name

if __name__ == '__main__':
    print( GetEncryptDecryptList(0,5) )