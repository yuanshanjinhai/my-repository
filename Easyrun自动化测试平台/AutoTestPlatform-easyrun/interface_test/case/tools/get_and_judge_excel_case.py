# coding=utf-8
from GeneralTools.ExcelAllSheet import *
from GeneralTools.OtherTools import RemoveSpacesAndEnter
from GeneralDB.OtherDB import *
from GeneralDB.CreatDB_Test import *
from GeneralDB.CreatDB_System import *
from interface_test.case.tools.judge_update_excel_case import *

def get_and_judge_excel_case(excel_path):
    error_str = ""

    ins_excel = ExcelAllSheet(excel_path)
    sheet_list = ins_excel.get_SheetList()  # 获取sheet列表
    if "用例" not in sheet_list:
        error_str += "用例文件中必须包含“用例”sheet；"

    sheet_name = "用例"
    max_row = ins_excel.get_max_row(sheet_name)
    if ins_excel.get_value(sheet_name, "A1") != "项目名称" or \
       ins_excel.get_value(sheet_name, "B1") != "用例组名称" or \
       ins_excel.get_value(sheet_name, "C1") != "对应接口" or \
       ins_excel.get_value(sheet_name, "D1") != "接口地址" or \
       ins_excel.get_value(sheet_name, "E1") != "用例/关联名称" or \
       ins_excel.get_value(sheet_name, "F1") != "顺序" or \
       ins_excel.get_value(sheet_name, "G1") != "方法" or \
       ins_excel.get_value(sheet_name, "H1") != "编解码" or \
       ins_excel.get_value(sheet_name, "I1") != "加解密文件" or \
       ins_excel.get_value(sheet_name, "J1") != "用例说明" or \
       ins_excel.get_value(sheet_name, "K1") != "请求头" or \
       ins_excel.get_value(sheet_name, "L1") != "请求体" or \
       ins_excel.get_value(sheet_name, "M1") != "预期返回值":
       error_str += "用例标题包含错误，请与模板核对，或重新下载模板；"
    elif max_row == 1:
        error_str += "用例内容不能为空；"
    r_list = []
    row = 2
    for ir in range(2,max_row + 1):
        tem_dict = {}
        product_name = ins_excel.get_value(sheet_name,"A" + str(ir))
        case_group_name = ins_excel.get_value(sheet_name,"B" + str(ir))
        interface_name = ins_excel.get_value(sheet_name,"C" + str(ir))
        interface_address = ins_excel.get_value(sheet_name,"D" + str(ir))
        case_name = ins_excel.get_value(sheet_name,"E" + str(ir))
        case_order = ins_excel.get_value(sheet_name, "F" + str(ir))
        method = ins_excel.get_value(sheet_name, "G" + str(ir))
        is_urlencode_unurlencode = ins_excel.get_value(sheet_name,"H" + str(ir))
        encrypt_decrypt_file = ins_excel.get_value(sheet_name,"I" + str(ir))

        case_explain = ins_excel.get_value(sheet_name,"J" + str(ir))
        if case_explain == "None":
            case_explain = None

        header = ins_excel.get_value(sheet_name,"K" + str(ir))
        if header == "None":
            header = None
        else:
            header = RemoveSpacesAndEnter(header)

        body = ins_excel.get_value(sheet_name,"L" + str(ir))
        if body == "None":
            body = None
        else:
            body = RemoveSpacesAndEnter(body)

        expect_response = ins_excel.get_value(sheet_name,"M" + str(ir))
        if expect_response == "None":
            expect_response = None
        else:
            expect_response = RemoveSpacesAndEnter(expect_response)

        tem_dict["row"] = row
        tem_dict["product_name"] = product_name
        tem_dict["case_group_name"] = case_group_name
        tem_dict["interface_name"] = interface_name
        tem_dict["interface_address"] = interface_address

        tem_dict["is_relationed"] = 0
        if "$" in case_name:
            for ir1 in range(0, len(r_list))[::-1]:
                if "$" not in r_list[ir1]["case_name"]:
                    r_list[ir1]["is_relationed"] = 1
                    break

        tem_dict["case_name"] = case_name
        tem_dict["case_order"] = case_order
        tem_dict["method"] = method
        tem_dict["is_urlencode_unurlencode"] = is_urlencode_unurlencode
        tem_dict["encrypt_decrypt_file"] = encrypt_decrypt_file
        tem_dict["case_explain"] = case_explain
        tem_dict["header"] = header
        tem_dict["body"] = body
        tem_dict["expect_response"] = expect_response

        r_list.append(tem_dict)
        row += 1

    judge_r = judge_update_excel_case(r_list)
    r = error_str + judge_r
    if r == "":
        return r_list
    else:
        return r