# coding=utf-8
from interface_test.run_case.DB.OtherDB import GetRelationField,GetJsonPath,GetRelationValue
from interface_test.run_case.run.encrypt_decrypt import *
from interface_test.run_case.tools.Replace_HBE import *
from interface_test.run_case.run.run_request_get_response import *
from interface_test.run_case.DB.IntoRunResult import *
from interface_test.run_case.tools.judge_case_run_is_right import *

def run_case_groupstart_and_end(case_groupstart_list,run_time):
    # start_relation_dict = {}
    for ic in case_groupstart_list:
        case_id = ic['case_id']
        case_name = ic['case_name']
        product_id = ic['product_id']
        interface_address = ic['interface_address']
        method = ic['method']
        encrypt_decrypt_file = ic['encrypt_decrypt_file']
        is_urlencode_pwd = ic['is_urlencode_pwd']
        encrypt_decrypt_file = ['encrypt_decrypt_file']
        header = ic['header']
        if header != None:
            header = Replace_HBE(product_id,header,None,0)
        body = ic['body']
        expect_response = ic['expect_response']
        expect_response = RemoveSpacesAndEnter(expect_response)

        if "$" not in case_name:
            body = Replace_HBE(product_id,body,None,0)
            print('body=',body)
            if is_urlencode_pwd == "1" or is_urlencode_pwd == "3":
                body = parse.quote(body)
            if is_urlencode_pwd == "2" or is_urlencode_pwd == "3":
                body = encrypt(encrypt_decrypt_file,body)
            actual_response = run_request_get_response(interface_address, method, header, body)
            if is_urlencode_pwd == "2" or is_urlencode_pwd == "3":
                actual_response = decrypt(encrypt_decrypt_file,actual_response)
            if is_urlencode_pwd == "1" or is_urlencode_pwd == "3":
                actual_response = parse.unquote(actual_response)
            actual_response = actual_response.text
            actual_response = RemoveSpacesAndEnter(actual_response)
            print('expect_responseHBE=',expect_response)
            expect_response = Replace_HBE(product_id, expect_response, actual_response, 0)
            print('expect_response0=',expect_response)
            judge_r = judge_case_run_is_right(expect_response, actual_response)
            if judge_r == 1:
                is_pass = '是'
            if judge_r == 0:
                is_pass = '否'
            print('is_pass=',is_pass)
            print('run_time=',run_time)
            IntoRunResult(case_id, actual_response, run_time, is_pass)
        if "$" in case_name:
            pass

# a = [("0", "无"), ("1", "url编码-url解码"), ("2", "加密-解密"),
# ("3", "url编码-加密-解密-url解码"), ("4", "仅url编码"), ("5", "仅url解码")]