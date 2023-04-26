# coding = utf-8
from flask import Blueprint,request, render_template, flash,session,redirect,url_for
from flask.views import MethodView
from  admin.role.models import *
from admin.role.tools.other_tools import *
from admin.role.DB.InsertRoleAndRoleResource import *
from admin.role.DB.UpdateRoleAndRoleResource import *
from admin.role.DB.DeleteRoleAndRoleResource import *

Blue_role = Blueprint("role", __name__)

class RoleList(MethodView):
    def __init__(self):
        self.ins_RoleListForm = RoleListForm(request.form)

    def get(self,page_no,offset,limit,role_id):
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
        role_list = GetRoleList(offset, limit)
        return render_template("admin/role/role_list.html", form=self.ins_RoleListForm, data_list=role_list,
                               page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, role_id=role_id)

    def post(self,page_no,offset,limit,role_id):
        if self.ins_RoleListForm.search_sub.data == 1:
            role_name = self.ins_RoleListForm.role_name.data
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
            role_list = SearchRoleList(role_name,offset,limit)
            return render_template("admin/role/role_list.html", form=self.ins_RoleListForm, data_list=role_list,
                                   page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, role_id=role_id)
        if self.ins_RoleListForm.delete_sub.data == 1:
            role_id = self.ins_RoleListForm.get_id.data
            role_name = self.ins_RoleListForm.role_name.data
            DeleteRoleAndRoleResource(role_id)
            page_no = int(page_no)
            offset = int(offset)
            limit = int(limit)
            total_pages = count_total_pages(limit)
            role_list = SearchRoleList(role_name, offset, limit)
            flash("删除角色成功；")
            return render_template("admin/role/role_list.html", form=self.ins_RoleListForm, data_list=role_list,
                                   page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, role_id=0)

Blue_role.add_url_rule("/admin/role/role_list/<page_no>/<offset>/<limit>/<role_id>",view_func=RoleList.as_view("role_list"))


class RoleNE(MethodView):
    def __init__(self):
        self.ins_RoleNEForm = RoleNEForm(request.form)

    def get(self,page_no,offset,limit,type,role_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        if type == "N":
            resource_str = GetAllResourceStr()
            self.ins_RoleNEForm.resource_str.data = resource_str
        if type == "E":
            role_name = GetRoleName(role_id)
            resource_str = GetAllResourceStrByRoleId(role_id)
            self.ins_RoleNEForm.role_name.data = role_name
            self.ins_RoleNEForm.resource_str.data = resource_str
        return render_template("admin/role/role_NE.html", form=self.ins_RoleNEForm, page_no=page_no, offset=offset, limit=limit, role_id=role_id)

    def post(self,page_no,offset,limit,type,role_id):
        role_id = int(role_id)
        if self.ins_RoleNEForm.submit_sub.data == 1:
            role_name = self.ins_RoleNEForm.role_name.data
            resource_str = self.ins_RoleNEForm.resource_str.data
            resource_list = resource_str.split("；")
            jr = judge_submit(type,role_name,resource_list )
            if jr != 1:
                flash(jr)
                self.ins_RoleNEForm.resource_str.data = resource_str
                return render_template("admin/role/role_NE.html", form=self.ins_RoleNEForm, page_no=page_no,offset=offset, limit=limit, role_id=role_id)
            elif jr == 1:
                if type == "N":
                    InsertRoleAndRoleResource(role_name,resource_list)
                    flash("创建角色成功；")
                if type == "E":
                    UpdateRoleAndRoleResource(role_id,role_name,resource_list)
                    flash("更新角色成功；")
            return render_template("admin/role/role_NE.html", form=self.ins_RoleNEForm, page_no=page_no, offset=offset, limit=limit, role_id=role_id)

Blue_role.add_url_rule("/admin/role/role_NE/<page_no>/<offset>/<limit>/<type>/<role_id>",view_func=RoleNE.as_view("role_NE"))