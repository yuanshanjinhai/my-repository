# coding=utf-8
import re
from interface_test.interface.DB.OtherDB import JudgeInterfaceNameIsRepeat_NC,JudgeInterfaceNameIsRepeat_E

def judge_submit(type,interface_id,product_name,interface_name,interface_order,interface_address,interface_method,interface_explain):
    error_str = ""
    if interface_name == "":
        error_str += "接口名称不能为空；"
    elif len(interface_name) > 50:
        error_str += "接口名称名称不能超50字；"
    elif ((type == "N" or type == "C") and JudgeInterfaceNameIsRepeat_NC(product_name, interface_name) == 0) or \
            (type == "E" and JudgeInterfaceNameIsRepeat_E(product_name, interface_name) == 0):
        error_str += "接口名称不能重复；"
    if interface_order != "AUTO":
        if re.findall(r"\d+",interface_order) == []:
            error_str += "接口顺序只能是正整数；"
    if interface_address == "":
        error_str += "接口地址不能为空；"
    if len(interface_address) > 500:
        error_str += "接口地址不能超过500字；"
    if interface_method == "":
        error_str += "方法不能为空；"
    if interface_explain == "":
        error_str += "接口说明不能为空；"
    elif len(interface_explain) > 800:
        error_str += "接口说明不能超600字；"

    if error_str == "":
        return 1
    else:
        return error_str