# coding=utf-8
from flask_wtf import FlaskForm as Form
import wtforms

class BatchrunForm(Form):
    upload_sub = wtforms.SubmitField("用例上传")
    select_file = wtforms.FileField("选择附件")
    check_case_sub = wtforms.SubmitField('用例校验')
    is_urldecode = wtforms.SelectField("url解码", choices=[("n", "无解码"),("y", "url解码")], default="n")
    run_case_sub = wtforms.SubmitField("用例执行")
    download_execute_sub = wtforms.SubmitField("下载结果")
    download_template_sub = wtforms.SubmitField("下载模板")