# coding=utf-8
from GeneralTools.ExcelAllSheet import *
from GeneralTools.OtherTools import HeaderValueIsUnStr,RemoveSpacesAndEnter
from interface_test.batchrun.tools.check_ShuangShuXian import *
from interface_test.batchrun.tools.CheckIsGuanlianedRight import *
from interface_test.batchrun.tools.other_tools import change_shuangyinhao
import json

def check_case(excel_path):
    error_str = ""
    ins_excel = ExcelAllSheet(excel_path)
    sheet_list = ins_excel.get_SheetList() # 获取sheet列表
    if sheet_list == []:
        error_str += "sheet为空；"
        return error_str
    if "用例" not in sheet_list or "全局变量" not in sheet_list:
        error_str += "sheet错误，应包含至少两个sheet，'全局变量'和'用例'；"
    case_sheet = "用例"
    # global_sheet = "全局变量"

    max_row = ins_excel.get_max_row(case_sheet) # 获取最大行
    for ir in range(2,max_row+1):
        if ins_excel.get_value(case_sheet,"A"+str(ir)) == "None":
            error_str += "第"+str(ir)+"行,是否执行不能为空；"
        elif ins_excel.get_value(case_sheet,"A"+str(ir)) == "否":
            continue
        elif ins_excel.get_value(case_sheet,"A"+str(ir)) == "$":
            case_group = ins_excel.get_value(case_sheet,"B"+str(ir))
            if case_group == "None":
                error_str += "第"+str(ir)+"行,用例组不能为空；"
            if ins_excel.get_value(case_sheet, "D" + str(ir)) == "None":
                error_str += "第" + str(ir) + "行,函数名称不能为空；"
            if ins_excel.get_value(case_sheet, "I" + str(ir)) == "None":
                error_str += "第" + str(ir) + "行,路径不能为空；"
                continue
        elif ins_excel.get_value(case_sheet,"A"+str(ir)) == "是":
            case_group = ins_excel.get_value(case_sheet,"B"+str(ir))
            if case_group == "None":
                error_str += "第"+str(ir)+"行,用例组不能为空；"
            if ins_excel.get_value(case_sheet,"D" + str(ir)) == "None":
                error_str += "第"+str(ir)+"行,接口地址不能为空；"

            method = ins_excel.get_value(case_sheet, "F" + str(ir))
            if method == "None":
                error_str += "第"+str(ir)+"行,请求方法不能为空；"
            if ins_excel.get_value(case_sheet, "F" + str(ir)) != "None":
                method = method.upper()
                if method not in ["POST","GET"]:
                    error_str += "第"+str(ir)+"行,请求方法只能是POST、GET；"

            header = ins_excel.get_value(case_sheet,"G" + str(ir))
            if header != "None":
                try:
                    header = eval(header)
                    header_error_str = HeaderValueIsUnStr(ir, header)
                    if header_error_str != "":
                        error_str += header_error_str
                except:
                    error_str += "第" + str(ir) + "行,请求头不是键值对形式；"

                IsShuangyinhaoRight = check_ShuangShuXian(ir, str(header), "请求头")
                if IsShuangyinhaoRight != 1:
                    error_str += IsShuangyinhaoRight
                IsGuanlianedRight_header = CheckIsGuanlianedRight(ir, excel_path,case_group, ''.join(RemoveSpacesAndEnter(change_shuangyinhao(str(header))).split("\n")))
                if IsGuanlianedRight_header != 1:
                    error_str += IsGuanlianedRight_header

            body = ins_excel.get_value(case_sheet,"H" + str(ir))
            if body != "None" and method == "GET":
                error_str += "第"+str(ir)+"行,GET方法不能有请求体；"
            elif body != "None" and method == "POST":
                try:
                    body = json.loads(body)
                except:
                    error_str += "第" + str(ir) + "行,请求体不是json对象；"
                body_str = json.dumps(body)
                IsShuangyinhaoRight = check_ShuangShuXian(ir, str(body_str), "请求体")
                if IsShuangyinhaoRight != 1:
                    error_str += IsShuangyinhaoRight
                IsGuanlianedRight_body = CheckIsGuanlianedRight(ir, excel_path, case_group, body_str)
                if IsGuanlianedRight_body != 1:
                    error_str += IsGuanlianedRight_body

            expect_response = ins_excel.get_value(case_sheet,"I" + str(ir))
            if expect_response == "None":
                error_str += "第" + str(ir) + "行,预期返回值不能为空；"
            IsShuangyinhaoRight = check_ShuangShuXian(ir, expect_response, "预期返回值")
            if IsShuangyinhaoRight != 1:
                error_str += IsShuangyinhaoRight
            IsGuanlianedRight_expect_response = CheckIsGuanlianedRight(ir, excel_path, case_group, expect_response)
            if IsGuanlianedRight_expect_response != 1:
                error_str += IsGuanlianedRight_expect_response

        else:
            error_str += "第" + str(ir) + "行,是否执行列的值只能是‘是’、‘否’、$；"

    if error_str == "":
        return 1
    elif error_str != "":
        return error_str