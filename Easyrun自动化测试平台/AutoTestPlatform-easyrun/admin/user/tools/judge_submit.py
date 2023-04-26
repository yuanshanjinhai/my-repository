# coding = utf-8
from admin.user.DB.OtherDB import JudgeUserNameIsRepead
from GeneralTools.OtherTools import md5_encrypt

def judge_submit(type,old_password,new_password,user_login_name,user_name,role):
    error_str = ""
    if user_login_name == "":
        error_str += "用户登录名不能为空；"
    if JudgeUserNameIsRepead(user_login_name)==0 and type == "N":
        error_str += "用户登录名不能重复；"
    if user_name == "":
        error_str += "用户名不能为空；"
    if old_password != 0 and new_password == "":
        error_str += "新密码不能为空；"
    if old_password != 0 and old_password == md5_encrypt(new_password):
        error_str += "新老密码不能重复；"
    if role == "None":
        error_str += "对应角色不能为空；"
    if len(user_login_name) > 30:
        error_str += "用户登录名最多不超过30字；"
    if len(user_name) > 50:
        error_str += "用户名最多不超过50字；"
    judge_user_name_is_repead = JudgeUserNameIsRepead(user_name)
    if judge_user_name_is_repead != 1:
        error_str += judge_user_name_is_repead
    if error_str == "":
        return 1
    else:
        return error_str