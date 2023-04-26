# coding = utf-8
from flask import Blueprint,request, render_template, flash,session,redirect,url_for
from flask.views import MethodView
from admin.product.models import *
from admin.product.DB.OtherDB import *
from admin.product.DB.InsertProduct import *
from admin.product.DB.UpdateProduct import *
from admin.product.DB.DeleteProduct import *
from admin.product.tools.other_tools import count_total_pages,GetProductList
from admin.product.tools.judge_submit import *

Blue_product = Blueprint("product", __name__)

class ProductList(MethodView):
    def __init__(self):
        self.ins_ProductListForm = ProductListForm(request.form)

    def get(self,page_no,offset,limit,product_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        page_no = int(page_no)
        offset = int(offset)
        limit = int(limit)
        total_pages = count_total_pages(limit)
        if total_pages == 1:
            offset = 0
            page_no = 1
        elif page_no <= 0:
            offset = 0
            page_no = 1
        elif page_no > total_pages:
            offset -= limit
            page_no = total_pages
        product_list = GetProductList(offset, limit)
        return render_template("admin/product/product_list.html", form=self.ins_ProductListForm, data_list=product_list,
                               page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, product_id=product_id)

    def post(self,page_no,offset,limit,product_id):
        search_product_name = self.ins_ProductListForm.product_name_inputbox.data
        if self.ins_ProductListForm.product_name_inputbox.data == 1:
            if search_product_name == "":
                page_no = int(page_no)
                offset = int(offset)
                limit = int(limit)
                total_pages = count_total_pages(limit)
                if total_pages == 1:
                    offset = 0
                    page_no = 1
                elif page_no <= 0:
                    offset = 0
                    page_no = 1
                elif page_no > total_pages:
                    offset -= limit
                    page_no = total_pages
                product_list = GetProductList(offset, limit)
                flash("请输入项目名称；")
                return render_template("admin/product/product_list.html", form=self.ins_ProductListForm, data_list=product_list,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, product_id=product_id)
            else:
                page_no = int(page_no)
                offset = int(offset)
                limit = int(limit)
                total_pages = count_total_pages(limit)
                if total_pages == 1:
                    offset = 0
                    page_no = 1
                elif page_no <= 0:
                    offset = 0
                    page_no = 1
                elif page_no > total_pages:
                    offset -= limit
                    page_no = total_pages
                product_list = SearchGetProductList(search_product_name, offset, limit)
                return render_template("admin/product/product_list.html", form=self.ins_ProductListForm,data_list=product_list,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, product_id=product_id)

        if self.ins_ProductListForm.delete_sub.data == 1:
            product_id = self.ins_ProductListForm.get_id.data
            page_no = int(page_no)
            offset = int(offset)
            limit = int(limit)
            total_pages = count_total_pages(limit)
            DeleteProduct(product_id)
            product_list = GetProductList(offset, limit)
            flash("删除项目成功；")
            return render_template("admin/product/product_list.html", form=self.ins_ProductListForm, data_list=product_list,
                                   page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, product_id=product_id)

Blue_product.add_url_rule("/admin/product/product_list/<page_no>/<offset>/<limit>/<product_id>",view_func=ProductList.as_view("product_list"))


class ProductNE(MethodView):
    def __init__(self):
        self.ins_ProductNEForm = ProductNEForm(request.form)

    def get(self,page_no,offset,limit,type,product_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        if type == "N":
            return render_template("admin/product/product_NE.html", form=self.ins_ProductNEForm, page_no=page_no, offset=offset,
                                   limit=limit, type=type, product_id=product_id)
        if type == "E":
            product_name = GetProductName(product_id)
            product_abbreviation = GetProductAbbreviation(product_id)
            product_explain = GetProductExplain(product_id)
            self.ins_ProductNEForm.product_name.data = product_name
            self.ins_ProductNEForm.product_abbreviation.data = product_abbreviation
            self.ins_ProductNEForm.product_explain.data = product_explain
        return render_template("admin/product/product_NE.html", form=self.ins_ProductNEForm, page_no=page_no, offset=offset,
                                   limit=limit, type=type, product_id=product_id)

    def post(self,page_no,offset,limit,type,product_id):
        if self.ins_ProductNEForm.submit_sub.data == 1:
            product_name = self.ins_ProductNEForm.product_name.data
            product_abbreviation = self.ins_ProductNEForm.product_abbreviation.data
            product_explain = self.ins_ProductNEForm.product_explain.data
            if type == "N":
                judge_submit_r = judge_submit("N",product_name, product_abbreviation, product_explain)
                if judge_submit_r != 1:
                    flash(judge_submit_r)
                    return render_template("admin/product/product_NE.html", form=self.ins_ProductNEForm, page_no=page_no, offset=offset,
                                           limit=limit, type=type, product_id=product_id)
                if judge_submit_r == 1:
                    flash("新增项目成功；")
                    InsertProduct(product_name, product_abbreviation, product_explain)
                    return render_template("admin/product/product_NE.html", form=self.ins_ProductNEForm, page_no=page_no, offset=offset,
                                           limit=limit, type=type, product_id=product_id)
            if type == "E":
                judge_submit_r = judge_submit("E",product_name, product_abbreviation, product_explain)
                if judge_submit_r != 1:
                    flash(judge_submit_r)
                    return render_template("admin/product/product_NE.html", form=self.ins_ProductNEForm, page_no=page_no, offset=offset,
                                           limit=limit, type=type, product_id=product_id)
                if judge_submit_r == 1:
                    flash("编辑项目成功；")
                    UpdateProduct(product_id, product_name, product_abbreviation, product_explain)
                    return render_template("admin/product/product_NE.html", form=self.ins_ProductNEForm, page_no=page_no, offset=offset,
                                           limit=limit, type=type, product_id=product_id)

Blue_product.add_url_rule("/admin/product/product_NE/<page_no>/<offset>/<limit>/<type>/<product_id>",view_func=ProductNE.as_view("product_NE"))