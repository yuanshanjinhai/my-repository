# coding=utf-8
from GeneralDB.InsertDB_System import *

def InsertCompany(company_name,company_abbreviation,company_explain):
    ins_insert = InsertDB_System()
    ins_insert.insert_system_company(company_name,company_abbreviation,company_explain)

def GetCompanyList():
    company_list0 = db.session.query(System_Company.id,System_Company.company_name,System_Company.company_abbreviation,System_Company.company_explain).all()
    company_list = []
    for i in company_list0:
        tem_dict = {'company_name':i[0],'company_abbreviation':i[1],'company_explain':i[2]}
        company_list.append(tem_dict)
    return company_list

def GetCompanyListByCompanyName(company_name):
    this_like = "%"+company_name+"%"
    company_list0 = db.session.query(System_Company.id,System_Company.company_name, System_Company.company_abbreviation,
                                     System_Company.company_explain).\
        filter(System_Company.company_name.like(this_like)).all()
    company_list = []
    for i in company_list0:
        tem_dict = {'company_name': i[0], 'company_abbreviation': i[1], 'company_explain': i[2]}
        company_list.append(tem_dict)
    return company_list

def GetOneCompanyDict(company_id):
    company_obj = db.session.query(System_Company.company_name,System_Company.company_abbreviation,
                                   System_Company.company_explain).filter(System_Company.id==company_id).first()
    company_one_dict = {}
    company_one_dict['company_id'] = company_id
    company_one_dict['公司名称'] = company_obj[0]
    company_one_dict['公司简称'] = company_obj[1]
    company_one_dict['说明'] = company_obj[2]
    return company_one_dict

def UpdateCompany(company_id,company_name,company_abbreviation,company_explain):
    one_obj = db.session.query(System_Company).filter(System_Company.id==company_id).first()
    one_obj.company_name = company_name
    one_obj.company_abbreviation = company_abbreviation
    one_obj.company_explain = company_explain
    db.session.commit()

def GetCompanyNameByCompanyId(company_id):
    company_name_q = db.session.query(System_Company.company_name).filter(System_Company.id==company_id).first()
    company_name = company_name_q[0]
    return company_name

if __name__ == '__main__':
    print( GetCompanyNameByCompanyId(1) )