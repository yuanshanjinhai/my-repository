# coding=utf-8
from flask import request,render_template,redirect,url_for
from flask_wtf import FlaskForm
import wtforms

class CreatBoundaryForm(FlaskForm):
    word_lenth = wtforms.StringField('生成长度')
    word_type = wtforms.SelectField('选择',choices=[("中文","中文"),("英文","英文"),("数字","数字"),("符号","符号"),("综合","综合")])
    submit_sub = wtforms.SubmitField('提交')
    punctuation_sub = wtforms.SubmitField('生成所有符号')
    reset_sub = wtforms.SubmitField('重置')