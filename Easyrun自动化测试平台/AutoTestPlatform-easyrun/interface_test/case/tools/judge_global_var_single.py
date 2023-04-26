# coding=utf-8
import re
from interface_test.case.DB.OtherDB import GetGlobalVarNameList

def judge_global_var_single0(product_name,hbe_str,type):
    error_str = ""
    global_var_list = GetGlobalVarNameList(product_name)
    re_global_var_list = re.findall(r"(?<=【)\w+\|\|\w+(?=】)", hbe_str)

    for ir in re_global_var_list:
        if ir.split("||")[1] not in global_var_list:
            if type == "h":
                relation_field_title = "请求头"
            if type == "b":
                relation_field_title  = "请求体"
            if type == "e":
                relation_field_title  = "预期返回值"
            error_str += relation_field_title + "中，全局变量" + ir[1:-1] + "不存在；"

    if error_str == "":
        return 1
    else:
        return error_str

def judge_global_var_single(product_name,header, body, expect_response):
    judge_header_r = judge_global_var_single0(product_name,header,"h")
    judge_body_r = judge_global_var_single0(product_name,body,"b")
    judge_expect_response_r = judge_global_var_single0(product_name,expect_response,"e")
    error_str = ""
    for ij in (judge_header_r, judge_body_r, judge_expect_response_r):
        if ij != 1:
            error_str += ij
    if error_str == "":
        return 1
    else:
        return error_str