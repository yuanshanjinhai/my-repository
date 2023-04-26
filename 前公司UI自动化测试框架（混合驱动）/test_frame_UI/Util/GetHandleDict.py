# coding=utf-8
from Util.data_GenerateAndRecord import *
import time

def SwitchHandleFirstTime(driver,handle_dict,handle_name_list): # 切换到新打开的窗口，并把新句柄插入到句柄字典，把字典重新写入到配置文件（当H列有||时）
    all_handles_list=driver.window_handles
    for ia in all_handles_list:
        if ia != handle_dict[handle_name_list[0]]:
            handle_dict[handle_name_list[1]]=ia
            write_handle(handle_dict) # 把新句柄写入到配置文件
            driver.switch_to.window(ia) # 切换至新窗口句柄
            break

def SwitchHandle(driver,handle_str): # 切换到新打开的窗口的句柄，并把新句柄插入到句柄字典，把字典重新写入到配置文件（当H列没有||时）
    all_handles_list = driver.window_handles
    handle_dict=read_handle()
    for ia in all_handles_list:
        count=0
        for v in handle_dict.values():
            if ia==v:
                count=1
        if count==0:
            handle_dict[handle_str]=ia
            write_handle(handle_dict) # 把新句柄写入到配置文件里
            break
    driver.switch_to.window(ia)
