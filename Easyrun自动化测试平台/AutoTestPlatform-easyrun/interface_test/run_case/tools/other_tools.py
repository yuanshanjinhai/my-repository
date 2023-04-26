# coding=utf-8
from interface_test.run_case.DB.OtherDB import CountCaseData,CountCaseData_product_name

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