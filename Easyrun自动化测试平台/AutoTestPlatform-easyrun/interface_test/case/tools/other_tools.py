# coding=utf-8
from interface_test.case.DB.OtherDB import *
import os
import os.path
from openpyxl import Workbook
from GeneralTools.AllPath import UploadCaseFile_path

def count_total_pages(limit):
    case_data_count = CountCaseData()
    if case_data_count % limit == 0:
        total_pages = case_data_count // limit
    elif case_data_count % limit > 0:
        total_pages = case_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

def count_total_pages_product_name(product_name,limit):
    case_data_count = CountCaseData_product_name(product_name)
    if case_data_count % limit == 0:
        total_pages = case_data_count // limit
    elif case_data_count % limit > 0:
        total_pages = case_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

def JugeCaseFileSuffix(file_name): # 判断文件后缀是否是xlsx
    suffix_str = os.path.splitext(file_name)[1]
    if suffix_str == ".xlsx":
        return 1
    else:
        return 0

def judge_dir_is_exist(product_name):
    if os.makedirs(UploadCaseFile_path + product_name) == 1:
        return 1
    else:
        return 0

def judge_header(ir,header_str):
    error_str = ""
    try:
        header_dict = eval(header_str)
        for j, k in header_dict.items():
            if isinstance(k, str) != 1:
                error_str += "第" + str(ir) + "行,请求头的" + str(j) + "键对应的值必须是字符串类型；"
    except:
        error_str += "第" + str(ir) + "行，请求头不是键值对；"
    if error_str == "":
        return 1
    else:
        return error_str

def judge_body_expectresponse(ir,ber_str0,type):
    error_str = ""
    if "'" in ber_str0 and type == "body":
        error_str += "第" + str(ir) + "行，请求体不能出现单引号；"
    if "'" in ber_str0 and type == "expect_response":
        error_str += "第" + str(ir) + "行，预期返回值不能出现单引号；"
    ber_str = ""
    for ib in ber_str0:
        if ib == "\\":
            continue
        ber_str += ib
    try:
        ber_dict = eval(ber_str)
    except:
        if type == "body":
            error_str += "第" + str(ir) + "行，请求体不是json类型；"
        if type == "expect_response":
            error_str += "第" + str(ir) + "行，预期返回值不是json类型；"
    if error_str == "":
        return 1
    else:
        return error_str

def get_urlencode_value(key):
    is_urlencode_pwd_dict = {'无':0,"url编码-url解码":1,"加密-解密":2,"url编码-加密-解密-url解码":3,"仅url编码":4,"仅url解码":5}
    value = is_urlencode_pwd_dict[key]
    return value

def get_urlencode_value2(key):
    is_urlencode_pwd_dict = {"0":"无", "1":"url编码-url解码", "2":"加密-解密", "3":"url编码-加密-解密-url解码", "4":"仅url编码", "5":"仅url解码"}
    value = is_urlencode_pwd_dict[key]
    return value

def creat_excel(excel_path):
    wb = Workbook()
    wb.save(excel_path)


if __name__ == '__main__':
    print(count_total_pages_product_name('测试系统2',5))