# coding=utf-8
from GeneralTools.ExcelAllSheet import *

def into_excel_by_DB(data_list,excel_path):
    ins_excel = ExcelAllSheet(excel_path)
    sheet_name = "用例"
    ins_excel.make_sheet(sheet_name)
    ins_excel.write_content(sheet_name, "A1", "项目名称")
    ins_excel.write_content(sheet_name, "B1", "用例组名称")
    ins_excel.write_content(sheet_name, "C1", "对应接口")
    ins_excel.write_content(sheet_name, "D1", "接口地址")
    ins_excel.write_content(sheet_name, "E1", "用例/关联名称")
    ins_excel.write_content(sheet_name, "F1", "顺序")
    ins_excel.write_content(sheet_name, "G1", "方法")
    ins_excel.write_content(sheet_name, "H1", "编解码")
    ins_excel.write_content(sheet_name, "I1", "加解密文件")
    ins_excel.write_content(sheet_name, "J1", "用例说明")
    ins_excel.write_content(sheet_name, "K1", "请求头")
    ins_excel.write_content(sheet_name, "L1", "请求体")
    ins_excel.write_content(sheet_name, "M1", "预期返回值")
    ins_excel.save_content()

    max_row = ins_excel.get_max_row("用例")
    for ir in range(2,max_row+1):
        ins_excel.write_content(sheet_name, "A" + str(ir), "")
        ins_excel.write_content(sheet_name, "B" + str(ir), "")
        ins_excel.write_content(sheet_name, "C" + str(ir), "")
        ins_excel.write_content(sheet_name, "D" + str(ir), "")
        ins_excel.write_content(sheet_name, "E" + str(ir), "")
        ins_excel.write_content(sheet_name, "F" + str(ir), "")
        ins_excel.write_content(sheet_name, "G" + str(ir), "")
        ins_excel.write_content(sheet_name, "H" + str(ir), "")
        ins_excel.write_content(sheet_name, "I" + str(ir), "")
        ins_excel.write_content(sheet_name, "J" + str(ir), "")
        ins_excel.write_content(sheet_name, "K" + str(ir), "")
        ins_excel.write_content(sheet_name, "L" + str(ir), "")
        ins_excel.write_content(sheet_name, "M" + str(ir), "")
    ins_excel.save_content()

    row = 2
    for ida in data_list:
        ins_excel.write_content(sheet_name, "A"+str(row), ida["product_name"])
        ins_excel.write_content(sheet_name, "B"+str(row), ida["case_group_name"])
        ins_excel.write_content(sheet_name, "C"+str(row), ida["interface_name"])
        ins_excel.write_content(sheet_name, "D"+str(row), ida["interface_address"])
        ins_excel.write_content(sheet_name, "E"+str(row), ida["case_name"])
        ins_excel.write_content(sheet_name, "F"+str(row), ida["case_order"])
        print("ida=",ida)
        ins_excel.write_content(sheet_name, "G"+str(row), ida["method"])
        ins_excel.write_content(sheet_name, "H"+str(row), ida["is_urlencode_pwd"])
        ins_excel.write_content(sheet_name, "I"+str(row), ida["encrypt_decrypt_file"])
        ins_excel.write_content(sheet_name, "J"+str(row), ida["case_explain"])
        ins_excel.write_content(sheet_name, "K"+str(row), ida["header"])
        ins_excel.write_content(sheet_name, "L"+str(row), ida["body"])
        ins_excel.write_content(sheet_name, "M"+str(row), ida["expect_response"])
        row += 1
    ins_excel.save_content()