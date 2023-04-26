# coding=utf-8
from flask import Blueprint,render_template,session,request,redirect,url_for
from flask.views import MethodView
from helps.case_rule.Toos import *

Blue_case_rule= Blueprint("CaseRule", __name__)

class CaseRule(MethodView):
    def get(self):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        case_rule_list = creat_list()
        return render_template("helps/case_rule/case_rule.html",deta_list=case_rule_list)

Blue_case_rule.add_url_rule("/helps/case_rule/", view_func=CaseRule.as_view("case_rule"))