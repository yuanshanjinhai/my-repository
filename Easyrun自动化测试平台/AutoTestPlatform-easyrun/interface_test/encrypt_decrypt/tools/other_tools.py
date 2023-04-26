# coding=utf-8
from GeneralTools.AllPath import encrypt_decrypt_load_path0
from interface_test.encrypt_decrypt.DB.OtherDB import *
import os
import os.path

def count_total_pages(limit):
    encrypt_decrypt_data_count = CountEncryptDecryptData()
    if encrypt_decrypt_data_count % limit == 0:
        total_pages = encrypt_decrypt_data_count // limit
    elif encrypt_decrypt_data_count % limit > 0:
        total_pages = encrypt_decrypt_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

# def count_total_pages(limit):
#     encrypt_decrypt_data_count = CountEncryptDecryptData()
#     if encrypt_decrypt_data_count % limit == 0:
#         total_pages = encrypt_decrypt_data_count // limit
#     elif encrypt_decrypt_data_count % limit > 0:
#         total_pages = encrypt_decrypt_data_count // limit + 1
#     if total_pages == 0:
#         total_pages = 1
#     return total_pages

def JugeCaseFileSuffix(file_name): # 判断文件后缀是否是.py
    suffix_str = os.path.splitext(file_name)[1]
    if suffix_str == ".py":
        return 1
    else:
        return 0

def jugde_encrypt_decrypt_DirFilename_is_exist(file_name):
    for root, dir_list, file_list in os.walk(encrypt_decrypt_load_path0 ,topdown=False):
        print("file_list=",file_list)
        pass
        if file_name in file_list:
            return 0
        else:
            return 1

def delete_file(product_name,file_name):
    file_path = encrypt_decrypt_load_path0 + file_name
    os.remove(file_path)

if __name__ == '__main__':
    print(count_total_pages('测试系统1',2))