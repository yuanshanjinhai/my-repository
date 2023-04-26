# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class CaseGroupListForm(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    search_sub = wtforms.SubmitField("搜索")
    get_id = wtforms.StringField('获取id')
    delete_sub = wtforms.SubmitField('删除')

class CaseGroupCreatEditCopyForm(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    is_run = wtforms.SelectField("是否执行",choices=[("Y","Y"),("N","N")])
    case_group_name = wtforms.StringField("用例组名称")
    case_group_order = wtforms.StringField("用例组顺序")
    case_group_type = wtforms.SelectField("用例组类型", choices=[("起始组", "起始组"), ("并发组", "并发组"), ("结束组", "结束组")], default="并发组")
    case_group_explain = wtforms.StringField("用例组说明")
    submit_sub = wtforms.SubmitField("提交")