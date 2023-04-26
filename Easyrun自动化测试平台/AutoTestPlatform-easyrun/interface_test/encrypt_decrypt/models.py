# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class EncryptDecryptListForm(FlaskForm):
    search_sub = wtforms.SubmitField("搜索")
    select_file = wtforms.FileField("选择附件")
    upload_sub = wtforms.SubmitField("上传")
    download_template_sub = wtforms.SubmitField("模板下载")
    get_id = wtforms.StringField('获取id')
    delete_sub = wtforms.SubmitField('删除')