# coding=utf-8
from interface_test.global_var.DB.OtherDB import *

def count_total_pages(limit):
    global_var_data_count = CountGlobalVarData()
    if global_var_data_count % limit == 0:
        total_pages = global_var_data_count // limit
    elif global_var_data_count % limit > 0:
        total_pages = global_var_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

def count_total_pages_product_name(product_name,limit):
    global_var_data_count = CountGlobalVarData_product_name(product_name)
    if global_var_data_count % limit == 0:
        total_pages = global_var_data_count // limit
    elif global_var_data_count % limit > 0:
        total_pages = global_var_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

