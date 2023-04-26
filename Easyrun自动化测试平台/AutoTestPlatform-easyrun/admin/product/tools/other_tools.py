# coding=utf-8
from admin.product.DB.OtherDB import *

def count_total_pages(limit):
    product_data_count = CountProductData()
    if product_data_count % limit == 0:
        total_pages = product_data_count // limit
    elif product_data_count % limit > 0:
        total_pages = product_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

if __name__ == '__main__':
    pass
