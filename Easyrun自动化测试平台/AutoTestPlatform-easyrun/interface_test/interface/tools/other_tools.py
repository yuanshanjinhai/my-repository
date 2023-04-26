# coding=utf-8
from interface_test.interface.DB.OtherDB import *

def count_total_pages(limit):
    interface_data_count = CountInterfaceData()
    if interface_data_count % limit == 0:
        total_pages = interface_data_count // limit
    elif interface_data_count % limit > 0:
        total_pages = interface_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

def count_total_pages_product_name(product_name,limit):
    interface_data_count = CountInterfaceData_product_name(product_name)
    if interface_data_count % limit == 0:
        total_pages = interface_data_count // limit
    elif interface_data_count % limit > 0:
        total_pages = interface_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

