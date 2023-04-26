# coding=utf-8
from Util.FormatTime import date_time_chinese
from Util.ExcelAllSheet import *
from Util.write_log import *
from ProjectVar.var import *
from Util.check_csae import *
from Action.action import *
from Util.choice_browser import *
from Util.data_GenerateAndRecord import *
from Util.SplitAndReplace_xpath import *
from Util.TransformXpathShuangyinhao import *
from Util.GetHandleDict import *
from Util.ExecuteFunction import *
from Util.writeto_excel import *
import time
import sys

ec=ExcelAllSheet(excel_path)
run_sheet_list=[] # 获取要执行的所有sheet
for ir in range(12,ec.get_max_row("参数设置")+1):
    if ec.get_value("参数设置","A"+str(ir))=="None":
        continue
    run_sheet_list.append(ec.get_value("参数设置","A"+str(ir)))

inscc=check_case(ec)
error_list=inscc.check() # 获取检查用例后的错误list
if error_list!=[]: # 如果error_list不为空，说明用例脚本编写有问题，打印出所有问题并结束程序
    for ier in error_list:
        print(ier)
    sys.exit()

driver=bowser_driver() # 获取浏览器实例，打开浏览器
driver.get(ec.get_value("参数设置","B6"))
# driver.maximize_window() # 窗口最大化
wl=Writelog() # 写入日志类的实例化

