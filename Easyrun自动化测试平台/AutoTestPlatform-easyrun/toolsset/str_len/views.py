# coding=utf-8
from flask import request, render_template, redirect, url_for,flash,session
from flask import Blueprint
from flask.views import MethodView
from toolsset.str_len.models import *

Blue_tools_strlen = Blueprint("tools_strlen", __name__)

class StrLen(MethodView):
    def __init__(self):
        self.ins_strlen_Form = CreatStrlenForm(request.form)

    def get(self,username,token):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            from login.models import loginform
            ins_loginfrom = loginform(request.form)
            return render_template("login/login.html", form=ins_loginfrom)
        return render_template("toolsset/str_len/str_len.html",form=self.ins_strlen_Form,username=username,token=token)

    def post(self,username,token):
        if self.ins_strlen_Form.submit_sub.data == 1: # 点击提交按钮
            str_ = self.ins_strlen_Form.str_.data
            if str_ == "":
                flash("请输入字符串！")
                return render_template("toolsset/str_len/str_len.html", form=self.ins_strlen_Form, username=username,token=token)
            elif str_ != "":
                str_len = len(str_)
                return render_template("toolsset/str_len/str_len.html", form=self.ins_strlen_Form, username=username,token=token,str_len=str_len)
        if self.ins_strlen_Form.reset_sub.data == 1:
            self.ins_strlen_Form.str_.data = ""
            return render_template("toolsset/str_len/str_len.html", form=self.ins_strlen_Form, username=username,token=token)
Blue_tools_strlen.add_url_rule("/str_len/<username>/<token>",view_func=StrLen.as_view("str_len"))