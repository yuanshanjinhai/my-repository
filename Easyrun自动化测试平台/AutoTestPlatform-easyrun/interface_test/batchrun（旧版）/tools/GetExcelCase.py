# coding=utf-8
from GeneralTools.ExcelAllSheet import *
from GeneralTools.AllPath import UploadCaseFile_path
import os

def GetExcelCase(file_name): # 从Excel中读出用例，并将用例做成这种形式：[[((),(),()),((),())],[((),()),((),(),(),)]]，每一个内嵌列表代表一个用例组，元组里面是用例的所有字段
    excel_path = os.path.join(UploadCaseFile_path,file_name)
    ins_excel = ExcelAllSheet(excel_path)
    # sheet_list = ins_excel.get_SheetList()  # 获取第一个sheet的名称
    case_sheet = "用例"
    max_row = ins_excel.get_max_row(case_sheet)
    case_group_list = []
    all_case_list = []
    for ir in range(2,max_row + 1):
        excel_row = ir
        is_run = ins_excel.get_value(case_sheet, "A" + str(ir))
        case_group = ins_excel.get_value(case_sheet,"B"+str(ir))
        address = ins_excel.get_value(case_sheet,"D"+str(ir))
        method = ins_excel.get_value(case_sheet,"F"+str(ir))
        header = ins_excel.get_value(case_sheet,"G"+str(ir))
        body = ins_excel.get_value(case_sheet,"H"+str(ir))
        expect_response = ins_excel.get_value(case_sheet,"I"+str(ir))

        case_tuple = (excel_row,is_run,case_group,address,method,header,body,expect_response)
        case_group_list.append(case_tuple)
        if ir != max_row:
            case_group_next = ins_excel.get_value(case_sheet,"B"+str(ir+1))
            if case_group == case_group_next:
                continue
            elif case_group != case_group_next:
                all_case_list.append(case_group_list)
                case_group_list = []
        elif ir == max_row:
            all_case_list.append(case_group_list)
    return all_case_list