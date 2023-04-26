# coding=utf-8
from ProjectVar.var import *

# 向配置文件中插入已自动生成的名称
def write_data(aim_str):
    fp=open(data_record_path,"r",encoding="utf-8")
    line_list = fp.readlines()
    if line_list!=[]: # 如果配置文件不为空，则先查找aim_str该插入到哪行
        aim_str1="".join([i for i in aim_str if str.isdigit(i)==0]) # aim_str1是去掉了数字后缀的aim_str
        line_count=0
        aim_str1_isexist=0 # 用于记录配置文件里是否已存在于aim_str一致的行
        for il in line_list:
            if aim_str1 in il: # 如果aim_str1在该行中，则就把aim_str插入到这行里
                il=il.strip()+"||"+aim_str+"\n"
                line_list[line_count]=il
                aim_str1_isexist=1 # 插入后，把此值置为1，表示已插入过
                break
            line_count+=1
        if aim_str1_isexist==0: # 如果此值为0，证明没插入过aim_str，进一步证明配置文件里没有与aim_str一致的行
            line_list.append(aim_str+"\n") # 把aim_str作为这一系列的第一个值，单起一行插入
    else: # 如果配置文件为空，则证明是第一次插入，则直接插入即可
        line_list.append(aim_str+"\n")
        fp.close()

    fp=open(data_record_path,"w",encoding="utf-8")
    for il in line_list:
        fp.write(il)
    fp.close()

# 自动生成名称
def auto_name(aim_str):
    fp=open(data_record_path,"r",encoding="utf-8")
    line_list=fp.readlines()
    for il in line_list:
        if aim_str[0:-1] in il:
            num_str=int("".join([i for i in il.split("||")[-1] if str.isdigit(i)==1]))
            fp.close()
            return aim_str[0:-1]+str(num_str+1)
    fp.close()
    print(aim_str[0:-1]+"1")
    return aim_str[0:-1]+"1"

# 把新句柄写入到配置文件里
def write_handle(handle_dict):
    fp=open(handles_path,"w",encoding="utf-8")
    fp.write(str(handle_dict))
    fp.close()

# 获取配置文件中的所有窗口句柄
def read_handle():
    fp=open(handles_path,"r",encoding="utf-8")
    handle_list=fp.readlines()
    if handle_list==[]:
        fp.close()
        return {}
    else:
        handle_dict=eval(handle_list[0].strip())
        fp.close()
        return handle_dict

if __name__=="__main__":
    print(auto_name("自动投标%"))
    write_data(auto_name("自动投标%"))

