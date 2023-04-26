# coding=utf-8
from GeneralDB.InsertDB_System import *
from GeneralDB.OtherDB import GetCompanyIdByCompanytName,GetCompanyNameByCompanyId,GetDepartmentIdByCompanyIdDepartmentName

def InsertDepartment(department_name,department_explain,company_name):
    ins_insert = InsertDB_System()
    ins_insert.insert_system_department(department_name,department_explain)

    department_id_tuple = db.session.query(System_Department.id).first()
    department_id = department_id_tuple[0]
    company_id = GetCompanyIdByCompanytName(company_name)
    ins_insert.insert_system_company_department(company_id,department_id)

def GetDepartmentList():
    department_list0 = db.session.query(System_Department.id,System_Department.department_name,
                                        System_Company.company_name,
                                        System_Department.department_explain).all()
    department_list = []
    for i in department_list0:
        department_id = i[0]
        department_name = i[1]
        company_name = i[2]
        department_explain = i[3]
        tem_dict = {'department_id':department_id,'department_name':department_name,'department_explain':department_explain,'company_name':company_name}
        department_list.append(tem_dict)
    return department_list

def GetDepartmentListByCompanyNameDepartmentName(company_name,department_name):
    company_id = GetCompanyIdByCompanytName(company_name)
    department_id = GetDepartmentIdByCompanyIdDepartmentName(company_id,department_name)
    department_department_explain_tuple = db.session.query(System_Department.department_explain).filter(System_Department.id==department_id).first()
    department_explain = department_department_explain_tuple[0]
    department_one_dict = {'department_id':department_id,'company_name':company_name,'department_name':department_name,'department_explain':department_explain}
    return department_one_dict

def GetDepartmentListByCompanyName(company_name):
    company_id = GetCompanyIdByCompanytName(company_name)
    department_id_list = db.session.query(System_Company_Department.department_id).filter(System_Company_Department.company_id==company_id).all()
    department_list = []
    for i in department_id_list:
        department_list_tem = db.session.query(System_Department.department_name,System_Department.department_explain).filter(System_Department.id==i[0]).all()
        department_list.append({'department_id':i[0],'company_name':company_name,'department_name':department_list_tem[0][0],'department_explain':department_list_tem[0][1]})
    return department_list

def GetCompanyNameByDepartmentId(department_id):
    company_id_tuple= db.session.query(System_Company_Department.company_id).filter(System_Company_Department.department_id==department_id).first()
    company_id = company_id_tuple[0]
    company_name_tuple = db.session.query(System_Company.company_name).filter(System_Company.id==company_id).first()
    company_name = company_name_tuple[0]
    return company_name

def GetCompanyIdByCompanyName(company_name):
    company_id_tuple = db.session.query(System_Company.id).filter(System_Company.company_name==company_name).first()
    company_id = company_id_tuple[0]
    return company_id

def GetDepartmentOneByDepartmentId(department_id):
    department_one_tuple = db.session.query(System_Department.department_name,System_Department.department_explain).filter(System_Department.id==department_id).first()
    department_one_dict = {}
    for i in department_one_tuple:
        department_one_dict['department_id'] = department_id
        company_name = GetCompanyNameByDepartmentId(7)
        department_one_dict['company_name'] = company_name
        department_one_dict['department_name'] = i[0]
        department_one_dict['department_explain'] = i[1]
    return department_one_dict

def GetDepartmentIdByDepartmentName(department_name):
    department_id_tuple = db.session.query(System_Department.id).filter(System_Department.department_name==department_name).first()
    department_id = department_id_tuple[0]
    return department_id

def GetDepartmentNameByDepartmentId(department_id):
    department_name_q = db.session.query(System_Department.department_name).filter(System_Department.id==department_id).first()
    department_name = department_name_q[0]
    return department_name

def UpdateDepartment(department_id,company_name,department_name,department_explain):
    company_id = GetCompanyIdByCompanyName(company_name)
    department_queryset = db.session.query(System_Department).filter(System_Department.id==department_id).first()
    department_queryset.department_name = department_name
    department_queryset.department_explain = department_explain
    db.session.commit()
    company_department_id_list = db.session.query(System_Company_Department.id).filter(System_Company_Department.department_id==department_id).first()
    company_department_id = company_department_id_list[0]
    for i in company_department_id_list:
        company_department_queryset = db.session.query(System_Company_Department).filter(System_Company_Department.id==company_department_id).first()
        company_department_queryset.company_id = company_id
        db.session.commit()

if __name__ == '__main__':
    print( GetDepartmentNameByDepartmentId(1) )
