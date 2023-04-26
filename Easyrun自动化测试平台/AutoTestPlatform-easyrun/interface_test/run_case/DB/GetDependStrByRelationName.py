# coding=utf-8
from GeneralDB.OtherDB import *
from sqlalchemy import and_
from GeneralDB.CreatDB_Test import *

def GetDependStrByRelationName(product_id,relation_name):
    print('product_id=',product_id,type(product_id))
    print('relation_name=',relation_name)
    depend_case_id_objct = db.session.query(Test_relation.case_id).filter(and_(Test_relation.product_id==product_id,Test_relation.relation_name==relation_name)).first()
    depend_case_id = depend_case_id_objct[0]
    print('depend_case_id=',depend_case_id)
    json_path = db.session.query(Test_relation.json_path).filter(and_(Test_relation.product_id==product_id,Test_relation.relation_name==relation_name)).first()[0]
    relation_field = db.session.query(Test_relation.relation_field).filter(Test_relation.case_id==depend_case_id).first()[0]
    print('relation_field=',relation_field)
    print('relation_field=',relation_field)
    if relation_field == "header":
        depanded_str = db.session.query(Test_Case.header).filter(Test_Case.id==depend_case_id).first()[0]
    if relation_field == "body":
        depanded_str = db.session.query(Test_Case.body).filter(Test_Case.id==depend_case_id).first()[0]
    if relation_field == "expect_response":
        depanded_str = db.session.query(Test_run_result.actual_response).filter(Test_run_result.case_id==depend_case_id).first()[0]
    try:
        depand_str = eval(str(depanded_str) + "[" + json_path + "]")
    except:
        depanded_str = "实际返回json中无此键！"
    print('depanded_str=',depanded_str)
    return depanded_str
