# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class ProductListForm(FlaskForm):
    product_name_inputbox = wtforms.StringField("项目名称输入框")
    search_sub = wtforms.SubmitField("搜索")
    get_id = wtforms.StringField('获取id')
    delete_sub = wtforms.SubmitField('删除')

class ProductNEForm(FlaskForm):
    product_name = wtforms.StringField("项目名称")
    product_abbreviation = wtforms.StringField("项目简称")
    product_explain = wtforms.TextAreaField("项目说明")
    submit_sub = wtforms.SubmitField("提交")

