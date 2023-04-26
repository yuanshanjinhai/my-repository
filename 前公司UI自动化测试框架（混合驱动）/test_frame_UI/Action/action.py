# coding=utf-8
import time
import sys
from selenium import webdriver
from Util.ExcelAllSheet import *
from ProjectVar.var import *
from Util.all_display_style_wait import *
from Util.keyboard import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# 设置一个显式等待的函数，虽然可以直接使用all_display_style_wait.py里的函数，但等待时间段和等待间隔还需要每个函数都输入一遍，不利于维护
def this_isvisible(driver,thisxpath):
    isvisible_result=isvisible(driver, 15, 0.2, thisxpath)
    if isvisible_result==1:
        return 1
    else:
        return 0

# ----------------获取并进入frame
def getintoframe(driver,thisxpath):
    if this_isvisible(driver,thisxpath)==1:
        pass
    else:
        return 0
    thisframe = driver.find_element_by_xpath(thisxpath)
    driver.switch_to_frame(thisframe)
    print("已进入frame/iframe")
    return 1

# ----------------退出frame
def outframe(driver):
    driver.switch_to.default_content()
    print("已退出frame/iframe")

# --------------向输入框输入内容，用clear()清空
def inputtext(driver,thisxpath,content):
    if this_isvisible(driver,thisxpath)==1:
        pass
    else:
        return 0
    thistext=driver.find_element("xpath",thisxpath)
    thistext.click()
    thistext.clear()
    thistext.send_keys(content)
    return 1

# ----------------向输入框输入内容，用键盘清空
def inputtext_by_kb(driver,thisxpath,content):
    if this_isvisible(driver,thisxpath)==1:
        pass
    else:
        return 0
    thistext = driver.find_element("xpath", thisxpath)
    thistext.click()
    keyDown("ctrl")
    keyDown("a")
    keyUp("a")
    keyUp("ctrl")
    keyDown("del")
    keyUp("del")
    thistext.send_keys(content)
    return 1

# ---------------点击元素
def clicksth(driver,thisxpath):
    if this_isvisible(driver,thisxpath)==1:
        pass
    else:
        return 0
    driver.find_element("xpath",thisxpath).click()
    return 1

# ----------------鼠标悬停
def mouse_stop(driver,thisxpath):
    if this_isvisible(driver,thisxpath)==1:
        pass
    else:
        return 0
    mouse=driver.find_element("xpath", thisxpath)
    ActionChains(driver).move_to_element(mouse).perform()
    return 1

# ------------从下拉框选择选项（下拉框无selec和option，需点击开其选项后才能定位）
def dropdown_noso(driver,thisxpath):
    if this_isvisible(driver, thisxpath.split("||")[0])==1:
        pass
    else:
        return 0
    driver.find_element("xpath", thisxpath.split("||")[0]).click()
    time.sleep(1)
    driver.find_element("xpath", thisxpath.split("||")[1]).click()
    return 1

# -------------通过键盘下箭头来选择下拉框数据，num为按几下下箭头
def dropdown_by_keyboard(driver,thisxpath,num):
    if this_isvisible(driver,thisxpath)==1:
        pass
    else:
        return 0
    driver.find_element("xpath",thisxpath).click()
    time.sleep(2)
    for i in range(0,int(num)):
        keyDown('down_arrow')
        keyUp('down_arrow')
        time.sleep(1)
    keyDown('enter')
    keyUp('enter')
    return 1

# -------------操作滚动条到底
def scroll_bar_bottom(driver):
    js = "window.scrollTo(0, document.body.scrollHeight"
    driver.execute_script(js)

# ---------------操作滚动条到一半位置
def scroll_bar_href(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5);")

# -------------点击Tab键
def Tab(num):
    for i in range(num):
        keyDown("tab")
        keyUp("tab")

# ---------------点击回车键
def Enter():
    keyDown("enter")
    keyUp("enter")

# -------------按PageDown键，num为按几下
def PageDown(num):
    for i in range(int(num)):
        keyDown('page_down')
        keyUp('page_down')
        time.sleep(1)

# ---------------按键盘下箭头
def option_down_arrow(num):
    for i in range(0,int(num)):
        keyDown('down_arrow')
        keyUp('down_arrow')
        time.sleep(0.3)

# 处理一条xpath语句定位出多个元素的情况，获取后点击该元素
def locate_elements(driver,thisxpath):
    thisxpath_list=thisxpath.split("||")
    element_list=driver.find_elements("xpath",thisxpath_list[0])
    element_list[int(thisxpath_list[1])-1].click()

# 判断元素是否存在于页面上
def isElementPresent(driver,thisxpath):
    try:
        driver.find_element("xpath",thisxpath)
    except NoSuchElementException as e:
        return False
    else:
        return True

if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Firefox(executable_path=r"D:\webdriver\geckodriver.exe")
    driver.get("http://192.168.70.248:8083/portal/")
    inputtext(driver, "//input[@id='userName']", "kongxu")
    #clicksth(driver, "//a[@href='http://news.baidu.com' and .='新闻']", "//a[.='举报']", 2)