# coding = utf-8
from flask import Blueprint,request, render_template, flash, session,redirect,url_for
from flask.views import MethodView
from interface_test.run_case.models import *
from GeneralTools.FormatTime import date_time
from interface_test.run_case.DB.OtherDB import GetProductNameList_Case_run,GetCaseRunList,GetCaseRunList_product_name
from interface_test.run_case.DB.GetRunCaseList import GetRunCaseList
from interface_test.run_case.DB.GlobalAdd import *
from interface_test.run_case.tools.other_tools import count_total_pages,count_total_pages_product_name
from interface_test.run_case.run.run_case_groupstart_and_end import *
from interface_test.run_case.run.run_case_groupbatch import run_case_groupbatch

Blue_run_case = Blueprint("run_case", __name__)

class CaseRunList(MethodView):
    def __init__(self):
        self.ins_CaseRunListForm = CaseRunListForm(request.form)

    def get(self,product_name,page_no,offset,limit,case_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        self.ins_CaseRunListForm.product_name.choices = GetProductNameList_Case_run()
        self.ins_CaseRunListForm.product_name.data = product_name
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
            case_run_list = GetCaseRunList(offset, limit)
        else:
            case_run_list = GetCaseRunList_product_name(product_name, offset, limit)
        return render_template("interface_test/run_case/run_case_list.html", form=self.ins_CaseRunListForm, data_list=case_run_list,
                               product_name=product_name, page_no=page_no, total_pages=total_pages, offset=offset,
                               limit=limit, case_id=case_id)

    def post(self, product_name, page_no, offset, limit, case_id):
        page_no = int(page_no)
        offset = int(offset)
        limit = int(limit)
        if self.ins_CaseRunListForm.search_sub.data == 1:
            product_name = self.ins_CaseRunListForm.product_name.data
            if product_name == "全部项目":
                total_pages = count_total_pages(limit)
                case_run_list = GetCaseRunList(offset, limit)
            else:
                total_pages = count_total_pages_product_name(product_name, limit)
                case_run_list = GetCaseRunList_product_name(product_name, offset, limit)
            self.ins_CaseRunListForm.product_name.choices = GetProductNameList_Case_run()
            return render_template("interface_test/run_case/run_case_list.html", form=self.ins_CaseRunListForm,
                                   data_list=case_run_list, product_name=product_name, page_no=page_no,
                                   total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)

        if self.ins_CaseRunListForm.run_case_sub.data == 1:
            product_name = self.ins_CaseRunListForm.product_name.data
            if product_name == "全部项目":
                flash("请选择项目；")
                total_pages = count_total_pages(limit)
                case_run_list = GetCaseRunList(offset, limit)
                self.ins_CaseRunListForm.product_name.choices = GetProductNameList_Case_run()
                return render_template("interface_test/run_case/run_case_list.html", form=self.ins_CaseRunListForm,
                                       data_list=case_run_list, product_name=product_name, page_no=page_no,
                                       total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)
            GlobalAdd(product_name)
            run_case_tuple0 = GetRunCaseList(product_name)
            run_time = date_time()
            run_case_tulpe = (run_case_tuple0[0],run_case_tuple0[1],run_case_tuple0[2],run_time)
            print('run_case_tulpe[0]=',run_case_tulpe[0])
            run_case_groupstart_and_end(run_case_tulpe[0],run_time)
            run_case_list = run_case_tulpe[1]
            run_case_groupbatch(run_case_list,run_time)
            run_case_groupstart_and_end(run_case_tulpe[2], run_time)
            flash("执行成功！")
            total_pages = count_total_pages(limit)
            case_run_list = GetCaseRunList(offset, limit)
            self.ins_CaseRunListForm.product_name.choices = GetProductNameList_Case_run()
            return render_template("interface_test/run_case/run_case_list.html", form=self.ins_CaseRunListForm,
                                   data_list=case_run_list, product_name=product_name, page_no=page_no,
                                   total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)

Blue_run_case.add_url_rule("/interface_test/run_case/run_case_list/<product_name>/<page_no>/<offset>/<limit>/<case_id>",view_func=CaseRunList.as_view("run_case_list"))
