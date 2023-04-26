# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from FlaskApp import app

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://easyruner:123456@127.0.0.1:3306/easyrun_db?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SQLALCHEMY_ECHO"]=True

db = SQLAlchemy(app)