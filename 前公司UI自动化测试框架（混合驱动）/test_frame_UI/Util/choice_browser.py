# coding=utf-8
from selenium import webdriver
from Util.ExcelAllSheet import *
from ProjectVar.var import *

def bowser_driver():
    ed=ExcelAllSheet(excel_path)
    for ir in range(2,5):
        if ed.get_value("参数设置","C"+str(ir)).strip()=="y":
            if ed.get_value("参数设置","A"+str(ir)).strip()=="IE":
                driver=webdriver.Ie(executable_path=ed.get_value("参数设置","B" + str(ir)))
            if ed.get_value("参数设置","A"+str(ir)).strip()=="Firefox":
                driver=webdriver.Firefox(executable_path=ed.get_value("参数设置","B" + str(ir)))
            if ed.get_value("参数设置","A"+str(ir)).strip()=="Chrome":
                driver = webdriver.Chrome(executable_path=ed.get_value("参数设置","B" + str(ir)))
            return driver