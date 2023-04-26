# coding=utf-8
import os

def JugeCaseFileSuffix(file_name): # 判断文件后缀是否是py
    suffix_str = os.path.splitext(file_name)[1]
    if suffix_str == ".py":
        return 1
    else:
        return 0


if __name__ == '__main__':
    pass