# coding=utf-8
import re
from GeneralDB.OtherDB import GetProduct_id_by_product_name
from interface_test.case.DB.OtherDB import GetCaseGroupId,GetRelationNameList

def judge_relation_single0(case_id,product_name,case_group,hbe_str,type):
    error_str = ""
    product_id = GetProduct_id_by_product_name(product_name)
    case_group_id = GetCaseGroupId(product_id,case_group)
    relation_name_list = GetRelationNameList(product_name, case_group_id)
    re_list = list(set(re.findall(r"(?<=【)\$\S+?(?=】)",hbe_str)))

    for ir in re_list:
        if ir not in relation_name_list:
            if type == "h":
                relation_field = "请求头"
            if type == "b":
                relation_field = "请求体"
            if type == "e":
                relation_field = "预期返回值"
            error_str += relation_field + "中，关联函数" + ir + "在所在用例组或起始组中不存在；"

    if error_str == "":
        return 1
    else:
        return error_str

def judge_relation_single(case_id,product_name,case_group,header,body,expect_response):
    print('case_group1=',case_group)
    judge_header_r = judge_relation_single0(case_id,product_name,case_group,header,"h")
    judge_body_r = judge_relation_single0(case_id,product_name,case_group,body,"b")
    judge_expect_response_r = judge_relation_single0(case_id,product_name,case_group,expect_response,"e")
    error_str = ""
    for ij in (judge_header_r,judge_body_r,judge_expect_response_r):
        if ij != 1:
            error_str += ij
    if error_str == "":
        return 1
    else:
        return error_str