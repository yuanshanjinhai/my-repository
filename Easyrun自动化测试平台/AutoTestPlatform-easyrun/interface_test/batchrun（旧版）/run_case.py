# coding = utf-8
import gevent
from gevent import monkey
import requests
import json
from GeneralTools.UrlcodeAndPwd import *
from interface_test.batchrun.tools.ReplaceHeaderBodyExpectresponse import *
from interface_test.batchrun.tools.other_tools import IntoExcel,ContrastExAndAu
from GeneralTools.OtherTools import *

def run_case(username,one_case_list,excel_case_path,is_urldecode): # 真正的被用于协程的执行用例函数，执行结果被回写到Excel
    for ioc in one_case_list: # 循环执行每一个用例组，注意每个用例组里的值，除了case_id是int外，其他都是str
        case_row = ioc[0]
        print("case_row=", case_row)
        is_run = ioc[1]
        if is_run == "否" or is_run == "$":
            continue
        case_group = ioc[2]
        address = ioc[3]
        address = ReplaceHeaderBodyExpectresponse(excel_case_path,username,address,"a",0) # 转换，把里面的【】转换成相应数据，返回的格式是字符串
        method = ioc[4]
        header = ioc[5]
        if header != "None":
            header = "".join(RemoveSpaces(header).split("\n"))
            header = ReplaceHeaderBodyExpectresponse(excel_case_path,username,header,"a",0) # 转换，把里面的【】转换成相应数据，返回的格式是字符串
            header = json.loads(header)
        body = ioc[6]
        if body != "None":
            body = "".join(RemoveSpaces(body).split("\n"))
            body = ReplaceHeaderBodyExpectresponse(excel_case_path,username,body,"a",0) # 转换，把里面的【】转换成相应数据，返回的格式是字符串
            print("body=",body)
            body = json.loads(body)  # 先转成字典
            body = json.dumps(body)  # 再转成json
        client = requests.Session()
        client.keep_alive = True
        print("body=",body)
        expect_response_str = ioc[7]

        if method == "POST":
            if header != "None":
                client.headers = header
                if body != "None":
                    try:
                        actual_respone = client.post(address, headers=header, data = body)
                    except:
                        actual_respone = client.post(address, headers=header, json = body)
                elif body == "None":
                    actual_respone = client.post(address, headers=header)

            elif header == "None":
                if body != "None":
                    try:
                        actual_respone = client.post(address, data = body)
                    except:
                        actual_respone = client.post(address, json = body)
                elif body == "None":
                    actual_respone = client.post(address)

        elif method == "GET":
            if header != "None":
                client.headers = header
                actual_respone = client.get(address, headers=header)
            elif header == "None":
                actual_respone = client.get(address)

        if actual_respone.status_code != 200:
            IntoExcel(case_row,excel_case_path,str(actual_respone.text),0) # 最后一个值代表是否通过，通过就为1，不通过就为0
        elif actual_respone.status_code == 200:
            actual_respone_str0 = json.dumps(actual_respone.json(), sort_keys=True, indent=4, separators=(",", ": "), ensure_ascii=False)
            expect_response_str = "".join(RemoveSpaces(expect_response_str).split("\n"))
            actual_respone_str = "".join(RemoveSpaces(actual_respone_str0).split("\n"))
            if is_urldecode == "y":
                actual_respone_str = urlencode(actual_respone_str)
            expect_response_str = ReplaceHeaderBodyExpectresponse(excel_case_path,username, expect_response_str, actual_respone_str,0)  # 转换，把里面的【】转换成相应数据，返回的格式是字符串
            contrast_r = ContrastExAndAu(expect_response_str,actual_respone_str) # 比较预期返回值和实际返回值
            IntoExcel(case_row,excel_case_path,actual_respone_str0,contrast_r)
    gevent.sleep(0)

def RunCase(all_case_list,username,excel_case_path,is_urldecode): # 自动切换协程执行用例的函数，其中all_case_list的形式为[[((),(),()),((),())],[((),()),((),(),(),)]]，内嵌列表为用例组
    print("协程开始")
    monkey.patch_all()
    xiecheng_list=[]
    for ia in all_case_list:
        r = gevent.spawn(run_case,username,ia,excel_case_path,is_urldecode)
        xiecheng_list.append(r)
    gevent.joinall(xiecheng_list)