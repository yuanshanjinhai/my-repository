# coding = utf-8
from flask import Blueprint,request, render_template, flash,session,redirect,url_for
from flask.views import MethodView
from interface_test.global_var.models import *
from interface_test.global_var.tools.other_tools import *
from interface_test.global_var.tools.judge_submit import *
from interface_test.global_var.DB.InsertGlobalVarSingle import *
from interface_test.global_var.DB.UpdateGlobalVarSingle import *

Blue_global_var = Blueprint("global_var", __name__)

class GlobalVarList(MethodView):
    def __init__(self):
        self.ins_GlobalVarListForm = GloblaVarListForm(request.form)

    def get(self,product_name,page_no,offset,limit,global_var_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        self.ins_GlobalVarListForm.product_name.choices = GetProductNameList()
        page_no = int(page_no)
        offset = int(offset)
        limit = int(limit)
        if product_name == '全部项目':
            total_pages = count_total_pages(limit)
        else:
            total_pages = count_total_pages_product_name(product_name, limit)
        if total_pages == 1:
            offset = 0
            page_no = 1
        elif page_no <= 0:
            offset = 0
            page_no = 1
        elif page_no > total_pages:
            offset -= limit
            page_no = total_pages
        if product_name == '全部项目':
            global_var_list = GetGlobalVarList(offset,limit)
        else:
            global_var_list = GetGlobalVarList_product_name(product_name, offset, limit)
        return render_template("interface_test/global_var/global_var_list.html", form=self.ins_GlobalVarListForm,
                               data_list=global_var_list, product_name=product_name, page_no=page_no,
                               total_pages=total_pages, offset=offset, limit=limit, global_var_id=global_var_id)

    def post(self,product_name,page_no,offset,limit,global_var_id):
        self.ins_GlobalVarListForm.product_name.choices = GetProductNameList()
        limit = int(limit)
        if self.ins_GlobalVarListForm.search_sub.data == 1:  # 点击搜索按钮
            product_name = self.ins_GlobalVarListForm.product_name.data
            global_var_id = global_var_id
            offset = 0
            total_pages = count_total_pages_product_name(product_name, limit)
            global_var_list = GetGlobalVarList_product_name(product_name, offset, limit)
            return render_template("interface_test/global_var/global_var_list.html", form=self.ins_GlobalVarListForm,
                                   data_list=global_var_list, product_name=product_name, page_no=1,
                                   total_pages=total_pages, offset=offset, limit=limit, global_var_id=global_var_id)
        if self.ins_GlobalVarListForm.delete_sub.data == 1:  # 点击删除按钮
            page_no = int(page_no)
            offset = int(offset)
            limit = int(limit)
            global_var_id = self.ins_GlobalVarListForm.get_id.data
            DeleteGlobalVar(global_var_id)
            if product_name == "全部项目":
                total_pages = count_total_pages(limit)
                if page_no > total_pages:
                    offset -= limit
                    page_no -= 1
                global_var_list = GetGlobalVarList(offset, limit)
            else:
                total_pages = count_total_pages_product_name(product_name, limit)
                if page_no > total_pages:
                    offset -= limit
                    page_no -= 1
                global_var_list = GetGlobalVarList_product_name(product_name, offset, limit)
            flash("删除成功；")
            return render_template("interface_test/global_var/global_var_list.html", form=self.ins_GlobalVarListForm,
                                   data_list=global_var_list, product_name=product_name, page_no=page_no,
                                   total_pages=total_pages, offset=offset, limit=limit, global_var_id=global_var_id)

Blue_global_var.add_url_rule("/interface_test/Blue_global_var/global_var_list/<product_name>/<page_no>/<offset>/<limit>/<global_var_id>",view_func=GlobalVarList.as_view("global_var_list"))


class GlobalVar_NEC(MethodView):
    def __init__(self):
        self.ins_GlobalVarNEC_Form = GloblaVarNEC_Form(request.form)

    def get(self,product_name,page_no,offset,limit,type,global_var_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        if type == "N":
            self.ins_GlobalVarNEC_Form.product_name.choices = GetProductNameList()
        if type == "E" or type == "C":
            self.ins_GlobalVarNEC_Form.product_name.choices = GetProductNameList()
            self.ins_GlobalVarNEC_Form.global_var_name.data = GetGlobalVarNameByGlobalVarId(global_var_id)
            self.ins_GlobalVarNEC_Form.global_var_value.data = GetIGlobalVarValueByGlobalVarId(global_var_id)
            self.ins_GlobalVarNEC_Form.is_auto_add.data = GetIsAutoAddByGlobalVarId(global_var_id)
            self.ins_GlobalVarNEC_Form.global_var_explain.data = GetGlobalVarExplainByGlobalVarId(global_var_id)
        return render_template("interface_test/global_var/global_var_NEC.html", form=self.ins_GlobalVarNEC_Form,
                               product_name=product_name, page_no=page_no, offset=offset, limit=limit, type=type,
                               global_var_id=global_var_id)

    def post(self,product_name,page_no,offset,limit,type,global_var_id):
        if self.ins_GlobalVarNEC_Form.submit_sub.data == 1: # 点击提交按钮
            product_name = self.ins_GlobalVarNEC_Form.product_name.data
            global_var_name = self.ins_GlobalVarNEC_Form.global_var_name.data
            global_var_value = self.ins_GlobalVarNEC_Form.global_var_value.data
            is_auto_add = self.ins_GlobalVarNEC_Form.is_auto_add.data
            global_var_explain = self.ins_GlobalVarNEC_Form.global_var_explain.data

            judge_submit_result = judge_submit(type,global_var_id,product_name,global_var_name,global_var_value,is_auto_add,global_var_explain)
            if judge_submit_result != 1:
                self.ins_GlobalVarNEC_Form.product_name.choices = GetProductNameList()
                flash(judge_submit_result)
                return render_template("interface_test/global_var/global_var_NEC.html",form=self.ins_GlobalVarNEC_Form,
                                       product_name=product_name, page_no=page_no, offset=offset, limit=limit,type=type,
                                       global_var_id=global_var_id)
            elif judge_submit_result == 1:
                self.ins_GlobalVarNEC_Form.product_name.choices = GetProductNameList()
                if type == "N":
                    InsertGlobalVarSingle(product_name,global_var_name,global_var_value,is_auto_add,global_var_explain)
                    flash("新增全局变量成功；")
                elif type == "E":
                    UpdataGlobalVarSingle(product_name,global_var_id,global_var_name,global_var_value,is_auto_add,global_var_explain)
                    flash("编辑全局变量成功；")
                elif type == "C":
                    InsertGlobalVarSingle(product_name,global_var_name,global_var_value,is_auto_add,global_var_explain)
                    flash("复制新增全局变量成功；")
                return render_template("interface_test/global_var/global_var_NEC.html", form=self.ins_GlobalVarNEC_Form,
                                       product_name=product_name, page_no=page_no, offset=offset, limit=limit,
                                       type=type, global_var_id=global_var_id)

Blue_global_var.add_url_rule("/interface_test/global_var/global_var_NEC/<product_name>/<page_no>/<offset>/<limit>/<type>/<global_var_id>",view_func=GlobalVar_NEC.as_view("global_var_NEC"))
