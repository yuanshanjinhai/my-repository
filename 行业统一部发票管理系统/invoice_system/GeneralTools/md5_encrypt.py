# coding=utf-8
import hashlib

def md5_encrypt(password_str):
    m = hashlib.md5()
    m.update(password_str.encode(encoding='utf-8'))
    r = m.hexdigest()
    return r