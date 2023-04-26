# coding=utf-8
from GeneralDB.OtherDB import *
from sqlalchemy import and_,desc
from GeneralDB.CreatDB_Test import *
from GeneralDB.InserDB import *

def IntoRunResult(case_id,actual_response, run_time,is_pass):
    ins_insert = Insert_db()
    ins_insert.insert_test_run_result(case_id,actual_response, run_time, is_pass)