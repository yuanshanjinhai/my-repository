# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
import json
from admin.company.DB import *

Blue_company = Blueprint("company",__name__)

class Company(MethodView):
    def get(self):
        company_name = request.args.get('company_name')
        if company_name == None: # 获得所有公司信息
            company_list = GetCompanyList()
            data1 = {"code": 1, "info": "success", "data": company_list}
            data = json.dumps(data1, ensure_ascii=False)
            return data
        else: # 搜索功能，通过公司名称查询一个公司的信息（模糊查询）
            company_list = GetCompanyListByCompanyName(company_name)
            data1 = {"code": 1, "info": "success", "data": company_list}
            data = json.dumps(data1, ensure_ascii=False)
            return data

    def post(self): # 创建公司
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        company_name = data_dict['company_name']
        company_abbreviation = data_dict['company_abbreviation']
        company_explain = data_dict['company_explain']
        InsertCompany(company_name, company_abbreviation, company_explain)
        data0 = {"company_name": company_name, "company_abbreviation": company_abbreviation,"company_explain":company_explain}
        data1 = {"code": 1, "info": "success", "data": data0}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_company.add_url_rule("/company/",view_func=Company.as_view("company1"))
# http://127.0.0.1:5002/invoice/company/
# http://127.0.0.1:5002/invoice/company/?company_name=京
# {"company_name":"京东","company_abbreviation":"jd","company_explain":"京东集团"}

class CompanyEdit(MethodView):
    def get(self): # 通过公司d获得一个公司的数据
        company_id = int(request.args.get('company_id'))
        one_company_dict = GetOneCompanyDict(company_id)
        data1 = {"code": 1, "info": "success", "data": one_company_dict}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self): # 更新一个公司的数据
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        company_id = data_dict['company_id']
        company_name = data_dict['company_name']
        company_abbreviation = data_dict['company_abbreviation']
        company_explain = data_dict['company_explain']
        UpdateCompany(company_id, company_name, company_abbreviation, company_explain)
        data1 = {"code": 1, "info": "success",}
        data = json.dumps(data1, ensure_ascii=False)
        return data

Blue_company.add_url_rule("/company_edit/",view_func=CompanyEdit.as_view("company2"))
# http://127.0.0.1:5002/invoice/company_edit/?company_id=2
# {"company_id":2,"company_name":"阿里集团","company_abbreviation":"阿里","company_explain":"马老板的阿里帝国"}
