# coding=utf-8
import re
from GeneralTools.OtherTools import RemoveSpacesAndEnter
from interface_test.run_case.DB.GetGlobalVarValue import *
from interface_test.run_case.DB.GetDependStrByRelationName import *

def Replace_HBE(product_id,HBE_str,actual_respone_str,start_index):
    is_remove_yinhao = 0
    for i_index in range(start_index, len(HBE_str)):
        if HBE_str[i_index] == "【":
            match_string = re.search(r"【\S+?】", HBE_str).group()
            if "【时间" in match_string:  # 只有预期返回值里才会有时间数据，而预期返回值是在执行完接口得到实际返回值后才会替换【】
                # 获取预期返回值中被替换的值的键
                expectresponse_key = re.findall(r'(?<=")\w+(?=":"【时间)', HBE_str)[0]
                # 通过预期返回值中被替换的值的键来获取实际返回值中生成的时间字符串
                depend_str_list = re.findall('(?<=' + str(expectresponse_key) + '":").*?(?=")',actual_respone_str)  # expectresponse_key可能应该是actual_respone_str
                if depend_str_list != []:
                    depend_str = depend_str_list[0]
                    time_fromat_dict = {1: "\d+{10}", 2: "\d+{13}", 3: "\d{4}-\d{2}-\d{2}\s{1}\d{2}:\d{2}:\d{2}",
                                        4: "\d{4}/\d{2}/\d{2}\s\d{2}:\d{2}:\d{2}",
                                        5: "\d{4}\s\d{2}\s\d{2}\s\d{2}:\d{2}:\d{2}"}
                    time_fromat_id = int(match_string[-2])
                    re_str = time_fromat_dict[time_fromat_id]
                    if re.findall(re_str, depend_str) == []:
                        depend_str = "时间格式错误！"
                elif depend_str_list == []:
                    depend_str = "json中无此键！"
                HBE_str = HBE_str.replace(match_string, depend_str, 1)
                HBE_str = Replace_HBE(product_id, HBE_str, actual_respone_str, i_index)
                return HBE_str
            elif re.findall(r"【a】|【d】|【ad】|【a\|\|\d+】|【d\|\|\d+】|【ad\|\|\d+】",match_string) != []:  # 只有预期返回值里才会有这种数据，而预期返回值是在执行完接口得到实际返回值后才会替换【】
                # 获取预期返回json中被替换的值的键
                expectresponse_key = re.findall(r'(?<=")\w+?(?=":"【)', HBE_str)[0]
                # 通过预期json中被替换的值的键来获取实际json中对应的值
                if re.findall(r"【d】|【d\|\|\d+】", match_string) != []:
                    depend_str_list = re.findall('(?<=' + str(expectresponse_key) + '":)\d+', actual_respone_str)
                else:
                    depend_str_list = re.findall('(?<=' + str(expectresponse_key) + '":")\w+', actual_respone_str)
                if depend_str_list != []:
                    depend_str = depend_str_list[0]
                    if re.findall(r"【a】", match_string) != []:
                        if re.findall(r"[a-zA-Z]+", depend_str) == []:
                            depend_str = "对应值格式错误！"
                    if re.findall(r"【d】", match_string) != []:
                        HBE_str = HBE_str.replace('"【d】"', '【d】', 1)
                        if re.findall(r"\d+", depend_str) == []:
                            depend_str = "对应值格式错误！"
                    if re.findall(r"【ad】", match_string) != []:
                        if re.findall(r"\w+", depend_str) == []:
                            depend_str = "对应值格式错误！"
                    if re.findall(r"【a\|\|\d+】", match_string) != []:
                        str_len = match_string[0:-1].split("||")[1]
                        if re.findall("[a-zA-Z]{" + str_len + "}", depend_str) == []:
                            depend_str = "对应值格式错误！"
                    if re.findall(r"【d\|\|\d+】", match_string) != []:
                        str_len = match_string[0:-1].split("||")[1]
                        if re.findall("\d{" + str_len + "}", depend_str) == []:
                            depend_str = "对应值格式错误！"
                    if re.findall(r"【ad\|\|\d+】", match_string) != []:
                        str_len = match_string[0:-1].split("||")[1]
                        if re.findall(r"\w{" + str_len + "}", depend_str) == []:
                            depend_str = "对应值格式错误！"
                elif depend_str_list == []:
                    depend_str = "实际返回json中无此键222！"
                HBE_str = HBE_str.replace(match_string, depend_str, 1)
                HBE_str = Replace_HBE(product_id, HBE_str, actual_respone_str, i_index)
                return HBE_str
            elif  re.findall(r"【\S+\|\|[a-zA-Z]\d+】",match_string) != [] and '+' not in match_string: # 处理预期返回值中的【guolint||G1】
                global_var_name = match_string.split('||')[1][0:-1]
                global_var_value = GetGlobalVarValue(product_id, global_var_name)
                depend_str = match_string.split('||')[0][1::] + str(global_var_value)
                HBE_str = HBE_str.replace(match_string, depend_str, 1)
                HBE_str = Replace_HBE(product_id, HBE_str, actual_respone_str, i_index)
            elif "【+" in match_string:  # 请求体才会有这种数据
                global_var_name = match_string[2:-1]
                global_var_value = GetGlobalVarValue(product_id,global_var_name.split('||')[1])
                depend_str = global_var_name.split("||")[0] + global_var_value
                HBE_str = HBE_str.replace(match_string, depend_str, 1)
                HBE_str = Replace_HBE(product_id,HBE_str, actual_respone_str, i_index)
                return HBE_str
            elif re.findall(r"\$\w+", match_string) != []:  # 请求头、请求体、预期返回值，都会有这种数据
                relation_name = match_string[1:-1]
                depend_str = GetDependStrByRelationName(product_id,relation_name)
                if isinstance(depend_str, int) == 1:
                    is_remove_yinhao = 1
                if is_remove_yinhao == 0 or depend_str == "json中无此键！":
                    HBE_str = HBE_str.replace(match_string, str(depend_str), 1)
                elif is_remove_yinhao == 1:
                    HBE_str = HBE_str.replace('"' + match_string + '"', str(depend_str), 1)
                HBE_str = Replace_HBE(HBE_str, actual_respone_str, i_index)
                return HBE_str
    return HBE_str