# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class InterfaceListForm(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    search_sub = wtforms.SubmitField("搜索")
    get_id = wtforms.StringField('获取id')
    # creat_sub = wtforms.SubmitField("新增")
    delete_sub = wtforms.SubmitField('删除')

class InterfaceNEC_Form(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    interface_name = wtforms.StringField("接口名称")
    interface_order = wtforms.StringField("接口顺序")
    interface_address = wtforms.StringField("接口地址")
    interface_method = wtforms.SelectField("接口方法", choices=[("POST", "POST"), ("GET", "GET")])
    interface_explain = wtforms.StringField("接口说明")
    submit_sub = wtforms.SubmitField("提交")