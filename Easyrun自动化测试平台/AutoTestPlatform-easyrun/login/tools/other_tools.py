# coding=utf-8
from login.DB.OtherDB import judge_login_name_is_exis,judge_old_password

def judge_new_password(new_password,new_password_again):
    if new_password == new_password_again:
        return 1
    else:
        return 0

def judge_updatepassword(login_name,old_password,new_password,new_password_again):
    print("login_name=",login_name,type(login_name),len(login_name))
    error_str = ""
    if login_name == "":
        error_str += "登录名不能为空；"
    if old_password == "":
        error_str += "原密码不能为空；"
    if new_password == "":
        error_str += "新密码不能为空；"
    if new_password_again == "":
        error_str += "确认新密码不能为空；"
    if error_str != "":
        return error_str
    if judge_login_name_is_exis(login_name) == 0:
        return "登录名不存在；"
    if judge_old_password(login_name,old_password) == 0:
        return "原密码错误；"
    if judge_new_password(new_password,new_password_again) == 0:
        return "新密码与确认新密码不一致；"
    return 1