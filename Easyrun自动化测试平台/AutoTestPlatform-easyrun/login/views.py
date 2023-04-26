# coding=utf-8
from flask import flash,session,redirect
from flask.views import MethodView
from flask import Blueprint
from login.models import *
from login.DB.OtherDB import *
from login.DB.UpdatePassword import UpdatePassword
from interface_test.singlerun.models import *
from GeneralTools.OtherTools import get_encypt_decrypt_file
from login.tools.other_tools import judge_updatepassword

Blue_login=Blueprint("login",__name__)

class Login(MethodView):
    def __init__(self):
        self.ins_loginfrom=loginform(request.form)
        self.ins_singlerunFrom = SinglerunForm(request.form)
    def get(self):
        if "user_resource_list" in session:
            del session["user_resource_list"]
        if "user_login_name" in session:
            del session["user_login_name"]
        if "user_name" in session:
            del session["user_name"]
        return render_template("login/login.html",form=self.ins_loginfrom)
    def post(self):
        user_login_name = self.ins_loginfrom.username.data
        input_password = self.ins_loginfrom.password.data
        JudegeUP = JudegeUserPassword(user_login_name, input_password)
        if JudegeUP == 0:
            flash("用户名或密码错误")
            return render_template("login/login.html", form=self.ins_loginfrom)
        if JudegeUP == 1:
            user_name = GetUserNameByUserLoginName(user_login_name)
            user_resource_list = GetUserResourceList(user_login_name)
            session["user_resource_list"] = user_resource_list
            session["user_login_name"] = user_login_name
            session["user_name"] = user_name
            self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
            return redirect(url_for("home.home"))

Blue_login.add_url_rule("/login/",view_func=Login.as_view("login"))


class UpdatePasword(MethodView):
    def __init__(self):
        self.ins_UpdatePasswordForm = UpdatePasswordForm(request.form)

    def get(self):
        return render_template("login/updatepassword.html",form=self.ins_UpdatePasswordForm)

    def post(self):
        login_name = self.ins_UpdatePasswordForm.login_name.data
        old_password = self.ins_UpdatePasswordForm.old_password.data
        new_password = self.ins_UpdatePasswordForm.new_password.data
        new_password_again = self.ins_UpdatePasswordForm.new_password_again.data
        judge_updatepassword_r = judge_updatepassword(login_name, old_password, new_password, new_password_again)
        if judge_updatepassword_r != 1:
            flash(judge_updatepassword_r)
            return render_template("login/updatepassword.html", form=self.ins_UpdatePasswordForm)
        if judge_updatepassword_r == 1:
            UpdatePassword(login_name, new_password)
            flash("修改密码成功；")
            return render_template("login/updatepassword.html", form=self.ins_UpdatePasswordForm)
            
Blue_login.add_url_rule("/updatepassword/",view_func=UpdatePasword.as_view("updatepassword"))



if __name__ == '__main__':
    pass