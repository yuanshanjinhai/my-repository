# coding=utf-8
from urllib import parse

def url_encode(s):
    r = parse.quote(s)
    return r

def url_decode(s):
    r = parse.unquote(s)
    return r

if __name__ == '__main__':
    print( url_encode( '{"a":1}' ))
