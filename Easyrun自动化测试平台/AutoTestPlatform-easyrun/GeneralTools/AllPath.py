# coding=utf-8
import os

encrypt_decrypt_load_path0 = os.path.dirname(os.path.dirname(__file__)) + r"\interface_test\encrypt_decrypt\encrypt_decrypt_load" + '\\'  # 上传或下载加解密文件目录

encrypt_decrypt_temlete_path = os.path.dirname(os.path.dirname(__file__)) + r"\interface_test\encrypt_decrypt\encrypt_decrypt_temlete" + '\\'

PwdTemlete_path = os.path.dirname(os.path.dirname(__file__)) + r"/interface_test/encrypt_decrypt/encrypt_decrypt_temlete/"

UploadAndDownloadCaseFile_path = os.path.dirname(os.path.dirname(__file__)) + r"/interface_test/case/case_upload_and_download/"

UploadCaseFile_path = "a"

# DownloadCaseFile_path = os.path.dirname(os.path.dirname(__file__)) + r"/interface_test/case/case_download/"

CaseTemplete_path = os.path.dirname(os.path.dirname(__file__)) + r"/interface_test/case/case_template/"

CaseRule_path = os.path .dirname(os.path.dirname(__file__)) + r"/helps/case_rule"

if __name__ == '__main__':
    print(UploadCaseFile_path)
