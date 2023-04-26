# coding=utf-8
from admin.user.DB.OtherDB import *

def count_total_pages(limit):
    user_data_count = CountUserData()
    if user_data_count % limit == 0:
        total_pages = user_data_count // limit
    elif user_data_count % limit > 0:
        total_pages = user_data_count // limit + 1
    if total_pages == 0:
        total_pages = 1
    return total_pages

def GetPassword(user_login_name):
    password = db.session.query(System_User.password).filter(System_User.user_login_name==user_login_name).first()[0]
    return password

if __name__ == '__main__':
    print(GetPassword("zhaoliu"))
