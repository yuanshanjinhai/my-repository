# coding=utf-8
from GeneralTools.ExcelAllSheet import *
from GeneralTools.AllPath import CaseRule_path

def creat_list():
    case_rule_PathAndFile = CaseRule_path + "/用例规则.xlsx"
    ins = ExcelAllSheet(case_rule_PathAndFile)
    max_row = ins.get_max_row("Sheet1")
    case_rule_list = []
    for ir in range(2, max_row + 1):
        tem_list_B = ins.get_value("Sheet1", "B" + str(ir)).split("\n")
        tem_list = [ins.get_value("Sheet1", "A" + str(ir)), tem_list_B, ins.get_value("Sheet1", "C" + str(ir))]
        case_rule_list.append(tem_list)
    return case_rule_list

if __name__ == '__main__':
    for i0 in creat_list():
        for i1 in i0:
            print(i1)