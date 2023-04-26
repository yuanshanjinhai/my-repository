#coding=utf-8
import os

# excel路径：
excel_path=os.path.dirname(os.path.dirname(__file__))+"\\Kwyword_Data\\kd.xlsx"

# 日志路径
log_path= os.path.dirname(os.path.dirname(__file__)) +"\\test_log\\test_log.log"

# 数据记录文件路径，该文件用于记录已创建过的数据，避免自动创建时出现数据重复而无法创建成功
data_record_path=os.path.dirname(os.path.dirname(__file__)) +"\\config_data_record\\data_record.conf"

# 窗口句柄记录文件的路径
handles_path=os.path.dirname(os.path.dirname(__file__)) +"\\config_data_record\\handles_record.conf"

path1 = os.getcwd()
path2 = os.path.dirname(os.path.dirname(__file__))
if __name__ == '__main__':
    print(path1)
    print(path2)