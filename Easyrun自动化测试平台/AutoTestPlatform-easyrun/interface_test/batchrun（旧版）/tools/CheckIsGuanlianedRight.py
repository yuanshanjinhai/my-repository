# coding=utf-8
import re
from GeneralTools.ExcelAllSheet import *

def CheckIsGuanlianedRight(ir,excel_path,case_group,body_str):
    error_str = ""
    ins_excel = ExcelAllSheet(excel_path)
    IsGuanlian_list = re.findall(r"【\$\|\|\w+】",body_str)
    if IsGuanlian_list == []:
        return 1
    else:
        depended_functionIsExit = 0
        for iI in IsGuanlian_list:
            depend_function = iI[1:-1].split("||")[1]
            for iin in range(ir, 1, -1):
                if ins_excel.get_value("用例", "A" + str(iin)) == "$":
                    function_name = ins_excel.get_value("用例", "D" + str(iin))
                    depended_json_path = ins_excel.get_value("用例", "I" + str(iin))
                    if function_name == depend_function:
                        depended_functionIsExit = 1
                        for i_iin in range(iin, 1, -1):
                            if ins_excel.get_value("用例", "A" + str(i_iin)) == "否":
                                error_str += "第" + str(i_iin) + "行,用例被设置为不执行，无法提供关联；"
                                break
                            elif ins_excel.get_value("用例","A" + str(i_iin)) == "是":
                                depend_str = ins_excel.get_value("用例", "I" + str(i_iin))
                                try:
                                    eval(depend_str + depended_json_path)
                                except:
                                    error_str += "第" + str(iin) + "行，无法根据路径在实际返回值中找到数据；"
                                break
        if depended_functionIsExit == 0:
            error_str += "第" + str(ir) + "行,该用例未找到被关联函数；"
        if error_str != "":
            return error_str
        else:
            return 1