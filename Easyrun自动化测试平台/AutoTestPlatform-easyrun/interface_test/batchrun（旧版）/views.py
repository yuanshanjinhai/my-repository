# coding = utf-8
from flask import Blueprint,request, render_template, flash,send_from_directory
from flask.views import MethodView
from GeneralTools.AllPath import *
from interface_test.batchrun.models import *
from interface_test.batchrun.run_case import *
from interface_test.batchrun.tools.check_case import *
from interface_test.batchrun.tools.GetExcelCase import *
from interface_test.batchrun.tools.other_tools import JugeCaseFileSuffix,delete_run_result
import os

Blue_easyrun = Blueprint("batchrun（旧版）", __name__)

class CaseEasyrun(MethodView):
    def __init__(self):
        self.ins_batchrunFrom = BatchrunForm(request.form)

    def get(self,username,token):
        return render_template("interface_test/run_case_list.html",form=self.ins_batchrunFrom,username=username,token=token)

    def post(self,username,token):
        if self.ins_batchrunFrom.upload_sub.data == 1:# 点击上传用例按钮
            upload_file = request.files.get('select_file')  # 获取文件对象
            file_name = upload_file.filename  # 获取文件名称
            if file_name == "":
                flash("请选择附件！2")
                return render_template("interface_test/run_case_list.html", form=self.ins_batchrunFrom,username=username,token=token)
            elif JugeCaseFileSuffix(file_name) == 0:
                flash("只能上传.xlsx格式的文件！0")
                return render_template("interface_test/run_case_list.html", form=self.ins_batchrunFrom,username=username,token=token)
            new_file_name = username + ".xlsx"
            upload_file.save(os.path.join(UploadCaseFile_path , new_file_name))
            # excel_case_path = os.path.join(UploadCaseFile_path, new_file_name)
            flash("用例上传成功！1")
            return render_template("interface_test/run_case_list.html", form=self.ins_batchrunFrom,username=username,token=token)

        if self.ins_batchrunFrom.check_case_sub.data == 1: # 点击校验用例按钮
            file_list = os.listdir(UploadCaseFile_path)
            if username + ".xlsx" not in file_list:
                flash("请选择附件！0")
                return render_template("interface_test/run_case_list.html", form=self.ins_batchrunFrom,username=username,token=token)
            excel_case_path = os.path.join(UploadCaseFile_path, username + ".xlsx")
            check_case_result = check_case(excel_case_path)
            if check_case_result == 1:
                flash("用例格式无误！1")
                return render_template("interface_test/run_case_list.html", form=self.ins_batchrunFrom,username=username,token=token)
            else:
                flash(check_case_result + "0")
                return render_template("interface_test/run_case_list.html", form=self.ins_batchrunFrom,username=username,token=token)

        if self.ins_batchrunFrom.run_case_sub.data == 1: # 点击用例执行按钮
            all_case_list = GetExcelCase(username + ".xlsx")
            is_urldecode = self.ins_batchrunFrom.is_urldecode.data
            excel_case_path = os.path.join(UploadCaseFile_path, username + ".xlsx")
            delete_run_result(excel_case_path)
            check_r = check_case(excel_case_path)  # 检查用例格式
            if check_r == 1:
                pass
            elif check_r != 1:
                flash(check_r + "0")
                return render_template("interface_test/run_case_list.html", form=self.ins_batchrunFrom, username=username, token=token)
            RunCase(all_case_list,username,excel_case_path,is_urldecode)
            flash("用例执行完毕，请检查结果！2")
            return render_template("interface_test/run_case_list.html", form=self.ins_batchrunFrom,username=username,token=token)

        if self.ins_batchrunFrom.download_execute_sub.data == 1: # 点击下载执行结果按钮
            return send_from_directory(UploadCaseFile_path, username + ".xlsx", as_attachment=True)

        if self.ins_batchrunFrom.download_template_sub.data == 1: # 点击下载模板按钮
            return send_from_directory(CaseTemplete_path, "case_template.xlsx", as_attachment=True)

Blue_easyrun.add_url_rule("/batch_run/<username>/<token>/",view_func=CaseEasyrun.as_view("easyrun_main"))

if __name__ == '__main__':
    username = "guolini"
    print(os.path.join(UploadCaseFile_path, username + ".xlsx"))