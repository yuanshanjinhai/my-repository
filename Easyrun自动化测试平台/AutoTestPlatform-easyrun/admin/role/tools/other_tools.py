# coding=utf-8
from admin.role.DB.OtherDB import *

def count_total_pages(limit):
    user_data_count = CountRoleData()
    if user_data_count % limit == 0:
        total_pages = user_data_count // limit
    elif user_data_count % limit > 0:
        total_pages = user_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

def working_resource_str(resource_str0):
    resource_list = resource_str0.split("；")
    if "interface-singlerun" in resource_list and 'interface-interface' in resource_list and 'interface-case_group' in resource_list and \
            'interface-global' in resource_list and 'interface-encypt_decypt' in resource_list and 'interface-case' and \
            'interface-batchrun（旧版）' in resource_list and 'interface-result' and 'interface-singlerun' in resource_list:
        resource_list.append('interface')
    if  'tools-creat_boundart' in resource_list and  'tools-str_len' in resource_list:
        resource_list.append("tools")
    if  'admin-user' in resource_list and 'admin-role' in resource_list:
        resource_list.append("admin")
    return resource_list

def judge_submit(type, role_name, creat_resource_list):
    error_str = ""
    if role_name == "":
        error_str += "角色名称不能为空；"
    if role_name in GetRoleNameList() and type == "N":
        error_str += "角色名称不能重复；"
    if role_name == "超级管理员":
        error_str += "角色名称不能叫做超级管理员；"
    if len(role_name) > 50:
        error_str += "角色名称不能超过50字；"
    all_resource_list = GetAllResourceList()
    is_space = 0
    for ic in creat_resource_list:
        if ic == "" or " " in ic:
            is_space = 1
        elif ic not in all_resource_list:
            error_str += ic + "模块不存在；"
    if is_space == 1:
        error_str += "资源列表中不能出现空值；"
    if error_str == "":
        return 1
    else:
        return error_str
