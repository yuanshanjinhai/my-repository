# coding=utf-8
from GeneralDB.CreatDB_Test import *
from GeneralDB.OtherDB import *

def DeleteCaseSingle(case_id):
    db.session.query(Test_Case).filter(Test_Case.id==case_id).delete()
    db.session.commit()