# coding=utf-8
from flask_wtf import FlaskForm
import wtforms

class CaseListForm(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    search_sub = wtforms.SubmitField("搜索")
    upload_sub = wtforms.SubmitField("上传(覆盖)")
    select_file = wtforms.FileField("选择附件")
    download_template_sub = wtforms.SubmitField("模板下载")
    download_case_sub = wtforms.SubmitField("用例下载")
    get_id = wtforms.StringField('获取id')
    delete_sub = wtforms.SubmitField('删除')

class CaseNVECForm(FlaskForm):
    product_name = wtforms.SelectField("项目名称")
    S1_sub = wtforms.SubmitField("①～＞")
    case_group = wtforms.SelectField("用例组")
    interface_name = wtforms.SelectField("接口")
    S2_sub = wtforms.SubmitField("②～＞")
    method = wtforms.StringField("方法")
    interface_address = wtforms.StringField("用例地址")
    case_name = wtforms.StringField("用例名称")
    case_order = wtforms.StringField("用例顺序")
    is_urlencode_pwd = wtforms.SelectField("编码/加解密", choices=[("0", "无"), ("1", "url编码-url解码"), ("2", "加密-解密"),
                                                             ("3", "url编码-加密-解密-url解码"), ("4", "仅url编码"),("5", "仅url解码")])
    encrypt_decrypt_file = wtforms.SelectField('加解密文件')
    #
    case_explain = wtforms.StringField("用例说明")
    header = wtforms.StringField("请求头")
    body = wtforms.TextAreaField("请求体")
    expect_response = wtforms.TextAreaField("预期返回值")
    submit_sub = wtforms.SubmitField("提交")