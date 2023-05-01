# coding = utf-8
from flask import Blueprint,request, render_template, flash, send_from_directory,session,redirect,url_for
from flask.views import MethodView
from GeneralTools.AllPath import CaseTemplete_path,UploadAndDownloadCaseFile_path
from GeneralTools.OtherTools import get_encypt_decrypt_file
from interface_test.case.models import *
from interface_test.case.DB.InsertCaseSingle import *
from interface_test.case.DB.UpdataCaseSingle import *
from interface_test.case.DB.InsertCaseByExcelForBatchrun import *
from interface_test.case.DB.GetCaseByDB import GetCaseByDB
from interface_test.case.DB.DeleteCaseSingle import DeleteCaseSingle
from interface_test.case.tools.judge_submit import *
from interface_test.case.tools.other_tools import *
from interface_test.case.tools.into_excel_by_DB import *
from interface_test.case.tools.get_and_judge_excel_case import *
from interface_test.case.tools.judge_relation_single import *
import os
import shutil

Blue_case = Blueprint("case", __name__)

class CaseList(MethodView):
    def __init__(self):
        self.ins_CaseListForm = CaseListForm(request.form)

    def get(self,product_name,page_no,offset,limit,case_id):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
        self.ins_CaseListForm.product_name.data = product_name
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
            case_list = GetCaseList(offset, limit)
        else:
            case_list = GetCaseList_product_name(product_name, offset, limit)
        return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm,data_list=case_list,
                               product_name=product_name, page_no=page_no,total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)

    def post(self,product_name,page_no,offset,limit,case_id):
        page_no = int(page_no)
        offset = int(offset)
        limit = int(limit)
        if self.ins_CaseListForm.search_sub.data == 1:
            product_name = self.ins_CaseListForm.product_name.data
            if product_name == "全部项目":
                total_pages = count_total_pages(limit)
                case_list = GetCaseList(offset, limit)
            else:
                total_pages = count_total_pages_product_name(product_name, limit)
                case_list = GetCaseList_product_name(product_name, offset, limit)
            self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
            return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm, data_list=case_list, product_name=product_name,
                                   page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)

        if self.ins_CaseListForm.download_case_sub.data == 1: # 用例下载
            product_name = self.ins_CaseListForm.product_name.data
            if product_name == "全部项目":
                flash("请先选择项目并搜索结果；")
                total_pages = count_total_pages_product_name(product_name, limit)
                self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
                case_list = GetCaseList_product_name(product_name, offset, limit)
                return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm,
                                       data_list=case_list, product_name=product_name,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit,
                                       case_id=case_id)
            file_list = os.listdir(UploadAndDownloadCaseFile_path + product_name)
            if product_name + ".xlsx" in file_list: # 如果用例文件已存在，则证明已上传过了
                pass
            else: # 否则就是没上传过用例，即没有模板，这就需要把模板复制过来：先创建相关目录，再复制模板，再给模板改名
                os.makedirs(UploadAndDownloadCaseFile_path + product_name) # 判断目录是否存在，不存在则自动创建
                shutil.copyfile(CaseTemplete_path + "case_template.xlsx", UploadAndDownloadCaseFile_path + product_name)
                os.rename(UploadAndDownloadCaseFile_path + product_name + "case_template.xlsx", product_name + ".xlsx")
            data_list = GetCaseByDB(product_name)
            excel_dir =  UploadAndDownloadCaseFile_path + product_name
            excel_path = UploadAndDownloadCaseFile_path + product_name + "/" + product_name + ".xlsx"
            into_excel_by_DB(data_list,excel_path)
            return send_from_directory(excel_dir, product_name + ".xlsx", as_attachment=True)

        if self.ins_CaseListForm.download_template_sub.data == 1: # 模板下载
            return send_from_directory(CaseTemplete_path, "case_template.xlsx", as_attachment=True)

        if self.ins_CaseListForm.upload_sub.data == 1: # 用例上传
            product_name = self.ins_CaseListForm.product_name.data
            if product_name == "全部项目":
                flash("请先选择项目并搜索结果；")
                total_pages = count_total_pages_product_name(product_name, limit)
                self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
                case_list = GetCaseList_product_name(product_name, offset, limit)
                return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm,data_list=case_list, product_name=product_name,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)
            total_pages = count_total_pages_product_name(product_name, limit)
            self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()

            try: # 如果目录已存在，将会报错，所以要try
                os.makedirs(UploadAndDownloadCaseFile_path + product_name) # 判断目录是否存在，不存在则自动创建
            except:
                pass
            upload_file = request.files.get('select_file') # 获取文件上传对象
            file_name = upload_file.filename # 获取文件名称
            if file_name == "":
                flash("请选择附件；")
                total_pages = count_total_pages_product_name(product_name, limit)
                self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
                case_list = GetCaseList_product_name(product_name, offset, limit)
                return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm,data_list=case_list, product_name=product_name,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit,case_id=case_id)
            elif JugeCaseFileSuffix(file_name) == 0:
                flash("只能上传.xlsx格式的文件；")
                total_pages = count_total_pages_product_name(product_name, limit)
                self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
                case_list = GetCaseList_product_name(product_name, offset, limit)
                return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm, data_list=case_list, product_name=product_name,
                                page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)
            new_file_name = product_name + ".xlsx"
            upload_file.save(os.path.join(UploadAndDownloadCaseFile_path + product_name, new_file_name))
            excel_path = UploadAndDownloadCaseFile_path + product_name + "/" + product_name + ".xlsx"
            upload_case_list = get_and_judge_excel_case(excel_path)
            if isinstance(upload_case_list,str):
                flash(upload_case_list)
                total_pages = count_total_pages_product_name(product_name, limit)
                self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
                case_list = GetCaseList_product_name(product_name, offset, limit)
                return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm,data_list=case_list, product_name=product_name,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit,case_id=case_id)
            elif isinstance(upload_case_list,list):
                InsertCaseByExcelForBatchrun(product_name, upload_case_list)
                case_list = GetCaseList_product_name(product_name, offset, limit)
                flash("用例上传成功；")
                total_pages = count_total_pages_product_name(product_name, limit)
                self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
                case_list = GetCaseList_product_name(product_name, offset, limit)
                return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm, data_list=case_list, product_name=product_name,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)

        if self.ins_CaseListForm.delete_sub.data == 1:
            case_id = self.ins_CaseListForm.get_id.data
            judge_case_is_relationed_r = JudgeCaseIsRelationed(case_id)
            if judge_case_is_relationed_r == 1:
                flash("该用例被关联，不能删除；")
                total_pages = count_total_pages_product_name(product_name, limit)
                self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
                case_list = GetCaseList_product_name(product_name, offset, limit)
                return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm, data_list=case_list, product_name=product_name,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit, case_id=case_id)
            elif judge_case_is_relationed_r == 0:
                DeleteCaseSingle(case_id)
                flash("删除用例成功；")
                total_pages = count_total_pages_product_name(product_name, limit)
                self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
                case_list = GetCaseList_product_name(product_name, offset, limit)
                return render_template("interface_test/case/case_list.html", form=self.ins_CaseListForm,
                                       data_list=case_list, product_name=product_name,
                                       page_no=page_no, total_pages=total_pages, offset=offset, limit=limit,
                                       case_id=case_id)

