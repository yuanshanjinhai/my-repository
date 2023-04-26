# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class RoleListForm(FlaskForm):
    role_name = wtforms.StringField("角色名")
    search_sub = wtforms.SubmitField("搜索")
    get_id = wtforms.StringField('获取id')
    delete_sub = wtforms.SubmitField('删除')

class RoleNEForm(FlaskForm):
    role_name = wtforms.StringField("角色名称")
    resource_str = wtforms.TextAreaField("资源列表")
    submit_sub = wtforms.SubmitField("提交")