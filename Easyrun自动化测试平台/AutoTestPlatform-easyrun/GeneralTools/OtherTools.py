# coding=utf-8
import json
import os
import hashlib
from GeneralTools.AllPath import encrypt_decrypt_load_path0

def RemoveSpacesAndEnter(json_str): # 去掉json里的空格，同时，时间字符串里的空格不能去掉，如：2021-01-12 17:53:39
    print('json_str=',json_str,type(json_str))
    r_json_str = ""
    for ij in range(0,len(json_str)):
        if json_str[ij] == " " and json_str[ij-1].isdigit() !=1:
            continue
        r_json_str += json_str[ij]
    return "".join(r_json_str.split("\n"))

def HeaderValueIsUnStr(ir,header_dict):
    error_str = ""
    for j,k in header_dict.items():
        if isinstance(k,str) != 1:
            if ir != "":
                error_str += "第"+str(ir)+"行,请求头的" + str(j) +"键对应的值必须是字符串类型；"
            elif ir == "":
                error_str += "请求头的" + str(j) + "键对应的值必须是字符串类型；"
    return error_str

def check_case(header,body):
    error_str = ""
    if header != "":
        try:
            header = eval(header)
            get_r = HeaderValueIsUnStr("", header)
            if get_r != "":
                error_str += get_r
        except:
            error_str += "请求头不是键值对形式；"

    if body != "":
        try:
            body = json.loads(body)
        except:
            error_str += "请求体不是json；"

    # if expect_response != "":
    #     try:
    #         expect_response = json.loads(expect_response)
    #     except:
    #         error_str += "预期返回值不是json；"

    if error_str == "":
        return 1
    elif error_str != "":
        return error_str

def get_encypt_decrypt_file():
    for root, dirs_list, files_list in os.walk(encrypt_decrypt_load_path0, topdown=False):
        pass
    file_list = []
    for ifl in files_list:
        if ifl == "__init__.py":
            continue
        file_list.append((ifl,ifl))
    return file_list

def md5_encrypt(password_str):
    m = hashlib.md5()
    m.update(password_str.encode(encoding='utf-8'))
    r = m.hexdigest()
    return r

def encrypt_decrypt(file_name,body_str):
    dir_file_func = __import__("interface_test.encrypt_decrypt.encrypt_decrypt_load." + file_name, fromlist=1)
    jr = hasattr(dir_file_func,"EncryptAndDecrypt")
    if jr == 1:
        ins_func = getattr(dir_file_func, "EncryptAndDecrypt")
        return eval("ins_func(" + body_str + ")")
    else:
        return 0

if __name__ == '__main__':
    password_str = '{"username":"10098567","mobile":"138****0830"}'
    print( md5_encrypt(password_str) )