for ish in run_sheet_list: # 循环执行所有用例sheet中的用例
    if "||" in ish: # 设置sheet_num，即一个sheet执行几遍
        sheet_num =int(ish.split("||")[1])
        ish=ish.split("||")[0]
    else:
        sheet_num=1
    isbreaksheet = 0  # 设置isbreaksheet，即是否跳出run_sheet_list的循环执行,0为不跳出，继续执行，1为跳出
    IsSuccess=1 # 设置用例是否执行成功，默认为1，即执行成功
    for irs in range(sheet_num):
        write_handle("")  # 清空句柄文件
        driver.get(ec.get_value("参数设置","B6"))
        if isbreaksheet==1:
            break
        if IsSuccess==-1: # IsSuccess==-1代表必填项的元素定位元素失败，因此不再循环执行sheet，直接跳出循环，执行下一个sheet
            break
        for ir in range(2,ec.get_max_row(ish)+1): # 从第二行循环至最大行
            if ec.get_value(ish,"L" + str(ir))=="n": # 如果是否执行列为n
                ec.write_content(ish,"M" + str(ir), "")
                continue

            if ec.get_value(ish,"E"+str(ir))=="isElementPresent": # 判断元素是否存在于页面上
                if "%" in ec.get_value(ish,"F" + str(ir)):
                    thisxpath = SplitAndReplace_xpath(ec.get_value(ish,"F" + str(ir)),ec,ish)
                    action = action + "\"" + thisxpath + "\"" + ","
                    action = action[0:-1] + """)"""
                result=exec(action)
                if result==True:
                    writeto_excel(ec,ish,ir,wl,1)
                if result==False:
                    writeto_excel(ec,ish, ir,wl, 0)
                    sys.exit()

            if ec.get_value(ish, "E" + str(ir)) == "close_window": # 判断是否关闭窗口
                handle_str=ec.get_value(ish, "H" + str(ir))
                handle_closed_name=handle_str.split("||")[0]
                handle_switchto_name=handle_str.split("||")[1]
                handle_dict=read_handle()
                for ih in handle_dict.keys():
                    if ih==handle_closed_name:
                        handle_closed_value=handle_dict[ih]
                    if ih==handle_switchto_name:
                        handle_switchto_value=handle_dict[ih]
                driver.switch_to.window(handle_closed_value)
                driver.close()
                driver.switch_to.window(handle_switchto_value)
                handle_dict=read_handle()
                del handle_dict[handle_str.split("||")[0]]
                write_handle(handle_dict)
                continue

            if ec.get_value(ish,"E"+str(ir))=="switch_window": # 判断是否需要切换窗口句柄
                handle_dict=read_handle()
                for k in handle_dict.keys():
                    if k==ec.get_value(ish,"H"+str(ir)):
                        driver.switch_to.window(handle_dict[k])
                        time.sleep(2)
                        break
                continue

            else:
                isautodata = 0  # 标识是否自动生成数据，如果自动生成，则置为1，否则一直是0
                if ec.get_value(ish, "H" + str(ir))!="None": # 如果H 列不为空，则需要切换窗口，此处为切换窗口
                    for ihf in "HF":
                        if ihf=="H":
                            isnewindow = 0  # 标识是否打开新窗口，打开则为1，沿用当前窗口则为0
                            if ec.get_value(ish, "H" + str(ir))!="None":
                                pass
                            handle_str=ec.get_value(ish, "H" + str(ir))
                            handle_dict = read_handle()  # 生成句柄字典
                            if "||" in handle_str:
                                handle_name_list=handle_str.split("||")
                                if handle_dict=={}:
                                    handle_dict[handle_name_list[0]]=driver.current_window_handle  # 设置句柄字典中当前窗口句柄的名称为窗口句柄列中||之前的部分，值为当前窗口句柄
                                isnewindow=1
                            if "||" not in handle_str:
                                isnewindow=1
                        if ihf == "F":
                            if isnewindow == 1:
                                function_name=ec.get_value_n(ish, "E" + str(ir))
                                thisxpath=ec.get_value_n(ish, "F" + str(ir))
                                thisdata=ec.get_value_n(ish, "G" + str(ir))
                                ExecuteFunction(driver, ec, ish, ir, wl, function_name, thisxpath, thisdata)
                                time.sleep(3)
                                if "||" in handle_str:
                                    SwitchHandleFirstTime(driver, handle_dict,handle_name_list)  # 切换到新打开的窗口的句柄，并把新句柄插入到句柄字典，把字典重新写入到配置文件
                                if "||" not in handle_str:
                                    SwitchHandle(driver, handle_str)  # 切换到新打开的窗口的句柄，并把新句柄插入到句柄字典，把字典重新写入到配置文件

                else:
                    function_name=ec.get_value_n(ish,"E"+str(ir))
                    thisxpath=TransformXpathShuangyinhao(ec.get_value_n(ish,"F"+str(ir))) # 取到F列的xpath值，并把双引号转换为单引号
                    thisdata=ec.get_value_n(ish,"G"+str(ir))
                    if "%" in thisdata: # 如果该行的G列含有%，说明需要自动生成名称，就调用auto_name函数来自动生成名称
                        thisdata=auto_name(thisdata)
                        isautodata=1 # 是否自动生成数据的标识被改成1

                    Execute_result_str=ExecuteFunction(driver, ec, ish, ir, wl, function_name, thisxpath, thisdata)
                    if Execute_result_str=="success": # 如果执行成功
                        IsSuccess = 1 # 1为执行成功，继续执行用例

                    if Execute_result_str=="success_nowrite": # 如果执行成功但无需写入excel和日志
                        IsSuccess = 1

                    if Execute_result_str == "Must_ElementLocationFailed": # 如果必填项执行失败
                        IsSuccess = -1 # -1为必填项执行失败，跳出循环，跳出代码到第二个循环处
                        writeto_excel(ec, ish, ir, wl, IsSuccess)

                    if Execute_result_str == "UnMust_ElementLocationFailed": # 如果非必填项执行失败
                        IsSuccess = 0 # 非必填项执行失败，不影响流程，继续执行用例
                        writeto_excel(ec, ish, ir, wl, IsSuccess)

                if IsSuccess==1:
                    pass
                if IsSuccess==0:
                    pass
                if IsSuccess==-1:
                    ec.save_content()  # 保存，每执行完一个sheet就保存一次，由于必填项执行失败，所以保存执行结果
                    break

                if isautodata==1:
                    write_data(thisdata) # 向记录自动生成数据的配置文件里插入自动生成的数据

                time.sleep(int(ec.get_value(ish, "K" + str(ir))))

        ec.save_content() # 保存，每执行完一个sheet就保存一次

wl.writelog("-"*100+"\n")

wl.closefp()
driver.quit()

if __name__=="__main__":
    pass