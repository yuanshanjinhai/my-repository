# coding=utf-8
from interface_test.case_group.DB.OtherDB import *

def count_total_pages(limit):
    case_group_data_count = CountCaseGroupData()
    if case_group_data_count % limit == 0:
        total_pages = case_group_data_count // limit
    elif case_group_data_count % limit > 0:
        total_pages = case_group_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

def count_total_pages_product_name(product_name,limit):
    case_group_data_count = CountCaseGroupData_product_name(product_name)
    if case_group_data_count % limit == 0:
        total_pages = case_group_data_count // limit
    elif case_group_data_count % limit > 0:
        total_pages = case_group_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

if __name__ == '__main__':
    print(count_total_pages_product_name('测试系统1',2))