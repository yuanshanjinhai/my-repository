# coding=utf-8
import re

def check_ShuangShuXian(ir,body_str,colum_title):
    error_str = ""
    shuangshuxian_list = re.findall("【.*】", body_str.encode('utf-8').decode("unicode_escape"))
    if shuangshuxian_list == []:
        return 1
    if shuangshuxian_list != []:
        for ish in shuangshuxian_list:
            if "|" in ish:
                r = re.findall(r"【\$\|\|\w+】|【\+\w+\|\|\w+】|【a\|\|\d+】|【d\|\|\d+】|【ad\|\|\d+】",ish)
                if r == []:
                    error_str += "第" + str(ir) + "行," + colum_title + "，" + str(ish) + "格式错误；"
        if error_str != 1:
            return error_str
        elif error_str == 1:
            return 1

if __name__ == '__main__':
    ir = 2
    body_str = '{"username":"【+guolint||G1】","password":"guolin123456","email":"guolin@126.com"}'
    colum_title = "请求体"
    print(check_ShuangShuXian(ir,body_str,colum_title))