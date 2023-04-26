# coding=utf-8
from Util.ExcelAllSheet import *
from ProjectVar.var import data_record_path

def SplitAndReplace_xpath(thisxpat,ec,ish):
    xpath_list=thisxpat.split("%")
    if "||" in xpath_list[1]:
        aoto_str_list=xpath_list[1].split("||")
        auto_str=ec.get_value(aoto_str_list[0],aoto_str_list[1])[0:-1]
    else:
        auto_str =ec.get_value(ish,xpath_list[1])[0:-1]
    fp=open(data_record_path,"r",encoding="utf-8")
    line_list=fp.readlines()
    for il in line_list:
        if auto_str in il:
            replace_str=il.split("||")[-1]
            xpath_list[1]=replace_str.strip()
            last_xpath="".join(xpath_list)
            fp.close()
            return last_xpath

if __name__ == '__main__':
    from ProjectVar.var import excel_path
    ec = ExcelAllSheet(excel_path)
    print(SplitAndReplace_xpath("//div[.='%测试用3||G9%']", ec,"测试用3"))