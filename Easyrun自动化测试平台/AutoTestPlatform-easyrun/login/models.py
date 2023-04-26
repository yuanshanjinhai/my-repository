# coding=utf-8
from flask import request,render_template,redirect,url_for
from flask_wtf import FlaskForm
import wtforms
from wtforms import validators

class loginform(FlaskForm): # 创建一个用于获取html页面数据的类，它必须继承自wtforms类的Form子类
    username=wtforms.StringField('用户名：',[validators.DataRequired("用户名不能为空"),validators.Length(min=4,max=16,message="用户名长度应在4到16个字符之间")]) # 设置username，html页面将从这里取数据
    password=wtforms.PasswordField('密码：',[validators.DataRequired("密码不能为空")],default="请输入你的密码")

class UpdatePasswordForm(FlaskForm):
    login_name = wtforms.StringField("登录名")
    old_password = wtforms.PasswordField("原密码")
    new_password = wtforms.PasswordField("新密码")
    new_password_again = wtforms.PasswordField("确认新密码")
    submit_sub = wtforms.SubmitField("提交")


if __name__ == '__main__':
    ins=loginform()