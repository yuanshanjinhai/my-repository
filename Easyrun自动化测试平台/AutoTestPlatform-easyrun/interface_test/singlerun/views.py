# coding = utf-8
from flask import Blueprint,request, render_template, flash,session,redirect,url_for
from flask.views import MethodView
from GeneralTools.AllPath import *
from GeneralTools.UrlcodeAndPwd import *
from GeneralTools.OtherTools import get_encypt_decrypt_file,check_case,encrypt_decrypt
from interface_test.singlerun.models import *
from interface_test.singlerun.run_interface import *
from interface_test.singlerun.tools import *

Blue_singlerun = Blueprint("singlerun", __name__)

class Singlerun(MethodView):
    def __init__(self):
        self.ins_singlerunFrom = SinglerunForm(request.form)

    def get(self):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        # resource_list0 = ["interface", "tools", "help"]
        # resource_list = resource_list0
        self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
        return render_template("/interface_test/single.html",form = self.ins_singlerunFrom)

    def post(self):
        # if self.ins_singlerunFrom.upload_sub_PwdAndUnpwd.data == 1:# 点击上传加解密文件按钮
        #     upload_file = request.files.get('select_file1_PwdAndUnpwd')  # 获取文件对象
        #     file_name = upload_file.filename  # 获取文件名称
        #     if file_name == "":
        #         flash("请选择附件！2")
        #         return render_template("interface_test/single.html", form=self.ins_singlerunFrom)
        #     elif JugeCaseFileSuffix(file_name) == 0:
        #         flash("只能上传.py格式的文件！0")
        #         return render_template("interface_test/single.html", form=self.ins_singlerunFrom)
        #     new_file_name = username + ".py"
        #     upload_file.save(os.path.join(UploadPwdFile_path, new_file_name))
        #     flash("加解密文件上传成功！1")
        #     return render_template("interface_test/single.html", form=self.ins_singlerunFrom)
        #
        # if self.ins_batchrunFrom.download_template_sub.data == 1:  # 点击下载模板按钮
        #     return send_from_directory(PwdTemlete_path, "encrypt_decrypt.py", as_attachment=True)

        if self.ins_singlerunFrom.run_sub.data == 1: # 点击执行按钮
            method = self.ins_singlerunFrom.method.data
            urlcode_pwd = self.ins_singlerunFrom.is_urlencode_pwd.data
            file_name = self.ins_singlerunFrom.encrypt_decrypt_file.data
            address = self.ins_singlerunFrom.address.data
            header = self.ins_singlerunFrom.heaer.data
            body = self.ins_singlerunFrom.body.data

            check_r = check_case(header, body)
            if check_r == 1:
                pass
            elif check_r != 1:
                flash(check_r + "0")
                self.ins_singlerunFrom.response.data = ""
                self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                return render_template("/interface_test/single.html", form=self.ins_singlerunFrom)
            if address == "":
                flash("请输入地址！0")
                self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                return render_template("/interface_test/single.html", form=self.ins_singlerunFrom)
            if (urlcode_pwd == "1" or urlcode_pwd == "3" or urlcode_pwd == "4") and method == "POST":
                body = url_encode(body)
            if urlcode_pwd == "2" or urlcode_pwd == "3":
                if os.path.exists(encrypt_decrypt_load_path0 + file_name) == 0:
                    flash("未上传加解密文件！0")
                    self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                    return render_template("/interface_test/single.html", form=self.ins_singlerunFrom)
                else:
                    ins_ende = encrypt_decrypt(file_name, body)
                    if ins_ende == 0:
                        flash("加解密类名称错误！0")
                        self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                        return render_template("/interface_test/single.html", form=self.ins_singlerunFrom)
                    else:
                        jr = hasattr(ins_ende,"encrypt")
                        if jr == 0:
                            flash("加密函数名称错误！0")
                            self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                            return render_template("/interface_test/single.html", form=self.ins_singlerunFrom)
                        elif jr == 1:
                            body = ins_ende.encryp()

            if method == "GET":
                actual_respone = run_interface_get(address,header)
                if self.ins_singlerunFrom.is_urlencode_pwd.data == "1" or self.ins_singlerunFrom.is_urlencode_pwd.data == "5":
                    actual_respone = url_decode(actual_respone)
                self.ins_singlerunFrom.response.data = actual_respone
                self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                return render_template("/interface_test/single.html",form = self.ins_singlerunFrom)
            if method == "POST":
                actual_respone = run_interface_post(address, header, body)
                if urlcode_pwd == "1" or urlcode_pwd == "3" or urlcode_pwd == "5":
                    actual_respone = url_decode(actual_respone)
                if urlcode_pwd == "2" or urlcode_pwd == "3":
                    ins_ende = encrypt_decrypt(file_name, body)
                    jr = hasattr(ins_ende, "decrypt")
                    if jr == 0:
                        flash("解密函数名称错误！0")
                        self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                        return render_template("/interface_test/single.html", form=self.ins_singlerunFrom)
                    elif jr == 1:
                        actual_respone = ins_ende.decrypt()
                self.ins_singlerunFrom.response.data = actual_respone
                self.ins_singlerunFrom.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                return render_template("/interface_test/single.html", form=self.ins_singlerunFrom)

Blue_singlerun.add_url_rule("/test_interface/single_run",view_func=Singlerun.as_view("singlerun_main"))