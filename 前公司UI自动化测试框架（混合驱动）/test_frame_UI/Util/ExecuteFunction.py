# coding=utf-8
from Util.ExcelAllSheet import *
from Util.write_log import *
from Util.writeto_excel import *
from Action.action import *

def ExecuteFunction0(driver,function_name,thisxpath,thisdata):
    if function_name=="inputtext": # 向输入框输入元素，通过clear()清空
        result=inputtext(driver, thisxpath, thisdata)
        return result

    if function_name=="inputtext_by_kb": # 向输入框输入元素，通过键盘清空
        result=inputtext_by_kb(driver, thisxpath, thisdata)
        return result

    if function_name=="clicksth": # 点击
        result=clicksth(driver, thisxpath)
        return result

    if function_name=="getintoframe": # 进入frame
        result=getintoframe(driver, thisxpath)
        return result

    if function_name=="outframe": # 退出frame
        outframe(driver)
        return -1

    if function_name=="mouse_stop": # 鼠标悬停
        result=mouse_stop(driver,thisxpath)
        return result

    if function_name=="dropdown_by_keyboard": # 通过键盘下箭头来选择下拉框数据
        result=dropdown_by_keyboard(driver,thisxpath,int(thisdata))
        return result

    if function_name=="dropdown_noso": # 从下拉框选择选项（下拉框无selec和option，需点击开其选项后才能定位）
        result=dropdown_noso(driver,thisxpath)
        return result

    if function_name=="scroll_bar_bottom": # 操作滚动条到底
        scroll_bar_bottom(driver)
        return -1

    if function_name=="scroll_bar_bottom": # 操作滚动条到一半
        scroll_bar_href(driver)
        return -1

    if function_name=="Tab": # 点击Tab键
        Tab(thisdata)
        return -1

    if function_name=="Enter": # 点击回车键:
        Enter()
        return -1

    if function_name=="PageDown": # 按PageDown键
        PageDown(thisdata)
        return -1

    if function_name=="option_down_arrow": # 按键盘的下箭头键
        option_down_arrow(thisdata)
        return -1

def ExecuteFunction(driver,ec,ish,ir,wl,function_name,thisxpath,thisdata):
    print(ish,"，用例",ir-1,"开始执行……")
    if ec.get_value(ish,"I"+str(ir))!="None": # 判断是否必填
        ismust =1
    else:
        ismust =0

    if ec.get_value(ish,"J"+str(ir))!="None": # 判断失败后循环次数
        LoopLimit=int(ec.get_value(ish,"J"+str(ir)))
    else:
        LoopLimit=3

    result0=ExecuteFunction0(driver,function_name,thisxpath,thisdata)
    if result0 == 1:
        print("ir1=",ir)
        writeto_excel(ec, ish, ir, wl, 1)
        return "success"
    elif result0==0:
        for ir in range(1, LoopLimit + 1):
            print("尝试第", str(ir + 1), " 次执行……")
            result = ExecuteFunction0(driver, function_name, thisxpath, thisdata)
            if result == 1:
                result_str= "success"
                return result_str
            else:
                continue
        if ismust == 1:
            return "Must_ElementLocationFailed"
        else:
            return "UnMust_ElementLocationFailed"
    else:
        return "success_nowrite"

if __name__ == '__main__':
    pass