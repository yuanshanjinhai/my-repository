# coding=utf-8
from GeneralDB.OtherDB import *
from GeneralDB.CreatDB_Test import *
# from interface_test.run_case.DB.OtherDB import GetRalationNameCaseGroup0
import copy

def GetRunCaseList(product_name):
    product_id = GetProduct_id_by_product_name(product_name)
    case_list0 = db.session.query(Test_Case, Test_Case_Group).join(Test_Case,
                                  Test_Case_Group.id == Test_Case.case_group_id).filter(
        Test_Case.product_id == product_id).order_by(Test_Case_Group.case_group_order).order_by(Test_Case.case_order).all()
    groupstart_dict = {}
    groupstart_list = []

    groupbatch_dict = {}
    groupbatch_list0 = []
    groupbatch_list = []

    groupend_dict = {}
    groupend_list = []
    for ic in range(0,len(case_list0)):
        case_id = case_list0[ic][0].id
        product_id = case_list0[ic][0].product_id
        case_group_id = case_list0[ic][0].case_group_id
        case_group_order = case_list0[ic][1].case_group_order
        interface_id = case_list0[ic][0].interface_id
        if interface_id != None:
            method = db.session.query(Test_Interface.method).filter(Test_Interface.id==interface_id).first()[0]
        else:
            method = None
        case_name = case_list0[ic][0].case_name
        interface_address = case_list0[ic][0].interface_address
        case_order = case_list0[ic][0].case_order
        is_relationed = case_list0[ic][0].is_relationed
        is_urlencode_pwd = case_list0[ic][0].is_urlencode_pwd
        encrypt_decrypt_file = case_list0[ic][0].encrypt_decrypt_file
        header = case_list0[ic][0].header
        body = case_list0[ic][0].body
        expect_response = case_list0[ic][0].expect_response

        if case_group_order == 0:
            groupstart_dict['case_id'] = case_id
            groupstart_dict['product_id'] = product_id
            groupstart_dict['case_group_id'] = case_group_id
            groupstart_dict['case_group_order'] = case_group_order
            groupstart_dict['interface_id'] = interface_id
            groupstart_dict['case_name'] = case_name
            groupstart_dict['method'] = method
            groupstart_dict['interface_address'] = interface_address
            groupstart_dict['case_order'] = case_order
            groupstart_dict['is_relationed'] = is_relationed
            groupstart_dict['is_urlencode_pwd'] = is_urlencode_pwd
            groupstart_dict['encrypt_decrypt_file'] = encrypt_decrypt_file
            groupstart_dict['header'] = header
            groupstart_dict['body'] = body
            groupstart_dict['expect_response'] = expect_response
            tem_groupstart_dict = copy.deepcopy(groupstart_dict)
            groupstart_list.append(tem_groupstart_dict)

        if case_group_order > 0 and case_group_order < 999:
            groupbatch_dict['case_id'] = case_id
            groupbatch_dict['product_id'] = product_id
            groupbatch_dict['case_group_id'] = case_group_id
            groupbatch_dict['case_group_order'] = case_group_order
            groupbatch_dict['interface_id'] = interface_id
            groupbatch_dict['case_name'] = case_name
            groupbatch_dict['method'] = method
            groupbatch_dict['interface_address'] = interface_address
            groupbatch_dict['case_order'] = case_order
            groupbatch_dict['is_relationed'] = is_relationed
            groupbatch_dict['is_urlencode_pwd'] = is_urlencode_pwd
            groupbatch_dict['encrypt_decrypt_file'] = encrypt_decrypt_file
            groupbatch_dict['header'] = header
            groupbatch_dict['body'] = body
            groupbatch_dict['expect_response'] = expect_response

            if case_order == 1 or case_order == case_list0[ic-1][0].case_order + 1:
                tem_groupbatch_dict = copy.deepcopy(groupbatch_dict)
                groupbatch_list0.append(tem_groupbatch_dict)
                if ic != len(case_list0)-1:
                    if case_list0[ic+1][0].case_order == 1:
                        groupbatch_list.append(groupbatch_list0)
                        groupbatch_list0 = []
                elif ic == len(case_list0)-1:
                    groupbatch_list.append(groupbatch_list0)
                    groupbatch_list0 = []

        if case_group_order == 999:
            groupend_dict['case_id'] = case_id
            groupend_dict['product_id'] = product_id
            groupend_dict['case_group_id'] = case_group_id
            groupend_dict['case_group_order'] = case_group_order
            groupend_dict['interface_id'] = interface_id
            groupend_dict['case_name'] = case_name
            groupend_dict['method'] = method
            groupend_dict['interface_address'] = interface_address
            groupend_dict['case_order'] = case_order
            groupend_dict['is_relationed'] = is_relationed
            groupend_dict['is_urlencode_pwd'] = is_urlencode_pwd
            groupend_dict['encrypt_decrypt_file'] = encrypt_decrypt_file
            groupend_dict['header'] = header
            groupend_dict['body'] = body
            groupend_dict['expect_response'] = expect_response
            tem_groupend_dict = copy.deepcopy(groupend_dict)
            groupend_list.append(tem_groupend_dict)

    return (groupstart_list,groupbatch_list,groupend_list)

if __name__ == '__main__':
    r = GetRunCaseList('测试系统1')
    print(r)