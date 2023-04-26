# coding=utf-8
from flask import request
from flask.views import MethodView
from flask import Blueprint
import json
from admin.product.DB import InsertProduc,GetProductList,GetProductListByProductName,GetProductOneByProductId,\
    UpdateProduct

Blue_product = Blueprint("product",__name__)

class Product(MethodView):
    def get(self):
        product_name = request.args.get('product_name')
        if product_name == None:
            product_r= GetProductList()
        else:
            product_r= GetProductListByProductName(product_name)
        data1 = {"code": 1, "info": "success", "data": product_r}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        product_name = data_dict['product_name']
        product_abbreviation = data_dict['product_abbreviation']
        product_explain = data_dict['product_explain']
        if product_name != None:
            InsertProduc(product_name, product_abbreviation, product_explain)
            data1 = {"code": 1, "info": "success"}
            data = json.dumps(data1, ensure_ascii=False)
            return data
        else:
            data1 = {"code": 0, "info": "项目名称不能为空"}
            data = json.dumps(data1, ensure_ascii=False)
            return data
Blue_product.add_url_rule("/product/",view_func=Product.as_view("product1"))
# http://127.0.0.1:5002/invoice/product
# http://127.0.0.1:5002/invoice/product?product_name=人力管理系统
# {"product_name":"设备管理系统","product_abbreviation":"SBS","product_explain":"本公司自用系统"}

class ProductEdit(MethodView):
    def get(self):
        product_id = int(request.args.get('product_id'))
        product_r = GetProductOneByProductId(product_id)
        data1 = {"code": 1, "info": "success", "data": product_r}
        data = json.dumps(data1, ensure_ascii=False)
        return data

    def post(self):
        try:
            data_dict = request.json
        except:
            data_dict = request.form
        product_id = int(data_dict['product_id'])
        product_name = data_dict['product_name']
        product_abbreviation = data_dict['product_abbreviation']
        product_explain = data_dict['product_explain']
        if product_name == None:
            data1 = {"code": 0, "info": "项目名称不能为空"}
            data = json.dumps(data1, ensure_ascii=False)
            return data
        UpdateProduct(product_id, product_name, product_abbreviation, product_explain)
        data1 = {"code": 1, "info": "success"}
        data = json.dumps(data1, ensure_ascii=False)
        return data
Blue_product.add_url_rule("/product_edit/",view_func=ProductEdit.as_view("product2"))
# http://127.0.0.1:5002/invoice/product_edit/?product_id=2
# http://127.0.0.1:5002/invoice/product_edit/
# {"product_id":2,"product_name":"人力管理系统","product_abbreviation":"RLS","product_explain":"本公司自用系统"}