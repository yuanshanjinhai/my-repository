# coding=utf-8
import re
from interface_test.case_group.DB.OtherDB import JudgeCaseGroupNameIsRepeat_NC,JudgeCaseGroupNameIsRepeat_E,JudgeQishizuIsOnly,JudgeQishizuIsOnly_Edit,JudgeJieshuzuIsOnly,JudgejieshuzuIsOnly_Edit

def judge_submit(type,case_group_id,product_name,case_group_name,case_group_order,case_group_type,case_group_explain):
    error_str = ""
    if case_group_name == "":
        error_str += "用例组名称不能为空；"
    elif len(case_group_name) > 100:
        error_str += "用例组名称不能超100字；"
    elif ((type == "N" or type == "C") and JudgeCaseGroupNameIsRepeat_NC(product_name, case_group_name) == 0) or \
            (type == "E" and JudgeCaseGroupNameIsRepeat_E(product_name, case_group_name) == 0):
        error_str += "用例组名称不能重复；"
    if case_group_order != "AUTO":
        if re.findall(r"\d+",case_group_order) == []:
            error_str += "用例组顺序只能是0-999之间的正整数；"
        elif type == "E" and case_group_type == "并发组" and (int(case_group_order) <= 0 or int(case_group_order) >= 999):
            error_str += "并发组的用例组顺序只能是1-998之间的正整数；"
    if case_group_explain == "":
        error_str += "用例组说明不能为空；"
    elif len(case_group_explain) > 800:
        error_str += "用例组说明不能超800字；"
    if case_group_type == "起始组":
        if (type == "N" or type == "C") and JudgeQishizuIsOnly(product_name) == 0:
            error_str += "用例组类型只能存在一个起始组；"
        if type == "E" and JudgeQishizuIsOnly_Edit(case_group_type, case_group_id, product_name) == 0:
            error_str += "用例组类型只能存在一个起始组；"
        if type == "E" and case_group_order != '0':
            error_str += "起始组的用例组顺序只能是0；"
    if case_group_type == "结束组":
        if (type == "N" or type == "C") and JudgeJieshuzuIsOnly(product_name) == 0:
            error_str += "用例组类型只能存在一个结束组；"
        if type == "E" and JudgejieshuzuIsOnly_Edit(case_group_type, case_group_id, product_name) == 0:
            error_str += "用例组类型只能存在一个结束组；"
        if type == "E" and case_group_order != '999':
            error_str += "结束组的用例组顺序只能是999；"

    if error_str == "":
        return 1
    else:
        return error_str