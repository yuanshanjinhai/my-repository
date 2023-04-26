# coding = utf-8
from flask import Blueprint,request, render_template, flash,session,redirect,url_for
from flask.views import MethodView

Blue_home = Blueprint("home", __name__)

class Home(MethodView):
    def get(self):
        if "user_resource_list" not in session or "user_login_name" not in session or "user_name" not in session:
            return redirect(url_for("login.login"))
        return render_template("home/home.html")

Blue_home.add_url_rule("/home/home/",view_func=Home.as_view("home"))