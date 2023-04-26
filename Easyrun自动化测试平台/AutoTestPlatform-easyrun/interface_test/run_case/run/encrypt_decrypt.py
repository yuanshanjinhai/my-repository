# coding=utf-8
from GeneralTools.OtherTools import get_encypt_decrypt_file,encrypt_decrypt

def encrypt(file_name,body):
    ins_ende = encrypt_decrypt(file_name, body)
    jr = hasattr(ins_ende, "encryp")
    if jr == 0:
        return "加密函数名称错误！0"
    elif jr == 1:
        body = ins_ende.encryp()
    return body

def decrypt(file_name,actual_respone):
    ins_ende = encrypt_decrypt(file_name, actual_respone)
    jr = hasattr(ins_ende, "decrypt")
    if jr == 0:
        return "解密函数名称错误！0"
    elif jr == 1:
        actual_respone = ins_ende.decrypt()
    return actual_respone

