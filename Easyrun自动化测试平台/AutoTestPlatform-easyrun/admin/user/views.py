# coding = utf-8
from flask import Blueprint,request, render_template, flash,session,redirect,url_for
from flask.views import MethodView
from  admin.user.models import *
from admin.user.tools.other_tools import *
from admin.user.DB.InsertUserAndUserRole import *
from admin.user.DB.UpdateUserAndUserRole import *
from admin.user.DB.DeleteUserAndUserRole import *
from admin.user.tools.judge_submit import *

Blue_user = Blueprint("user", __name__)

class UserList(MethodView):
    def __init__(self):
        self.ins_UserListForm = UserListForm(request.form)

    def get(self,page_no,offset,limit,user_id):
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
        user_list = GetUserList(offset, limit)
        return render_template("admin/user/user_list.html", form=self.ins_UserListForm, data_list=user_list,
                               page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, user_id=user_id)

    def post(self,page_no,offset,limit,user_id):
        page_no = int(page_no)
        offset = int(offset)
        limit = int(limit)
        if self.ins_UserListForm.search_sub.data == 1:
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
            user_name = self.ins_UserListForm.user_name_inputbox.data
            user_list = SearchGetUserList(user_name, offset, limit)
            return render_template("admin/user/user_list.html", form=self.ins_UserListForm, data_list=user_list,
                                   page_no=page_no, total_pages=total_pages, offset=offset, limit=limit,user_id=user_id)

        if self.ins_UserListForm.delete_sub.data == 1:
            user_id = self.ins_UserListForm.get_id.data
            DeleteUserAndUserRole(user_id)
            total_pages = count_total_pages(limit)
            user_list = GetUserList(offset, limit)
            flash("删除用户成功；")
            return render_template("admin/user/user_list.html", form=self.ins_UserListForm, data_list=user_list,
                                   page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, user_id=user_id)

Blue_user.add_url_rule("/admin/user/user_list/<page_no>/<offset>/<limit>/<user_id>",view_func=UserList.as_view("user_list"))


class UserNE(MethodView):
    def __init__(self):
        self.ins_UserNEForm = UserNEForm(request.form)

    def get(self,page_no,offset,limit,type,user_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        if type == "N":
            self.ins_UserNEForm.role.choices = GetRoleList_()
            return render_template("admin/user/user_NE.html", form=self.ins_UserNEForm,page_no=page_no, offset=offset,
                                   limit=limit, type=type, user_id=user_id)
        if type == "E":
            self.ins_UserNEForm.user_login_name.data = GetUserLoginName(user_id)
            self.ins_UserNEForm.user_name.data = GetUserName(user_id)
            self.ins_UserNEForm.role.choices = GetRoleList_()
            self.ins_UserNEForm.role.data = GetRole(user_id)
            return render_template("admin/user/user_NE.html", form=self.ins_UserNEForm, page_no=page_no, offset=offset,
                                   limit=limit, type=type, user_id=user_id)

    def post(self,page_no,offset,limit,type,user_id):
            if self.ins_UserNEForm.submit_sub.data == 1:
                self.ins_UserNEForm.role.choices = GetRoleList_()
                user_login_name = self.ins_UserNEForm.user_login_name.data
                user_name = self.ins_UserNEForm.user_name.data
                old_password = 0
                new_password = 0
                if type == "E" and self.ins_UserNEForm.is_update_password.data == "是":
                    old_password = GetPassword(user_login_name)
                    new_password = self.ins_UserNEForm.new_password.data
                role = self.ins_UserNEForm.role.data
                judeg_r = judge_submit(type,old_password,new_password,user_login_name,user_name,role)
                if judeg_r != 1:
                    flash(judeg_r)
                    return render_template("admin/user/user_NE.html", form=self.ins_UserNEForm, page_no=page_no,
                                           offset=offset, limit=limit, type=type, user_id=user_id)
                else:
                    if type == "N":
                        InsertUserAndUserRole(user_login_name,user_name,role)
                        flash("创建用户成功；")
                    if type == "E" and new_password ==0:
                        UpdateUserAndUserRole(new_password, user_login_name, user_name, role)
                    elif type == "E" and new_password !=0:
                        UpdateUserAndUserRole(md5_encrypt(new_password), user_login_name, user_name, role)
                    flash("编辑用户成功；")
                    return render_template("admin/user/user_NE.html", form=self.ins_UserNEForm, page_no=page_no,
                                           offset=offset, limit=limit, type=type, user_id=user_id)


Blue_user.add_url_rule("/admin/user/user_NE/<page_no>/<offset>/<limit>/<type>/<user_id>",view_func=UserNE.as_view("user_NE"))
