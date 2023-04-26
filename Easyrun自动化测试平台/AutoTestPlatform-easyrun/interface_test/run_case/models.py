# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class CaseRunListForm(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    search_sub = wtforms.SubmitField("搜索")
    run_case_sub = wtforms.SubmitField('执行')
    get_id = wtforms.StringField('获取用例id')