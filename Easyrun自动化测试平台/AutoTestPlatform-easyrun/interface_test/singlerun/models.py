# coding=utf-8
from flask_wtf import FlaskForm as Form
import wtforms

class SinglerunForm(Form):
    method = wtforms.SelectField('方法：',choices=[("POST","POST"),("GET","GET")])
    is_urlencode_pwd = wtforms.SelectField("编码与加密", choices=[("0", "无"), ("1", "url编码-url解码"), ("2", "加密-解密"),
                                                             ("3", "url编码-加密-解密-url解码"), ("4", "仅url编码"),
                                                             ("5", "仅url解码")])
    encrypt_decrypt_file = wtforms.SelectField('加解密文件')
    run_sub = wtforms.SubmitField("执行")
    update_sub = wtforms.SubmitField("刷新")
    address = wtforms.StringField("地址")
    heaer = wtforms.StringField("请求头")
    body = wtforms.TextAreaField("请求体")
    response = wtforms.TextAreaField("返回值")