# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class GloblaVarListForm(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    search_sub = wtforms.SubmitField("搜索")
    get_id = wtforms.StringField('获取id')
    delete_sub = wtforms.SubmitField('删除')

class GloblaVarNEC_Form(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    global_var_name = wtforms.StringField("全局变量名")
    global_var_value = wtforms.StringField("全局变量值")
    is_auto_add = wtforms.SelectField("是否自增", choices=[("是", "是"), ("否", "否")], default="否")
    global_var_explain = wtforms.StringField("说明")
    submit_sub = wtforms.SubmitField("提交")