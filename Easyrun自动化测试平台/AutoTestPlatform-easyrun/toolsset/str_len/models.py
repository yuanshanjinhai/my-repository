# coding=utf-8
from flask import request,render_template,redirect,url_for
from flask_wtf import FlaskForm
import wtforms

class CreatStrlenForm(FlaskForm):
    str_ = wtforms.StringField('字符串')
    submit_sub = wtforms.SubmitField('提交')
    reset_sub = wtforms.SubmitField('重置')