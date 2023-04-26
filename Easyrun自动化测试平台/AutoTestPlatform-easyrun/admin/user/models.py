# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class UserListForm(FlaskForm):
    user_name_inputbox = wtforms.StringField("用户名输入框")
    search_sub = wtforms.SubmitField("搜索")
    get_id = wtforms.StringField('获取id')
    delete_sub = wtforms.SubmitField('删除')

class UserNEForm(FlaskForm):
    user_login_name = wtforms.StringField("用户id")
    user_name = wtforms.StringField("用户名")
    is_update_password = wtforms.SelectField("是否修改密码",choices=[("否", "否"), ("是", "是")])
    new_password = wtforms.StringField("新密码")
    role = wtforms.SelectField("对应角色")
    submit_sub = wtforms.SubmitField("提交")
