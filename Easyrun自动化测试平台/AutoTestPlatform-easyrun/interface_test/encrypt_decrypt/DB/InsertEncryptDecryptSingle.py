# coding=utf-8
from GeneralDB.InserDB import *

def InsertEncryptDecryptSingle(file_name):
    ins_insert = Insert_db()
    ins_insert.insert_test_encrypt_decrypt(file_name)