# coding=utf-8
from urllib import parse

def password_encode(s):
    r = parse.quote(s)
    return r

if __name__ == '__main__':
    print( password_encode("abc123") )