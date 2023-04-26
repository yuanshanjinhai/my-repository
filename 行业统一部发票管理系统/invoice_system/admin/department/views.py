# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
import json
from admin.department.DB import *

Blue_department = Blueprint("department",__name__)

class Department(MethodView):
    def get(self):
        company_name = request.args.get('company_name')
        department_name = request.args.get('department_name')
        if company_name == None and department_name == None:
            department_list = GetDepartmentList()
        elif company_name != None and department_name != None:
            department_list = GetDepartmentListByCompanyNameDepartmentName(company_name, department_name)
        elif company_name != None and department_name == None:
            department_list = GetDepartmentListByCompanyName(company_name)
        elif company_name == None and department_name != None:
            data1 = {"code": 0, "info": "请先选择公司"}
            data = json.dumps(data1, ensure_ascii=False)
            return data
        data1 = {"code": 1, "info": "success", "data": department_list}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        department_name = data_dict['department_name']
        department_explain = data_dict['department_explain']
        company_name = data_dict['company_name']
        InsertDepartment(department_name, department_explain, company_name)
        data1 = {"code": 1, "info": "success"}
        data = json.dumps(data1, ensure_ascii=False)
        return data

Blue_department.add_url_rule("/department/",view_func=Department.as_view("department1"))
# http://127.0.0.1:5002/invoice/department/?company_name=京东&department_name=开发部
# {"department_name":"人事部","department_explain":"京东的人事部","company_name":"京东"}

class Department_edit(MethodView):
    def get(self):
        department_id = int(request.args.get('department_id'))
        if department_id != None:
            department_one_dict = GetDepartmentOneByDepartmentId(department_id)
            data1 = {"code": 1, "info": "success", "data": department_one_dict}
            data = json.dumps(data1, ensure_ascii=False)
            return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        department_id = int(data_dict['department_id'])
        company_name = data_dict['company_name']
        department_name = data_dict['department_name']
        department_explain = data_dict['department_explain']
        UpdateDepartment(department_id,company_name, department_name, department_explain)
        data1 = {"code": 1, "info": "success"}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_department.add_url_rule("/department_edit/",view_func=Department_edit.as_view("department2"))