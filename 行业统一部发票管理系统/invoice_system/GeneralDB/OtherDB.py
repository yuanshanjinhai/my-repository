# coding=utf-8
from GeneralDB.CreatDB import *
from GeneralDB.CreatDB_System import *

def GetCompanyIdByCompanytName(company_name):
    obj = db.session.query(System_Company.id).filter(System_Company.company_name==company_name).first()
    company_id = obj[0]
    return company_id

def GetCompanyNameByCompanyId(company_id):
    obj = db.session.query(System_Company.company_name).filter(System_Company.id==company_id).first()
    company_name = obj[0]
    return company_name

def GetDepartmentIdByCompanyIdDepartmentName(company_id,department_name):
    obj = db.session.query(System_Company_Department.id).filter(System_Company_Department.company_id==company_id,System_Department.department_name==department_name).first()
    department_id = obj[0]
    return department_id

if __name__ == '__main__':
    print( GetDepartmentIdByCompanyIdDepartmentName(3,'开发部') )
    # print( GetDepartmentIdByCompanyNameDepartmentName('腾讯','开发部') )