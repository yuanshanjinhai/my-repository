# coding=utf-8
from GeneralTools.OtherTools import check_case
from interface_test.case.DB.OtherDB import JudgeCaseNameIsRepeat,GetRelationedHeader,GetRelationedBody,GetRelationedExpectEesponse
from interface_test.case.tools.judge_relation_single import judge_relation_single
from interface_test.case.tools.judge_global_var_single import judge_global_var_single
from GeneralDB.OtherDB import GetProduct_name_by_product_id,GetCaseGroupIdByCaseGroupName

def judge_submit(case_id,product_name,case_group_name,interface_name,method,interface_address,case_name,case_explain,header,body,expect_response,type):
    error_str = ""
    product_id = GetProduct_name_by_product_id(product_name)
    if case_group_name != None:
        case_group_id = GetCaseGroupIdByCaseGroupName(case_group_name)
    else:
        error_str += "用例组不能为空；"
    if case_name == "":
        error_str += "用例名称不能为空；"
    if case_group_name == "0":
        error_str += "用例组不能为空；"
    if interface_name == None:
        error_str += "接口不难为空；"
    if "$" not in case_name:
        if interface_name == "0":
            error_str += "接口名称不能为空；"
        if method == 0:
            error_str += "方法不能为空；"
        if interface_address == "":
            error_str += "接口地址不能为空；"
        if case_explain == "":
            error_str += "用例说明不能为空；"
        elif len(case_name) > 100:
            error_str += "用例名称不能多于100字符；"

        if type == "N" or type == "C":
            r1 = JudgeCaseNameIsRepeat(case_group_name, case_name)
            if r1 == 0:
                error_str += "同一用例组下用例名称不能重复；"

        r2 = check_case(header, body)
        if r2 != 1:
            error_str += r2

        if case_group_name != None:
            r3 = judge_relation_single(case_id,product_name, case_group_name, header, body, expect_response)
            if r3 != 1:
                error_str += r3

        r4 = judge_global_var_single(product_name,header, body, expect_response)
        if r4 != 1:
            error_str += r4

    if "$" in case_name:
        header_digit = 0
        body_digit = 0
        expect_response_digit = 0

        if header != "":
            header_digit = 1
            relationed_header_str = GetRelationedHeader(product_id,case_group_id)
            try:
                eval( str(relationed_header_str)  + '["' + header + '"]' )
            except:
                error_str += "请求头中关联路径错误；"

        if body != "":
            body_digit = 1
            relationed_body_str = GetRelationedBody(product_id,case_group_id)
            try:
                eval( str(relationed_body_str) + '["' + body + '"]' )
            except:
                error_str += "请求体中关联路径错误；"

        if expect_response != "":
            expect_response_digit = 1
            relationed_expect_response_str = GetRelationedExpectEesponse(product_id, case_group_id)
            try:
                eval( str(relationed_expect_response_str) + '["' + expect_response + '"]' )
            except:
                error_str += "预期返回值中关联路径错误；"

        hbe_digit = header_digit + body_digit + expect_response_digit
        if hbe_digit < 1:
            error_str += "没有设置关联路径；"
        if hbe_digit > 1:
            error_str += "不能出现多个关联路径；"

    if error_str == "":
        return 1
    else:
        return error_str