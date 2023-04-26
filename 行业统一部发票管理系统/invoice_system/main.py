# coding=utf-8
from FlaskApp import *
app.secret_key="HFDJjfujdu2854397584tfoig"

from login.views import *
app.register_blueprint(Blue_login,url_prefix='/invoice')

from admin.user.views import *
app.register_blueprint(Blue_user,url_prefix='/invoice')

from admin.company.views import *
app.register_blueprint(Blue_company,url_prefix='/invoice')

from admin.department.views import *
app.register_blueprint(Blue_department,url_prefix='/invoice')

from admin.product.views import *
app.register_blueprint(Blue_product,url_prefix='/invoice')

from admin.invoicetype.views import *
app.register_blueprint(Blue_invoicetype,url_prefix='/invoice')

from invoice.invoice.views import *
app.register_blueprint(Blue_invoice,url_prefix='/invoice')

from invoice.statisticalanalysis.views import *
app.register_blueprint(Blue_statisticalanalysis,url_prefix='/invoice')

from all_list.views import *
app.register_blueprint(Blue_alllist,url_prefix='/invoice')

if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)