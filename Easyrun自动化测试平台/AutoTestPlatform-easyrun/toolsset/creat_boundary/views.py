# coding=utf-8
from flask import request, render_template, redirect, url_for,flash,session
from flask import Blueprint
from flask.views import MethodView
from toolsset.creat_boundary.models import *
from toolsset.creat_boundary.tools import *

Blue_tools_boundary = Blueprint("boundary", __name__)

class CreatBoundary(MethodView):
    def __init__(self):
        self.ins_creat_boundary_Form = CreatBoundaryForm(request.form)

    def get(self,username,token):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            from login.models import loginform
            ins_loginfrom = loginform(request.form)
            return render_template("login/login.html", form=ins_loginfrom)
        return render_template("toolsset/creat_boundary/creat_boundary.html",form=self.ins_creat_boundary_Form,username=username,token=token)

    def post(self,username,token):
        word_lenth = self.ins_creat_boundary_Form.word_lenth.data
        word_type = self.ins_creat_boundary_Form.word_type.data

        error_str = ""
        if self.ins_creat_boundary_Form.submit_sub.data == 1:
            if word_lenth == "":
                error_str += "请输入文本长度！"
            if word_lenth != "" and str.isdigit(word_lenth) == 0:
                error_str += "只能输入正整数！"
            if word_lenth != "" and str.isdigit(word_lenth) == 1 and int(word_lenth)>20000:
                error_str += "长度不能超过20000！"
            if error_str != "":
                flash(error_str)
                return render_template("toolsset/creat_boundary/creat_boundary.html", form=self.ins_creat_boundary_Form,username=username,token=token)
            else:
                word_lenth = int(word_lenth)
                if word_type == "综合" and word_lenth < 36:
                    error_str += "综合输入的长度不能小于等于35！"
                    flash(error_str)
                    return render_template("toolsset/creat_boundary/creat_boundary.html",form=self.ins_creat_boundary_Form,username=username,token=token)
                output_word = creat_word(word_lenth, word_type)
                return render_template("toolsset/creat_boundary/creat_boundary.html",form=self.ins_creat_boundary_Form,username=username,token=token,opw=output_word)

        if self.ins_creat_boundary_Form.reset_sub.data == 1: # 点击重置按钮
            self.ins_creat_boundary_Form.word_lenth.data = ""  # 设置输入长度默认值
            return render_template("toolsset/creat_boundary/creat_boundary.html",form=self.ins_creat_boundary_Form,username=username,token=token)

        if self.ins_creat_boundary_Form.punctuation_sub.data == 1:
            if word_lenth == "":
                output_word = creat_punctuation()
                return render_template("toolsset/creat_boundary/creat_boundary.html",form=self.ins_creat_boundary_Form,username=username,token=token, opw=output_word)
            elif str.isdigit(word_lenth) == 0:
                    error_str += "只能输入1-32之间的正整数！"
            elif int(word_lenth) > 32 or int(word_lenth) < 1:
                    error_str += "只能输入1-32之间的正整数！"
            if error_str != "":
                flash(error_str)
                return render_template("toolsset/creat_boundary/creat_boundary.html",form=self.ins_creat_boundary_Form,username=username,token=token)
            else:
                output_word = creat_punctuation(int(word_lenth))
            return render_template("toolsset/creat_boundary/creat_boundary.html", form=self.ins_creat_boundary_Form,username=username,token=token,opw=output_word)
Blue_tools_boundary.add_url_rule("/creat_boundary/<username>/<token>",view_func=CreatBoundary.as_view("creat_boundary"))

