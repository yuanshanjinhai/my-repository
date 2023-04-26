# coding=utf-8
import os

path1 = os.getcwd()
path2 = os.path.dirname(os.path.dirname(__file__))
if __name__ == '__main__':
    print(path1)
    print(path2)