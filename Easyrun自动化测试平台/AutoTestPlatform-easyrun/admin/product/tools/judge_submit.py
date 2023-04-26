# coding = utf-8
from admin.product.DB.OtherDB import JudgeProductNameIsRepeat

def judge_submit(type, product_name, product_abbreviation, product_explain):
    error_str = ""
    if product_name == "":
        error_str += "项目名称不能为空；"
    if product_explain == "":
        error_str += "项目说明不能为空；"
    if JudgeProductNameIsRepeat(product_name) == 0 and type == "N":
        error_str += "项目名称不能重复；"
    if len(product_name) > 50:
        error_str += "项目名称不能超过50字；"
    if len(product_abbreviation) > 30:
        error_str += "项目简称不能超过30字；"
    if len(product_explain) > 1000:
        error_str += "项目说明不能超过1000字；"
    if error_str == "":
        return 1
    elif error_str != "":
        return error_str