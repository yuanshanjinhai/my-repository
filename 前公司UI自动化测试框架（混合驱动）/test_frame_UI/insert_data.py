# coding=utf-8
from Util.ExcelAllSheet import *
from ProjectVar.var import *

ec=ExcelAllSheet(excel_path)

case_designer=ec.get_value("参数设置","A9")

run_sheet_list=[] # 获取要执行的所有sheet
for ir in range(12,ec.get_max_row("参数设置")+1):
    this_sheet=ec.get_value("参数设置","A"+str(ir))
    if this_sheet=="None":
        continue
    if "||" in this_sheet:
        this_sheet=this_sheet.split("||")[0]
    run_sheet_list.append(this_sheet)

for irs in run_sheet_list:
    id = 1
    for ir in range(2,ec.get_max_row(irs)+1):
        ec.write_content(irs,"A"+str(ir),str(id))
        if case_designer!="":
            ec.write_content(irs,"N"+str(ir),case_designer)
        id+=1
    ec.save_content()
