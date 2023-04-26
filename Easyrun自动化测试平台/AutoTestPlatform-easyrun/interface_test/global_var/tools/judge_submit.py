# coding=utf-8
import re
from interface_test.global_var.DB.OtherDB import JudgeGlobalVarNameIsRepeat_NC,JudgeGlobalVarNameIsRepeat_E

def judge_submit(type,global_var_id,product_name,global_var_name,global_var_value,is_auto_add,global_var_explain):
    error_str = ""
    if global_var_name == "":
        error_str += "全局变量名称不能为空；"
    elif len(global_var_name) > 50:
        error_str += "全局变量名称名称不能超50字；"
    elif ((type == "N" or type == "C") and JudgeGlobalVarNameIsRepeat_NC(product_name, global_var_name) == 0) or \
            (type == "E" and JudgeGlobalVarNameIsRepeat_E(product_name, global_var_name) == 0):
        error_str += "全局变量名称不能重复；"
    if global_var_value == "":
        error_str += "全局变量值不能为空；"
    if len(global_var_value) > 300:
        error_str += "全局变量值不能超过300字；"
    if global_var_explain == "":
        error_str += "全局变量说明不能为空；"
    elif len(global_var_explain) > 500:
        error_str += "全局变量说明不能超500字；"
    if is_auto_add == "是":
        if re.findall(r"\d+",global_var_value) == []:
            error_str += "自增的全局变量的值必须为整型类型；"

    if error_str == "":
        return 1
    else:
        return error_str