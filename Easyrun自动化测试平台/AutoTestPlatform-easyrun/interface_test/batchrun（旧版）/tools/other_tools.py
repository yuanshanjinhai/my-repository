# coding = utf-8
import os
import re
import json
from GeneralTools.AllPath import *
from GeneralTools.OtherTools import *
from GeneralTools.ExcelAllSheet import *

def JugeCaseFileSuffix(file_name): # 判断文件后缀是否是xlsx
    suffix_str = os.path.splitext(file_name)[1]
    if suffix_str == ".xlsx":
        return 1
    else:
        return 0

def change_shuangyinhao(aim_str): # 把字符串里的单引号变成双引号
    r_str = ""
    for ia in aim_str:
        if ia != "'":
            r_str += ia
        elif ia == "'":
            r_str += '"'
    return r_str

def get_global_value_list(ins_excel,global_key0):
    max_row = ins_excel.get_max_row("全局变量")
    for ir in range(2,max_row):
        global_key = ins_excel.get_value("全局变量","A" + str(ir))
        if global_key == global_key0:
            return ins_excel.get_value("全局变量","B" + str(ir))
    return 0

def get_global_value(excel_case_path,global_key):
    ins_excel = ExcelAllSheet(excel_case_path)
    max_row = ins_excel.get_max_row("全局变量")
    for ir in range(2,max_row+1):
        global_key0 = ins_excel.get_value("全局变量","A" + str(ir))
        if global_key0 == global_key:
            global_value = ins_excel.get_value("全局变量","B" + str(ir))
            return global_value

def IntoExcel(excel_row,excel_path,actual_respone,contrast_r):
    ins_excel = ExcelAllSheet(excel_path)
    sheet_list = ins_excel.get_SheetList()  # 获取第一个sheet的名称
    case_sheet = "用例"
    ins_excel.write_content(case_sheet,"J"+str(excel_row),actual_respone)
    if contrast_r == 0:
        ins_excel.write_content(case_sheet,"K"+str(excel_row),"否")
    elif contrast_r == 1:
        ins_excel.write_content(case_sheet, "K" + str(excel_row), "是")
    ins_excel.save_content()

def delete_run_result(excel_path):
    ins_excel = ExcelAllSheet(excel_path)
    max_row = ins_excel.get_max_row("用例")
    for ir in range(2,max_row+1):
        ins_excel.write_content("用例", "J" + str(ir), "")
        ins_excel.write_content("用例", "K" + str(ir), "")
    ins_excel.save_content()

def ContrastExAndAu(expect_response_str,actual_respone_str):
    if expect_response_str == actual_respone_str:
        return 1
    else:
        return 0

if __name__ == '__main__':
    pass