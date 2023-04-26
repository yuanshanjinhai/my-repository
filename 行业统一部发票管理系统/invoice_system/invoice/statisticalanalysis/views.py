# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
import json
from invoice.statisticalanalysis.DB import GetQueryRuslt

Blue_statisticalanalysis = Blueprint("statisticalanalysis",__name__)

class statisticalanalysis(MethodView):
    def get(self):
        user_id = request.args.get('user_id')
        invoicetype_id = request.args.get('invoicetype_id')
        time_start = request.args.get('time_start')
        time_end = request.args.get('time_end')
        rdict = GetQueryRuslt(user_id, invoicetype_id, time_start, time_end)
        data1 = {"code": 1, "info": "success", "data": rdict}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_statisticalanalysis.add_url_rule("/statisticalanalysis/",view_func=statisticalanalysis.as_view("statisticalanalysis1"))
# http://127.0.0.1:5002/invoice/statisticalanalysis?user_id=2
#  http://127.0.0.1:5002/invoice/statisticalanalysis?time_start=2023-01-16&time_end=2023-01-19