# coding = utf-8
from flask import Blueprint,request, render_template, flash,session,redirect,url_for
from flask.views import MethodView
from interface_test.case_group.models import *
from interface_test.case_group.DB.InsertCaseGroupSingle import *
from interface_test.case_group.DB.UpdataCaseGroupSingle import *
from interface_test.case_group.tools.judge_submit import *
from interface_test.case_group.tools.other_tools import *

Blue_case_group = Blueprint("case_group", __name__)

class CasegroupList(MethodView):
    def __init__(self):
        self.ins_CaseGroupListFrom = CaseGroupListForm(request.form)

    def get(self,product_name,page_no,offset,limit,case_group_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        self.ins_CaseGroupListFrom.product_name.choices = GetProductNameList()
        page_no = int(page_no)
        offset = int(offset)
        limit = int(limit)
        if product_name == '全部项目':
            total_pages = count_total_pages(limit)
        else:
            total_pages = count_total_pages_product_name(product_name,limit)
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
            case_group_list = GetCaseGroupList(offset,limit)
        else:
            case_group_list = GetCaseGroupList_product_name(product_name,offset,limit)
        return render_template("interface_test/case_group/case_group_list.html", form=self.ins_CaseGroupListFrom,data_list=case_group_list,product_name=product_name,page_no=page_no,total_pages=total_pages,offset=offset,limit=limit,case_group_id=case_group_id)

    def post(self,product_name,page_no,offset,limit,case_group_id):
        self.ins_CaseGroupListFrom.product_name.choices = GetProductNameList()
        limit = int(limit)
        if self.ins_CaseGroupListFrom.search_sub.data == 1: # 点击搜索按钮
            product_name = self.ins_CaseGroupListFrom.product_name.data
            case_group_id = case_group_id
            offset = 0
            total_pages = count_total_pages_product_name(product_name,limit)
            case_group_list = GetCaseGroupList_product_name(product_name, offset, limit)
            return render_template("interface_test/case_group/case_group_list.html", form=self.ins_CaseGroupListFrom,data_list=case_group_list,product_name=product_name,page_no=1,total_pages=total_pages,offset=offset,limit=limit,case_group_id=case_group_id)
        if self.ins_CaseGroupListFrom.delete_sub.data == 1: # 点击删除按钮
            page_no = int(page_no)
            offset = int(offset)
            limit = int(limit)
            case_group_id = self.ins_CaseGroupListFrom.get_id.data
            DeleteCaseGroup(case_group_id)
            if product_name == "全部项目":
                total_pages = count_total_pages(limit)
                if page_no > total_pages:
                    offset -= limit
                    page_no -= 1
                case_group_list = GetCaseGroupList(offset, limit)
            else:
                total_pages = count_total_pages_product_name(product_name, limit)
                if page_no > total_pages:
                    offset -= limit
                    page_no -= 1
                case_group_list = GetCaseGroupList_product_name(product_name, offset, limit)
            flash("删除成功；")
            return render_template("interface_test/case_group/case_group_list.html", form=self.ins_CaseGroupListFrom,data_list=case_group_list,product_name=product_name,page_no=1,total_pages=total_pages,offset=offset,limit=limit,case_group_id=case_group_id)

Blue_case_group.add_url_rule("/interface_test/case_group/case_group_list/<product_name>/<page_no>/<offset>/<limit>/<case_group_id>",view_func=CasegroupList.as_view("case_group_list"))


class CaseGroupNEC(MethodView):
    def __init__(self):
        self.ins_CaseGroupNEC_From = CaseGroupCreatEditCopyForm(request.form)

    def get(self,product_name,page_no,offset,limit,type,case_group_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        if type == "N":
            self.ins_CaseGroupNEC_From.product_name.choices = GetProductNameList()
        if type == "E" or type == "C":
            self.ins_CaseGroupNEC_From.product_name.choices = GetProductNameList()
            self.ins_CaseGroupNEC_From.product_name.data = product_name
            self.ins_CaseGroupNEC_From.case_group_name.data = GetCaseGroupNameByCaseGroupId(case_group_id)
            self.ins_CaseGroupNEC_From.case_group_order.data = GetCaseGroupOrder(case_group_id)
            self.ins_CaseGroupNEC_From.case_group_type.data = GetCaseGroupType(case_group_id)
            self.ins_CaseGroupNEC_From.case_group_explain.data = GetCaseGroupExplain(case_group_id)
        return render_template("interface_test/case_group/case_group_NEC.html", form=self.ins_CaseGroupNEC_From,
                               product_name=product_name, page_no=page_no, offset=offset, limit=limit, type=type,
                               case_group_id=case_group_id)

    def post(self,product_name,page_no,offset,limit,type,case_group_id):
        case_group_id = int(case_group_id)
        if self.ins_CaseGroupNEC_From.submit_sub.data == 1: # 点击提交按钮
            product_name = self.ins_CaseGroupNEC_From.product_name.data
            is_run = self.ins_CaseGroupNEC_From.is_run.data
            case_group_name = self.ins_CaseGroupNEC_From.case_group_name.data
            if type == "E":
                case_group_order = self.ins_CaseGroupNEC_From.case_group_order.data
            elif type =="N" or type == "C":
                case_group_order = "AUTO"
            case_group_type = self.ins_CaseGroupNEC_From.case_group_type.data
            case_group_explain = self.ins_CaseGroupNEC_From.case_group_explain.data
            judge_submit_result = judge_submit(type, case_group_id, product_name, case_group_name, case_group_order, case_group_type,case_group_explain)

            if judge_submit_result != 1:
                self.ins_CaseGroupNEC_From.product_name.choices = GetProductNameList()
                flash(judge_submit_result)
                return render_template("interface_test/case_group/case_group_NEC.html", form=self.ins_CaseGroupNEC_From,
                                       product_name=product_name, page_no=page_no, offset=offset, limit=limit,
                                       type=type, case_group_id=case_group_id)

            elif judge_submit_result == 1:
                if case_group_order != "AUTO":
                    case_group_order = int(case_group_order)
                self.ins_CaseGroupNEC_From.product_name.choices = GetProductNameList()
                if type == "N":
                    InsertCaseGroupSingle(product_name, is_run,case_group_name, case_group_type, case_group_explain)
                    flash("新增用例组成功；")
                elif type == "E":
                    UpdataCaseGroupSingle(product_name, is_run, case_group_id, case_group_name, case_group_order,case_group_type, case_group_explain)
                    flash("编辑用例组成功；")
                elif type == "C":
                    InsertCaseGroupSingle(product_name, is_run, case_group_name, case_group_type, case_group_explain)
                    flash("复制新增用例组成功；")
                return render_template("interface_test/case_group/case_group_NEC.html", form=self.ins_CaseGroupNEC_From,
                                       product_name=product_name, page_no=page_no, offset=offset, limit=limit,
                                       type=type, case_group_id=case_group_id)

Blue_case_group.add_url_rule("/interface_test/case_group/case_group_NEC/<product_name>/<page_no>/<offset>/<limit>/<type>/<case_group_id>",view_func=CaseGroupNEC.as_view("case_group_NEC"))