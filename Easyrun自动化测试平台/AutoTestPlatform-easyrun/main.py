# coding=utf-8
from FlaskApp import *
app.secret_key="HJAHFJKdsjfkajkh8968780"

from login.views import *
app.register_blueprint(Blue_login,url_prefix="/easyrun")

from home.views import *
app.register_blueprint(Blue_home,url_prefix="/easyrun")

# from interface_test.batchrun.views import *
# app.register_blueprint(Blue_easyrun,url_prefix="/easyrun")

from interface_test.case_group.views import *
app.register_blueprint(Blue_case_group,url_prefix="/easyrun")

from interface_test.interface.views import *
app.register_blueprint(Blue_interface,url_prefix="/easyrun")

from interface_test.global_var.views import *
app.register_blueprint(Blue_global_var,urlprefix="/easyrun")

from interface_test.singlerun.views import *
app.register_blueprint(Blue_singlerun,url_prefix="/easyrun")

from interface_test.encrypt_decrypt.views import *
app.register_blueprint(Blue_encrypt_decrypt,urlprefix="/easyrun")

from interface_test.case.views import *
app.register_blueprint(Blue_case,urlprefix="/easyrun")

from interface_test.run_case.views import *
app.register_blueprint(Blue_run_case,urlprefix="/easyrun")

from toolsset.creat_boundary.views import *
app.register_blueprint(Blue_tools_boundary,url_prefix="/toolsset")

from toolsset.str_len.views import *
app.register_blueprint(Blue_tools_strlen,url_prefix="/toolsset")

from helps.case_rule.views import *
app.register_blueprint(Blue_case_rule,url_prefix='/easyrun')

from admin.user.views import *
app.register_blueprint(Blue_user,url_prefix='/easyrun')

from admin.role.views import *
app.register_blueprint(Blue_role,url_prefix='/easyrun')

from admin.product.views import *
app.register_blueprint(Blue_product,url_prefix='/easyrun')

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)