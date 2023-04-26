

def JudgeInterfaceNameIsRepeat_NC(product_name, interface_name): # 判断接口名称是否重复(新增和复制新增时使用）
    product_id = GetProduct_name_by_product_id(product_name)
    case_interface_list0 = db.session.query(Test_Interface.interface_name).filter(Test_Interface.product_id == product_id).all()
    case_interface_list = list(map(lambda x: x[0], case_interface_list0))
    if interface_name in case_interface_list:
        return 0
    else:
        return 1

def JudgeInterfaceNameIsRepeat_E(product_name, interface_name): # 判断接口名称是否重复（编辑时使用）
    product_id = GetProduct_name_by_product_id(product_name)
    case_interface_list0 = db.session.query(Test_Interface.interface_name).filter(
        and_(Test_Interface.product_id == product_id, Test_Interface.interface_name != interface_name)).all()
    case_interface_list = list(map(lambda x: x[0], case_interface_list0))
    if interface_name in case_interface_list:
        return 0
    else:
        return 1