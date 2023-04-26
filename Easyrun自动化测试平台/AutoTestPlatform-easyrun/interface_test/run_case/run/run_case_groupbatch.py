# coding = utf-8
import gevent
from gevent import monkey
from interface_test.run_case.DB.OtherDB import GetRelationField,GetJsonPath,GetRelationValue
from interface_test.run_case.DB.IntoRunResult import *
from interface_test.run_case.run.run_request_get_response import *
from interface_test.run_case.DB.OtherDB import GetMethod
from interface_test.run_case.tools.Replace_HBE import *
from interface_test.run_case.tools.judge_case_run_is_right import *

def run_case_groupbatch_one_case_list(one_case_group_list,run_time): # 真正的被用于协程的执行用例函数，执行结果被回写到Excel
    print('one_case_group_list=',one_case_group_list)
    for ioc in one_case_group_list:
        # for ioc in one_case_list: # 循环执行每一个用例组，注意每个用例组里的值，除了case_id是int外，其他都是str
        case_id = ioc['case_id']
        case_name = ioc['case_name']
        product_id = ioc['product_id']
        interface_id = ioc['interface_id']
        method = GetMethod(interface_id)
        interface_address = ioc['interface_address']
        is_relationed = ioc['is_relationed']
        is_urlencode_pwd = ioc['is_urlencode_pwd']
        encrypt_decrypt_file = ioc['encrypt_decrypt_file']
        header = ioc['header']
        if header != "None":
            header = RemoveSpacesAndEnter(header)
            header = Replace_HBE(product_id,header,None,0) # 转换，把里面的【】转换成相应数据，返回的格式是字符串
            # header = json.loads(header)
        body = ioc['body']
        if body != "None":
            body = RemoveSpacesAndEnter(body)
            print('HBE开始')
            body = Replace_HBE(product_id,body,None,0) # 转换，把里面的【】转换成相应数据，返回的格式是字符串
            print('HEB结束')
        client = requests.Session()
        client.keep_alive = True
        expect_response = ioc['expect_response']
        expect_response = RemoveSpacesAndEnter(expect_response)
        actual_response = run_request_get_response(interface_address, method, header, body)
        print('actual_response0=',actual_response.status_code)
        if actual_response.status_code != 200:
            actual_response = str(actual_response.status_code)
        actual_response = RemoveSpacesAndEnter(actual_response)
        expect_response = Replace_HBE(product_id, expect_response, actual_response, 0)
        print('expect_response0=',expect_response)

        judge_r = judge_case_run_is_right(expect_response, actual_response)
        if judge_r == 1:
            is_pass = '是'
        if judge_r == 0:
            is_pass = '否'
        print('case_id=',case_id)
        print('actual_response=',actual_response)
        print('is_pass=',is_pass)
        print('run_time=',run_time)
        IntoRunResult(case_id, actual_response, run_time, is_pass)

        if "$" in case_name:
            pass

    gevent.sleep(0)

def run_case_groupbatch(run_case_groupbatch,run_time): # 自动切换协程执行用例的函数，其中all_case_list的形式为[[((),(),()),((),())],[((),()),((),(),(),)]]，内嵌列表为用例组
    print("协程开始")
    monkey.patch_all()
    xiecheng_list=[]
    for i_group_list in run_case_groupbatch:
        r = gevent.spawn(run_case_groupbatch_one_case_list,i_group_list,run_time)
        xiecheng_list.append(r)
    gevent.joinall(xiecheng_list)