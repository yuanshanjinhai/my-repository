# coding=utf-8
from interface_test.case.DB.OtherDB import JudgeProducNameIsExist,JudgeCaseGroupIsExist,JudgeEncryptDecryptFileIsExist,JudgeGlobalNameIsExist,\
    GetCaseGroupOrder,GetProductIdByProductName,GetCaseGroupId,JudgeInterfaceNameIsExist,GetInterfaceIdByInterfaceName
from interface_test.case.tools.other_tools import judge_header,judge_body_expectresponse
import re

def judge_hbe(hbe_str,ir,upload_case_list,field):
    judge_hbe_error_str = ""
    global_relation_list = re.findall(r"【\S+?】",str(hbe_str))
    for igr in global_relation_list:
        zhongkuohao_geshi = 0
        re_r0 = re.findall(r"【\+\S+\|\|\S+】", igr)
        if re_r0 != []:
            zhongkuohao_geshi = 1
            re_r = re_r0[0]
            global_name = re_r[1:-1].split("||")[1]
            if JudgeGlobalNameIsExist(global_name) == 1:
                pass
            else:
                judge_hbe_error_str += "第" + str(upload_case_list[ir]["row"]) + "行" + field + "字段中的" + re_r + "中的全局变量名称不存在；"
        if re.findall(r"【d】]",igr) != []:
            zhongkuohao_geshi = 1
        if re.findall(r"【d\d+】",igr) != []:
            zhongkuohao_geshi = 1
        if re.findall(r"【ad】",igr) != []:
            zhongkuohao_geshi = 1
        if re.findall(r"【ad\d+】",igr) != []:
            zhongkuohao_geshi = 1
        if re.findall(r"【时间\d】",igr) != []:
            zhongkuohao_geshi = 1
        re_r = re.findall(r"【\$\S+】",igr)
        if re_r != []:
            zhongkuohao_geshi = 1
            relation_name = re_r[2:-1]
            relation_name_is_exist = 0
            for ir1 in range(0,ir)[::-1]:
                if "$" in upload_case_list[ir1]["case_name"]:
                    relation_nameed = upload_case_list[ir1]["case_name"][1::]
                    # case_group_order = GetCaseGroupOrder(upload_case_list[ir]["product_id"],upload_case_list[ir]["case_group_name"])
                    case_group_ordered = GetCaseGroupOrder(upload_case_list[ir1]["product_id"],upload_case_list[ir1]["case_group_name"])
                    if case_group_ordered == None: # 如果被关联用例组不存在，就不必再判断下去了，跳出循环去判断下一条用例
                        break
                    if (relation_nameed == relation_name and upload_case_list[ir]["case_group_name"]==upload_case_list[ir1]["case_group_name"]) or \
                            (relation_nameed == relation_name and case_group_ordered==0):
                        relation_name_is_exist = 1
                        break
            if relation_name_is_exist == 0 and re_r0 != []:
                judge_hbe_error_str += "第" + str(upload_case_list[ir]["row"]) + "行" + field + "字段中的" + re_r + "中的关联名称不存在；"
        if zhongkuohao_geshi == 0 and re_r0 != []:
            judge_hbe_error_str += "第" + str(upload_case_list[ir]["row"]) + "行" + field + "字段中的" + re_r + "格式错误；"
    if judge_hbe_error_str == "":
        return 1
    else:
        return judge_hbe_error_str

