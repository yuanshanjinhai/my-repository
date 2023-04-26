# coding=utf-8
import os

def JugeExcel(file_name):
    allowed_ext_list = [".xlsx", ".xls"]  # 允许上传的后缀列表
    ext = os.path.splitext(file_name)[1].lower() # 获取后缀并转成小写
    if ext in allowed_ext_list:
        return 1
    else:
        return 0

def get_ext(file_name): # 获取文件后缀
    ext = os.path.splitext(file_name)[1].lower()  # 获取后缀并转成小写
    return ext