Blue_case.add_url_rule("/interface_test/case/case_list/<product_name>/<page_no>/<offset>/<limit>/<case_id>",view_func=CaseList.as_view("case_list"))


class CaseNVEC(MethodView):
    def __init__(self):
        self.ins_CaseListForm = CaseListForm(request.form)
        self.ins_CaseNVEC_Form = CaseNVECForm(request.form)

    def get(self,product_name,case_group,interface_name,page_no,offset,limit,type,case_id):
        offset = int(offset)
        limit = int(limit)
        page_no = int(page_no)
        offset = int(offset)
        if product_name == '全部项目':
            flash('请选择项目；')
            total_pages = count_total_pages(limit)
            case_list = GetCaseList_product_name(product_name, offset, limit)
            self.ins_CaseListForm.product_name.choices = GetProductNameList_TestCaseList()
            return redirect(url_for("case.case_list", form=self.ins_CaseListForm,
                                   data_list=case_list,
                                   product_name=product_name, page_no=page_no, total_pages=total_pages, offset=offset,
                                   limit=limit, case_id=case_id))
        self.ins_CaseNVEC_Form.product_name.choices = GetProductNameList()
        self.ins_CaseNVEC_Form.case_group.choices = GetCaseGroupList(product_name)
        if case_id != "0":
            is_urlencode_pwd = GetIsUrlencodePwd(case_id)
            self.ins_CaseNVEC_Form.is_urlencode_pwd.data = is_urlencode_pwd
            encrypt_decrypt_file = GetEncryptDecryptFile(case_id)
            self.ins_CaseNVEC_Form.encrypt_decrypt_file.data = encrypt_decrypt_file
        if case_group != '0':
            self.ins_CaseNVEC_Form.case_group.data = case_group
        self.ins_CaseNVEC_Form.interface_name.choices = GetInterfaceList(product_name)
        if interface_name != "0":
            self.ins_CaseNVEC_Form.interface_name.data = interface_name
        self.ins_CaseNVEC_Form.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
        if type == "N":
            return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name,
                            page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id,case_group=0, interface_name=0, method=0, is_add_s1=0)
        elif type == "V":
            one_data_list = GetOneDataList(case_id)
            product_id = GetProductIdByCaseId(case_id)
            return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name,
                            page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id,case_group=0, interface_name=0,
                                   method=0, is_add_s1=0,data_list=one_data_list,case_name=one_data_list[5])
        elif type == "E" or type == "C":
            one_data_list = GetOneDataList(case_id)
            self.ins_CaseNVEC_Form.product_name.data = product_name
            self.ins_CaseNVEC_Form.case_group.data = one_data_list[1]
            method = one_data_list[3]
            self.ins_CaseNVEC_Form.interface_address.data = one_data_list[4]
            self.ins_CaseNVEC_Form.case_name.data = one_data_list[5]
            self.ins_CaseNVEC_Form.case_order.data = one_data_list[6]
            self.ins_CaseNVEC_Form.is_urlencode_pwd.data = one_data_list[7]
            self.ins_CaseNVEC_Form.encrypt_decrypt_file.data = one_data_list[8]
            self.ins_CaseNVEC_Form.case_explain.data = one_data_list[9]
            self.ins_CaseNVEC_Form.header.data = one_data_list[10]
            self.ins_CaseNVEC_Form.body.data = one_data_list[11]
            self.ins_CaseNVEC_Form.expect_response.data = one_data_list[12]
            return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name,
                    page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id,case_group=0, interface_name=0, method=method, is_add_s1=0,case_name=one_data_list[5])

    def post(self,product_name,case_group,interface_name,page_no,offset,limit,type,case_id):
        offset = int(offset)
        limit = int(limit)
        product_name0 = product_name
        if self.ins_CaseNVEC_Form.S1_sub.data == 1:
            product_name = self.ins_CaseNVEC_Form.product_name.data
            self.ins_CaseNVEC_Form.product_name.choices = GetProductNameList()
            self.ins_CaseNVEC_Form.case_group.choices = GetCaseGroupList(product_name)
            self.ins_CaseNVEC_Form.interface_name.choices = GetInterfaceList(product_name)
            self.ins_CaseNVEC_Form.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
            self.ins_CaseNVEC_Form.product_name.data = product_name
            return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name0,
                        page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id, case_group=1, interface_name=1, method=0,is_add_s1=1)

        if self.ins_CaseNVEC_Form.S2_sub.data == 1:
            product_name = self.ins_CaseNVEC_Form.product_name.data
            case_group = self.ins_CaseNVEC_Form.case_group.data
            interface_name = self.ins_CaseNVEC_Form.interface_name.data
            if interface_name == "None":
                product_name = self.ins_CaseNVEC_Form.product_name.data
                self.ins_CaseNVEC_Form.product_name.choices = GetProductNameList()
                self.ins_CaseNVEC_Form.case_group.choices = GetCaseGroupList(product_name)
                self.ins_CaseNVEC_Form.interface_name.choices = GetInterfaceList(product_name)
                self.ins_CaseNVEC_Form.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                self.ins_CaseNVEC_Form.product_name.data = product_name
                return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name,
                        page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id,case_group=1, interface_name=1, method=0, is_add_s1=1)

            method = GetMefhod(product_name,interface_name)
            self.ins_CaseNVEC_Form.method.data = method
            interface_address = GetInterfaceAddress(product_name,interface_name)
            self.ins_CaseNVEC_Form.product_name.choices = GetProductNameList()
            self.ins_CaseNVEC_Form.case_group.choices = GetCaseGroupList(product_name)
            self.ins_CaseNVEC_Form.interface_name.choices = GetInterfaceList(product_name)
            self.ins_CaseNVEC_Form.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
            self.ins_CaseNVEC_Form.product_name.data = product_name
            self.ins_CaseNVEC_Form.case_group.data = case_group
            self.ins_CaseNVEC_Form.interface_name.data = interface_name
            self.ins_CaseNVEC_Form.method = method
            self.ins_CaseNVEC_Form.interface_address.data = interface_address
            return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name,
                    page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id, case_group=1, interface_name=1, method=method, is_add_s1=1)

        if self.ins_CaseNVEC_Form.submit_sub.data == 1:
            product_name = self.ins_CaseNVEC_Form.product_name.data
            self.ins_CaseNVEC_Form.product_name.choices = GetProductNameList()
            self.ins_CaseNVEC_Form.product_name.data = product_name
            case_group = self.ins_CaseNVEC_Form.case_group.data
            if type == "E":
                case_order = int(self.ins_CaseNVEC_Form.case_order.data)
            self.ins_CaseNVEC_Form.case_group.choices = GetCaseGroupList(product_name)
            self.ins_CaseNVEC_Form.case_group.data = case_group
            # if case_group != '0':
            #     case_group = self.ins_CaseNVEC_Form.case_group.data
            #     self.ins_CaseNVEC_Form.case_group.choices = GetCaseGroupList(case_id)
            #     self.ins_CaseNVEC_Form.case_group.data = case_group
            interface_name = self.ins_CaseNVEC_Form.interface_name.data
            self.ins_CaseNVEC_Form.interface_name.choices = GetInterfaceList(product_name)
            self.ins_CaseNVEC_Form.interface_name.data = interface_name
            # elif case_group == "0":
            #     self.ins_CaseNVEC_Form.case_group.choices = GetCaseGroupList(case_id)
            # if interface_name != "0":
            #     interface_name = self.ins_CaseNVEC_Form.interface_name.data
            #     self.ins_CaseNVEC_Form.interface_name.choices = GetInterfaceList(product_name)
            #     self.ins_CaseNVEC_Form.interface_name.data = interface_name
            # elif interface_name == "0":
            #     self.ins_CaseNVEC_Form.interface_name.choices = GetInterfaceList(product_name)
            # method = self.ins_CaseNVEC_Form.method.data
            if interface_name != None:
                method = GetMefhod(product_name, interface_name)
            else:
                method = 0
            interface_address = self.ins_CaseNVEC_Form.interface_address.data
            case_name = self.ins_CaseNVEC_Form.case_name.data
            case_explain = self.ins_CaseNVEC_Form.case_explain.data
            is_urlencode_pwd = self.ins_CaseNVEC_Form.is_urlencode_pwd.data
            if is_urlencode_pwd == "2" or is_urlencode_pwd == "3":
                encrypt_decrypt_file = self.ins_CaseNVEC_Form.encrypt_decrypt_file.data
                self.ins_CaseNVEC_Form.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                self.ins_CaseNVEC_Form.encrypt_decrypt_file.data = encrypt_decrypt_file
            else:
                encrypt_decrypt_file = ""
                self.ins_CaseNVEC_Form.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
            header = self.ins_CaseNVEC_Form.header.data
            body = self.ins_CaseNVEC_Form.body.data
            expect_response = self.ins_CaseNVEC_Form.expect_response.data

            judge_r = judge_submit(case_id,product_name,case_group,interface_name,method,interface_address,case_name,case_explain,header,body,expect_response,type)
            if judge_r != 1:
                flash(judge_r)
                if type == "N":
                    return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name,
                                           page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id,
                                           case_group=0, interface_name=0, is_add_s1=0)
                if type == "C":
                    return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form, product_name=product_name,
                                           page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id,
                                           case_group=case_group, interface_name=interface_name, method=method, is_add_s1=0)
                if type == "E":
                    return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form, product_name=product_name,
                                           page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id,
                                           case_group=case_group, interface_name=interface_name, method=0, is_add_s1=0)
            if judge_r == 1:
                if type == "N" or type == "C":
                    InsertCaseSingle(product_name, case_group, interface_name, interface_address, case_name,
                                     is_urlencode_pwd, encrypt_decrypt_file, case_explain, header, body, expect_response)
                    # self.ins_CaseNVEC_Form.product_name.choices = GetProductNameList_TestCase()
                    # self.ins_CaseNVEC_Form.case_group.choices = GetCaseGroupList(product_name)
                    # self.ins_CaseNVEC_Form.interface_name.choices = GetInterfaceList(product_name)
                    # self.ins_CaseNVEC_Form.encrypt_decrypt_file.choices = get_encypt_decrypt_file()
                    flash("新增用例成功；")
                    if type == "N":
                        return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name,
                                               page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id, case_group=0, interface_name=0,
                                               method=0,is_add_s1=0)
                    if type == "C":
                        return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form,product_name=product_name,
                                               page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id, case_group=case_group,
                                               interface_name=interface_name, method=0, is_add_s1=0)
                if type == "E":
                    UpdataCaseSingle(product_name, case_group, interface_name, interface_address, case_name, case_order, is_urlencode_pwd,
                                     encrypt_decrypt_file, case_explain, header, body, expect_response, case_id)
                    flash("编辑用例成功；")
                    return render_template("interface_test/case/case_NVEC.html", form=self.ins_CaseNVEC_Form, product_name=product_name,
                                           page_no=page_no, offset=offset, limit=limit, type=type, case_id=case_id, case_group=case_group,
                                           interface_name=interface_name, method=0, is_add_s1=0)

Blue_case.add_url_rule("/interface_test/case/case_NEC/<product_name>/<case_group>/<interface_name>/<page_no>/<offset>/<limit>/<type>/<case_id>",view_func=CaseNVEC.as_view("case_NVEC"))