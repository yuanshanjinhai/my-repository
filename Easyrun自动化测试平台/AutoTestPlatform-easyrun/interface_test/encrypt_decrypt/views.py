# coding = utf-8
from flask import Blueprint,request, render_template, flash, send_from_directory,session,redirect,url_for
from flask.views import MethodView
from interface_test.encrypt_decrypt.models import *
from interface_test.encrypt_decrypt.DB.InsertEncryptDecryptSingle import *
from interface_test.encrypt_decrypt.tools.other_tools import *
from GeneralTools.AllPath import encrypt_decrypt_load_path0, encrypt_decrypt_temlete_path
import os.path

Blue_encrypt_decrypt = Blueprint("encrypt_decrypt", __name__)

class EncryptDecryptList(MethodView):
    def __init__(self):
        self.ins_EncryptDecryptListFrom = EncryptDecryptListForm(request.form)

    def get(self,page_no,offset,limit,encrypt_decrypt_id):
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
        encrypt_decrypt_list = GetEncryptDecryptList(offset, limit)
        return render_template("interface_test/encrypt_decrypt/encrypt_decrypt_list.html", form=self.ins_EncryptDecryptListFrom,
                               data_list=encrypt_decrypt_list, page_no=page_no,
                               total_pages=total_pages, offset=offset, limit=limit, encrypt_decrypt_id=encrypt_decrypt_id)

    def post(self, page_no, offset, limit, encrypt_decrypt_id):
        limit = int(limit)
        if self.ins_EncryptDecryptListFrom.search_sub.data == 1:  # 点击搜索按钮
            # encrypt_decrypt_id = encrypt_decrypt_id
            offset = 0
            total_pages = count_total_pages(limit)
            encrypt_decrypt_list = GetEncryptDecryptList(offset, limit)
            return render_template("interface_test/encrypt_decrypt/encrypt_decrypt_list.html", form=self.ins_EncryptDecryptListFrom,
                                   data_list=encrypt_decrypt_list, page_no=1,
                                   total_pages=total_pages, offset=offset, limit=limit, encrypt_decrypt_id=encrypt_decrypt_id)

        if self.ins_EncryptDecryptListFrom.upload_sub.data == 1: # 点击上传按钮
            encrypt_decrypt_id = encrypt_decrypt_id
            offset = 0
            total_pages = count_total_pages(limit)
            encrypt_decrypt_list = GetEncryptDecryptList(offset, limit)
            upload_file_obj = request.files.get('select_file')  # 获取文件对象
            file_name = upload_file_obj.filename  # 获取文件名称
            if file_name == "":
                flash("请选择附件")
                return render_template("interface_test/encrypt_decrypt/encrypt_decrypt_list.html", form=self.ins_EncryptDecryptListFrom,
                                   data_list=encrypt_decrypt_list, page_no=1,total_pages=total_pages, offset=offset, limit=limit,
                                    encrypt_decrypt_id=encrypt_decrypt_id)
            else:
                if JugeCaseFileSuffix(file_name) == 0:
                    flash("请上传.py格式的文件")
                    return render_template("interface_test/encrypt_decrypt/encrypt_decrypt_list.html", form=self.ins_EncryptDecryptListFrom,
                                       data_list=encrypt_decrypt_list, page_no=1,total_pages=total_pages, offset=offset,
                                           limit=limit, encrypt_decrypt_id=encrypt_decrypt_id)
                else:
                    if jugde_encrypt_decrypt_DirFilename_is_exist(file_name) == 0:
                        flash("该文件已存在")
                        return render_template("interface_test/encrypt_decrypt/encrypt_decrypt_list.html",form=self.ins_EncryptDecryptListFrom,
                                               data_list=encrypt_decrypt_list,page_no=1,total_pages=total_pages,
                                               offset=offset, limit=limit,encrypt_decrypt_id=encrypt_decrypt_id)
                    else:
                        upload_file_obj.save(os.path.join(encrypt_decrypt_load_path0 , file_name))
                        InsertEncryptDecryptSingle(file_name)
                        flash("文件上传成功")
                        encrypt_decrypt_list = GetEncryptDecryptList(offset, limit)
                        return render_template("interface_test/encrypt_decrypt/encrypt_decrypt_list.html", form=self.ins_EncryptDecryptListFrom,
                                           data_list=encrypt_decrypt_list,page_no=1,total_pages=total_pages, offset=offset,
                                               limit=limit, encrypt_decrypt_id=encrypt_decrypt_id)

        if self.ins_EncryptDecryptListFrom.download_template_sub.data == 1: # 点击下载模板按钮
            return send_from_directory(encrypt_decrypt_temlete_path, "encrypt_decrypt.py", as_attachment=True)

        if self.ins_EncryptDecryptListFrom.delete_sub.data == 1: # 点击删除按钮
            encrypt_decrypt_id = self.ins_EncryptDecryptListFrom.get_id.data
            file_name = GetFileNameByEncryptDecrypt(encrypt_decrypt_id)
            delete_file(file_name)
            DeleteEncryptDecrypt(encrypt_decrypt_id)
            total_pages = count_total_pages(limit)
            flash("文件删除成功")
            encrypt_decrypt_list = GetEncryptDecryptList(offset, limit)
            return render_template("interface_test/encrypt_decrypt/encrypt_decrypt_list.html",form=self.ins_EncryptDecryptListFrom,
                                   data_list=encrypt_decrypt_list, page_no=1,total_pages=total_pages,
                                   offset=offset, limit=limit,encrypt_decrypt_id=encrypt_decrypt_id)


Blue_encrypt_decrypt.add_url_rule("/interface_test/encrypt_decrypt/encrypt_decrypt_list/<page_no>/<offset>/<limit>/<encrypt_decrypt_id>",view_func=EncryptDecryptList.as_view("encrypt_decrypt_list"))
