# coding=utf-8
from GeneralDB.CreatDB import *
from GeneralDB.CreatDB_System import *
from GeneralDB.CreatDB_Test import *

class Insert_db():
    def __init__(self):
        self.db=db

    def insert_system_product(self,product_name,product_abbreviation,product_explain):
        this_data = System_Product(product_name,product_abbreviation,product_explain)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_user(self,user_login_name,user_name,passwod):
        this_data = System_User(user_login_name,user_name,passwod)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_user_role(self,user_id,role_id):
        this_data = System_User_Role(user_id,role_id)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_role(self,role_name):
        this_data = System_Role(role_name)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_resource(self,resource_name):
        this_data = System_Resource(resource_name)
        db.session.add(this_data)
        db.session.commit()

    def insert_system_role_resource(self,role_id,resource_id):
        this_data_role = System_Role_Resource(role_id,resource_id)
        db.session.add(this_data_role)
        db.session.commit()

    def insert_test_case_group(self,product_id,is_run,case_group_name,case_group_order,case_group_type,case_group_explain):
        this_data = Test_Case_Group(product_id,is_run,case_group_name,case_group_order,case_group_type,case_group_explain)
        db.session.add(this_data)
        db.session.commit()

    def insert_test_global_var(self,product_id,global_var_name,global_var_value,is_auto_add,global_var_explain):
        this_data = Test_Global_Var(product_id,global_var_name,global_var_value,is_auto_add,global_var_explain)
        db.session.add(this_data)
        db.session.commit()

    def insert_test_encrypt_decrypt(self,file_name):
        this_data = Test_Encrypt_Decrypt(file_name,"")
        db.session.add(this_data)
        db.session.commit()

    def insert_test_interface(self,product_id,interface_name,interface_order,interface_address,interface_method,interface_explain):
        method = interface_method
        this_data = Test_Interface(product_id,interface_name,interface_order,interface_address,method,interface_explain)
        db.session.add(this_data)
        db.session.commit()

    def insert_test_case(self,product_id,case_group_id,interface_id,interface_address,is_relationed,case_name,case_order,is_urlencode_pwd,encrypt_decrypt_file,case_explain,header,body,expect_response,creat_time,update_time):
        this_data = Test_Case(product_id,case_group_id,interface_id,interface_address,is_relationed,case_name,case_order,is_urlencode_pwd,encrypt_decrypt_file,case_explain,header,body,expect_response,creat_time,update_time)
        db.session.add(this_data)
        db.session.commit()

    def insert_test_relation(self,product_id,case_group_id,case_id,relation_name,relation_field,json_path):
        this_data = Test_relation(product_id,case_group_id,case_id,relation_name,relation_field,json_path)
        db.session.add(this_data)
        db.session.commit()

    def insert_test_run_result(self,case_id,actual_response,run_time,is_pass):
        this_data = Test_run_result(case_id,actual_response,run_time,is_pass)
        db.session.add(this_data)
        db.session.commit()

if __name__ == '__main__':
    # ins_insert = Insert_db()
    # ins_insert.insert_system_resource("home")
    # ins_insert.insert_system_resource("interface-singlerun")
    # ins_insert.insert_system_resource("interface-interface")
    # ins_insert.insert_system_resource("interface-case_group")
    # ins_insert.insert_system_resource("interface-global")
    # ins_insert.insert_system_resource("interface-encypt_decypt")
    # ins_insert.insert_system_resource("interface-case")
    # ins_insert.insert_system_resource("interface-run")
    # ins_insert.insert_system_resource("interface-result")
    # ins_insert.insert_system_resource("interface-singlerun")
    # ins_insert.insert_system_resource("tools-creat_boundart")
    # ins_insert.insert_system_resource("tools-str_len")
    # ins_insert.insert_system_resource("help-case_rule")
    # ins_insert.insert_system_resource("admin-product")
    # ins_insert.insert_system_resource("admin-user")
    # ins_insert.insert_system_resource("admin-role")
    pass
