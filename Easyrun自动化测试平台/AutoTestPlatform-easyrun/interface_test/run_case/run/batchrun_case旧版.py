# coding=utf-8
import gevent
from gevent import monkey
import requests

def BatchRunCase(run_case_tuple): # 自动切换协程执行用例的函数
    group0_list = run_case_tuple[0]
    
    print("协程开始") #其中all_case_list的形式为[[((),(),()),((),())],[((),()),((),(),(),)]]，内嵌列表为用例组
    monkey.patch_all()
    xiecheng_list=[]
    for ia in all_case_list:
        r = gevent.spawn(run_case,username,ia,excel_case_path,is_urldecode)
        xiecheng_list.append(r)
    gevent.joinall(xiecheng_list)