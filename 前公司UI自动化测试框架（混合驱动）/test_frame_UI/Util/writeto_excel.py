# coding=utf-8
from Util.ExcelAllSheet import *

def writeto_excel(ec,sheet_name,ir,wl,IsSuccess): # 向Excel中写入执行结果，同时对外打印执行过程
    # ir -= 1
    if IsSuccess==1:
        ec.write_content(sheet_name,"M" + str(ir), "通过")
        ec.write_datetime_en(sheet_name,"N" + str(ir))
        wl.writelog(date_time(),ec.get_value(sheet_name,"O" + str(ir-1)),"调用了",ec.get_value(sheet_name,'E' + str(ir-1)),"函数",ec.get_value(sheet_name,'M' + str(ir-1)),"\n")

        print("%s ，用例 %d 执行成功 ：）" % (sheet_name,ir-1))
    if IsSuccess==0 or IsSuccess==-1:
        ec.write_content(sheet_name, "M" + str(ir), "未通过")
        print("%s，用例 %d 执行失败 ：（" % (sheet_name, ir-1))

    print("-" * 100)