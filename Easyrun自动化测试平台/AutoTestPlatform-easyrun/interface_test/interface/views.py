# coding = utf-8
from flask import Blueprint,request, render_template, flash,session,redirect,url_for
from flask.views import MethodView
from interface_test.interface.models import *
from interface_test.interface.tools.other_tools import *
from interface_test.interface.tools.judge_submit import *
from interface_test.interface.DB.InsertInterfaceSingle import *
from interface_test.interface.DB.UpdateInterfaceSingle import *

Blue_interface = Blueprint("interface", __name__)

class InterfaceList(MethodView):
    def __init__(self):
        self.ins_InterfaceListForm = InterfaceListForm(request.form)

    def get(self,product_name,page_no,offset,limit,interface_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        self.ins_InterfaceListForm.product_name.choices = GetProductNameList()
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
            interface_list = GetInterfaceList(offset, limit)
        else:
            interface_list = GetInterfaceList_product_name(product_name, offset, limit)
        return render_template("interface_test/interface/interface_list.html", form=self.ins_InterfaceListForm,
                               data_list=interface_list, product_name=product_name, page_no=page_no,
                               total_pages=total_pages, offset=offset, limit=limit, interface_id=interface_id)

    def post(self,product_name,page_no,offset,limit,interface_id):
        page_no = int(page_no)
        offset = int(offset)
        limit = int(limit)
        product_name = self.ins_InterfaceListForm.product_name.data
        self.ins_InterfaceListForm.product_name.choices = GetProductNameList()
        limit = int(limit)
        if self.ins_InterfaceListForm.search_sub.data == 1:  # 点击搜索按钮
            product_name = self.ins_InterfaceListForm.product_name.data
            interface_id = interface_id
            offset = 0
            total_pages = count_total_pages_product_name(product_name, limit)
            case_group_list = GetInterfaceList_product_name(product_name, offset, limit)
            return render_template("interface_test/interface/interface_list.html", form=self.ins_InterfaceListForm,
                                   data_list=case_group_list, product_name=product_name, page_no=1,
                                   total_pages=total_pages, offset=offset, limit=limit, interface_id=interface_id)
        if self.ins_InterfaceListForm.delete_sub.data == 1:  # 点击删除按钮
            page_no = int(page_no)
            offset = int(offset)
            limit = int(limit)
            interface_id = self.ins_InterfaceListForm.get_id.data
            DeleteInterface(interface_id)
            if product_name == "全部项目":
                total_pages = count_total_pages(limit)
                if page_no > total_pages:
                    offset -= limit
                    page_no -= 1
                InterfaceList = GetInterfaceList(offset, limit)
            else:
                total_pages = count_total_pages_product_name(product_name, limit)
                if page_no > total_pages:
                    offset -= limit
                    page_no -= 1
                InterfaceList = GetInterfaceList_product_name(product_name, offset, limit)
            flash("删除成功；")
            return render_template("interface_test/interface/interface_list.html", form=self.ins_InterfaceListForm,
                                   data_list=InterfaceList, product_name=product_name, page_no=1,
                                   total_pages=total_pages, offset=offset, limit=limit, interface_id=interface_id)

Blue_interface.add_url_rule("/interface_test/interface/interface_list/<product_name>/<page_no>/<offset>/<limit>/<interface_id>",view_func=InterfaceList.as_view("interface_list"))


class Interface_NEC(MethodView):
    def __init__(self):
        self.ins_InterfaceNEC_Form = InterfaceNEC_Form(request.form)

    def get(self,product_name,page_no,offset,limit,type,interface_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        if type == "N":
            self.ins_InterfaceNEC_Form.product_name.choices = GetProductNameList()
        if type == "E" or type == "C":
            self.ins_InterfaceNEC_Form.product_name.choices = GetProductNameList()
            self.ins_InterfaceNEC_Form.interface_name.data = product_name
            self.ins_InterfaceNEC_Form.interface_name.data = GetInterfaceNameByInterfaceId(interface_id)
            self.ins_InterfaceNEC_Form.interface_order.data = GetInterfaceOrderByInterfaceId(interface_id)
            self.ins_InterfaceNEC_Form.interface_address.data = GetInterfaceAddressByInterfaceId(interface_id)
            self.ins_InterfaceNEC_Form.interface_method.data = GetMethodByInterfaceId(interface_id)
            self.ins_InterfaceNEC_Form.interface_explain.data = GetInterfaceExplainByInterfaceId(interface_id)
        return render_template("interface_test/interface/interface_NVEC.html", form=self.ins_InterfaceNEC_Form,
                               product_name=product_name, page_no=page_no, offset=offset, limit=limit, type=type,
                               interface_id=interface_id)

    def post(self,product_name,page_no,offset,limit,type,interface_id):
        if self.ins_InterfaceNEC_Form.submit_sub.data == 1:
            product_name = self.ins_InterfaceNEC_Form.product_name.data
            interface_name = self.ins_InterfaceNEC_Form.interface_name.data
            if type == "E":
                interface_order = self.ins_InterfaceNEC_Form.interface_order.data
            elif type =="N" or type == "C":
                interface_order = "AUTO"
            interface_method = self.ins_InterfaceNEC_Form.interface_method.data
            interface_address = self.ins_InterfaceNEC_Form.interface_address.data
            interface_explain = self.ins_InterfaceNEC_Form.interface_explain.data

            judge_submit_result = judge_submit(type,interface_id,product_name,interface_name,interface_order,interface_address,interface_method,interface_explain)
            if judge_submit_result != 1:
                self.ins_InterfaceNEC_Form.product_name.choices = GetProductNameList()
                flash(judge_submit_result)
                return render_template("interface_test/interface/interface_NVEC.html",form=self.ins_InterfaceNEC_Form,
                                       product_name=product_name, page_no=page_no, offset=offset, limit=limit,type=type,
                                       interface_id=interface_id)
            elif judge_submit_result == 1:
                if interface_order != "AUTO":
                    interface_order = int(interface_order)
                self.ins_InterfaceNEC_Form.product_name.choices = GetProductNameList()
                if type == "N":
                    InsertInterfaceSingle(product_name,interface_name,interface_address,interface_method,interface_explain)
                    flash("新增接口成功；")
                elif type == "E":
                    UpdataInterfaceSingle(product_name,interface_id,interface_name,interface_order,interface_address,interface_method,interface_explain)
                    flash("编辑接口成功；")
                elif type == "C":
                    InsertInterfaceSingle(product_name,interface_name,interface_address,interface_method,interface_explain)
                    flash("复制新增接口成功；")
                return render_template("interface_test/interface/interface_NVEC.html", form=self.ins_InterfaceNEC_Form,
                                       product_name=product_name, page_no=page_no, offset=offset, limit=limit,
                                       type=type, interface_id=interface_id)

Blue_interface.add_url_rule("/interface_test/interface/interface_NVEC/<product_name>/<page_no>/<offset>/<limit>/<type>/<interface_id>",view_func=Interface_NEC.as_view("interface_NEC"))