def judge_update_excel_case(upload_case_list):
    error_str = ""
    for ir in range(0,len(upload_case_list)):
        if "$" not in upload_case_list[ir]["case_name"]:
            product_name = upload_case_list[ir]['product_name']
            print('product_name=',upload_case_list[ir]["row"],product_name,type(product_name),upload_case_list[ir]["case_explain"])
            if product_name == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，项目名称不能为空；"
            else:
                if JudgeProducNameIsExist(upload_case_list[ir]['product_name']) == 0:
                    error_str += "第" + str(upload_case_list[ir]["row"]) + "行，项目名称不存在；"
                    continue
                else:
                    product_id = GetProductIdByProductName(product_name)
                    upload_case_list[ir]["product_id"] = product_id

            case_group_name = upload_case_list[ir]['case_group_name']
            if case_group_name == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例组不能为空；"
            else:
                if product_name != "None":
                    if JudgeCaseGroupIsExist(upload_case_list[ir]['product_id'],upload_case_list[ir]['case_group_name']) == 0:
                        error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例组不存在；"
                    else:
                        case_group_id = GetCaseGroupId(product_id,case_group_name)
                        upload_case_list[ir]["case_group_id"] = case_group_id

            interface_name = upload_case_list[ir]["interface_name"]
            if interface_name == "":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，对应接口不能为空；"
            else:
                if JudgeInterfaceNameIsExist(product_id,interface_name) == 0:
                    error_str += "第" + str(upload_case_list[ir]["row"]) + "行，对应接口不存在；"
                else:
                    interface_id = GetInterfaceIdByInterfaceName(product_id,interface_name)
                    upload_case_list[ir]["interface_id"] = interface_id

            if upload_case_list[ir]['interface_address'] == "":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，接口地址不能为空；"
            if upload_case_list[ir]['case_name'] == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例名称不能为空；"
            if upload_case_list[ir]['case_order'] == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例顺序不能为空；"
            if re.findall(r"\d+",upload_case_list[ir]['case_order']) == []:
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例顺序必须为整型数字；"
            else:
                if re.findall(r"\d+",upload_case_list[ir]['case_order']) != []:
                    if upload_case_list[ir]["row"] == 2:
                        if upload_case_list[ir]["case_order"] != "1":
                            error_str += "第" + str(upload_case_list[ir]["row"]) + "行，首行用例的顺序必需从1开始；"
                    else:
                        if upload_case_list[ir]["case_group_name"] != upload_case_list[ir-1]["case_group_name"]:
                            if upload_case_list[ir]["case_order"] != "1":
                                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例组内首条用例的顺序必需从1开始；"
                        elif upload_case_list[ir]["case_group_name"] == upload_case_list[ir-1]["case_group_name"]:
                            if int(upload_case_list[ir]["case_order"]) != int(upload_case_list[ir-1]["case_order"])+1:
                                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例顺序不连续；"
            if upload_case_list[ir]["method"] == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，方法不能为空；"
            if upload_case_list[ir]["is_urlencode_unurlencode"] == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，编解码不能为空；"
            if upload_case_list[ir]["is_urlencode_unurlencode"] == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，编解码不能为空；"

            if (upload_case_list[ir]["is_urlencode_unurlencode"] == "加密-解密" or upload_case_list[ir]["is_urlencode_unurlencode"] =="url编码-加密-解密-url解码") \
                    and upload_case_list[ir]["encrypt_decrypt_file"] == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，加解密文件不能为空；"
            else:
                if (upload_case_list[ir]["is_urlencode_unurlencode"] == "加密-解密" or upload_case_list[ir]["is_urlencode_unurlencode"] =="url编码-加密-解密-url解码") \
                    and upload_case_list[ir]["encrypt_decrypt_file"] != "None":
                    encrypt_decrypt_file = upload_case_list[ir]["encrypt_decrypt_file"]
                    if JudgeEncryptDecryptFileIsExist(encrypt_decrypt_file) == 0:
                        error_str += "第" + str(upload_case_list[ir]["row"]) + "行，加解密文件不存在；"
            # if upload_case_list[ir]["case_explain"] == "None":
            #     error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例说明不能为空；"

            if upload_case_list[ir]["header"] != None:
                judge_header_result = judge_header(upload_case_list[ir]["row"], upload_case_list[ir]["header"])
                if judge_header_result != 1:
                    error_str += judge_header_result
                judge_header_r = judge_hbe(upload_case_list[ir]["header"], ir, upload_case_list, "header")
                if judge_header_r != 1:
                    error_str += judge_header_r

            if upload_case_list[ir]["body"] != None:
                print('upload_case_list[ir]["row"]=',upload_case_list[ir]["row"])
                print('upload_case_list[ir]["body"]=',upload_case_list[ir]["body"],type(upload_case_list[ir]["body"]))
                judge_body_eepectresponse_result = judge_body_expectresponse(upload_case_list[ir]["row"], upload_case_list[ir]["body"],"body")
                if judge_body_eepectresponse_result != 1:
                    error_str += judge_body_eepectresponse_result
                judge_body_r = judge_hbe(upload_case_list[ir]["body"], ir, upload_case_list, "body")
                if judge_body_r != 1:
                    error_str += judge_body_r

            if upload_case_list[ir]["expect_response"] != "None":
                judge_body_eepectresponse_result = judge_body_expectresponse(upload_case_list[ir]["row"], upload_case_list[ir]["expect_response"],"expect_response")
                if judge_body_eepectresponse_result != 1:
                    error_str += judge_body_eepectresponse_result
                judge_expect_response_r = judge_hbe(upload_case_list[ir]["expect_response"], ir, upload_case_list, "expect_response")
                if judge_expect_response_r != 1:
                    error_str += judge_expect_response_r

        elif "$" in upload_case_list[ir]["case_name"]:
            if upload_case_list[ir]["row"] == 2:
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，关联不能出现在第一行；"
            if upload_case_list[ir]["case_group_name"] != upload_case_list[ir - 1]["case_group_name"]:
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，关联不能出现在用例组内第一行；"
            product_name = upload_case_list[ir]['product_name']
            if product_name == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，项目名称不能为空；"
            else:
                if JudgeProducNameIsExist(upload_case_list[ir]['product_name']) == 0:
                    error_str += "第" + str(upload_case_list[ir]["row"]) + "行，项目名称不存在；"
                    continue
                else:
                    product_id = GetProductIdByProductName(product_name)
                    upload_case_list[ir]["product_id"] = product_id

            case_group_name = upload_case_list[ir]['case_group_name']
            if case_group_name == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例组不能为空；"
            else:
                if JudgeCaseGroupIsExist(upload_case_list[ir]['product_id'],
                                         upload_case_list[ir]['case_group_name']) == 0:
                    error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例组不存在；"
                else:
                    case_group_id = GetCaseGroupId(product_id, case_group_name)
                    upload_case_list[ir]["case_group_id"] = case_group_id

            if re.findall(r"\$\S+",upload_case_list[ir]["case_name"]) == []:
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，关联名称格式错误；"
            if upload_case_list[ir]['case_order'] == "None":
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例顺序不能为空；"
            if re.findall(r"\d+", upload_case_list[ir]['case_order']) == []:
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例顺序必须为整型数字；"
            elif re.findall(r"\d+", upload_case_list[ir]['case_order']) != []:
                if upload_case_list[ir]["row"] == 2:
                    if upload_case_list[ir]["case_order"] != "1":
                        error_str += "第" + str(upload_case_list[ir]["row"]) + "行，首行用例的顺序必需从1开始；"
                else:
                    if upload_case_list[ir]["case_group_name"] != upload_case_list[ir - 1]["case_group_name"]:
                        if upload_case_list[ir]["case_order"] != "1":
                            error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例组内首条用例的顺序必需从1开始；"
                    elif upload_case_list[ir]["case_group_name"] == upload_case_list[ir - 1]["case_group_name"]:
                        if int(upload_case_list[ir]["case_order"]) != int(
                                upload_case_list[ir - 1]["case_order"]) + 1:
                            error_str += "第" + str(upload_case_list[ir]["row"]) + "行，用例顺序不连续；"
            if upload_case_list[ir]["header"] == None:
                h = 0
            else:
                h = 1
            if upload_case_list[ir]["body"] == None:
                b = 0
            else:
                b = 1
            if upload_case_list[ir]["expect_response"] == None:
                e = 0
            else:
                e = 1
            if h + b + e == 0:
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，未设置关联；"
            if h + b + e > 1:
                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，关联只能来自一个字段；"
            if h + b + e == 1:
                if upload_case_list[ir]["header"] != None:
                    path = upload_case_list[ir]["header"]
                    for tem_ir in range(0,ir)[::-1]:
                        if "$" not in upload_case_list[tem_ir]["header"]:
                            try:
                                r = eval(upload_case_list[tem_ir]["header"] + path)
                            except:
                                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，路径错误；"
                            break
                if upload_case_list[ir]["body"] != None:
                    path = upload_case_list[ir]["body"]
                    for tem_ir in range(ir, 0)[::-1]:
                        if "$" not in upload_case_list[tem_ir]["body"]:
                            try:
                                r = eval(upload_case_list[tem_ir]["body"] + path)
                            except:
                                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，路径错误；"
                            break
                if upload_case_list[ir]["expect_response"] != None:
                    path = upload_case_list[ir]["expect_response"]
                    for tem_ir in range(ir, 0)[::-1]:
                        if "$" not in upload_case_list[tem_ir]["expect_response"]:
                            try:
                                r = eval(upload_case_list[tem_ir]["expect_response"] + path)
                            except:
                                error_str += "第" + str(upload_case_list[ir]["row"]) + "行，路径错误；"
                            break

            relation_name_list = []
            for tem_ir1 in range(0,ir)[::-1]:
                relation_nameed = upload_case_list[tem_ir1]["case_name"]
                if relation_nameed != upload_case_list[tem_ir1+1]["case_name"]:
                    break
                if "$" in relation_nameed:
                    relation_nameed = relation_nameed[1::]
                    relation_name_list.append(relation_nameed)
            if relation_name_list != []:
                if case_group_name not in relation_name_list:
                    error_str += "第" + str(upload_case_list[ir]["row"]) + "行，关联名称不能重复；"
    print("error_str=",error_str)

    if error_str == "":
        return ""
    else:
        return error_str
