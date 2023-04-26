# coding=utf-8
from flask import request,render_template,redirect,url_for
from flask_wtf import FlaskForm
import wtforms

class LogoutForm(FlaskForm):
    logout_sub = wtforms.SubmitField("确定退出")