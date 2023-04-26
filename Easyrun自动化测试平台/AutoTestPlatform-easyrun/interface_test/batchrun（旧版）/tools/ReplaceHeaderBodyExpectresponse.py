# coding=utf-8
from GeneralTools.ExcelAllSheet import *
from GeneralTools.OtherTools import RemoveSpacesAndEnter
from interface_test.batchrun.tools.other_tools import get_global_value
import re


def ReplaceHeaderBodyExpectresponse(excel_case_path,username,depended_total_str,actual_respone_str,start_index): # 用于把被传入的str中的所有【】替换成具体值
    ins_excel = ExcelAllSheet(excel_case_path)
    # sheet_list = ins_excel.get_SheetList()
    # case_sheet = "用例" # 获取sheet的名称
    # global_sheet = "全局变量"
    depended_total_str = RemoveSpacesAndEnter(depended_total_str)
    is_remove_yinhao = 0
    for i_index in range(start_index,len(depended_total_str)):
        if depended_total_str[i_index] == "【":
            match_string = re.search(r"【\S+?】", depended_total_str).group()
            if "【时间||" in match_string: # 只有预期返回值里才会有时间数据，而预期返回值是在执行完接口得到实际返回值后才会替换【】
                # 获取预期返回值中被替换的值的键
                expectresponse_key = re.findall(r'(?<=")\w+(?=":"【时间\|\|)',depended_total_str)[0]
                # 通过预期返回值中被替换的值的键来获取实际返回值中生成的时间字符串
                depend_str_list = re.findall('(?<='+str(expectresponse_key)+'":").*?(?=")',actual_respone_str) ### expectresponse_key可能应该是actual_respone_str
                if depend_str_list != []:
                    depend_str = depend_str_list[0]
                    time_fromat_dict = {1: "\d+{10}", 2: "\d+{13}", 3: "\d{4}-\d{2}-\d{2}\s{1}\d{2}:\d{2}:\d{2}",
                                        4: "\d{4}/\d{2}/\d{2}\s\d{2}:\d{2}:\d{2}",
                                        5: "\d{4}\s\d{2}\s\d{2}\s\d{2}:\d{2}:\d{2}"}
                    time_fromat_id = int(match_string.split("||")[1][0])
                    re_str = time_fromat_dict[time_fromat_id]
                    if re.findall(re_str,depend_str) == []:
                        depend_str = "时间格式错误！"
                elif depend_str_list == []:
                    depend_str = "json中无此键！"
                depended_total_str = depended_total_str.replace(match_string, depend_str, 1)
                depended_total_str = ReplaceHeaderBodyExpectresponse(excel_case_path,username, depended_total_str, actual_respone_str, i_index)
                return depended_total_str
            elif re.findall(r"【a】|【d】|【ad】|【a\|\|\d+】|【d\|\|\d+】|【ad\|\|\d+】",match_string) != []: # 只有预期返回值里才会有这种数据，而预期返回值是在执行完接口得到实际返回值后才会替换【】
                # 获取预期返回json中被替换的值的键
                expectresponse_key = re.findall(r'(?<=")\w+?(?=":"【)', depended_total_str)[0]
                # 通过预期json中被替换的值的键来获取实际json中对应的值
                if re.findall(r"【d】|【d\|\|\d+】",match_string) !=[]:
                    depend_str_list = re.findall('(?<=' + str(expectresponse_key) + '":)\d+', actual_respone_str)
                else:
                    depend_str_list = re.findall('(?<=' + str(expectresponse_key) + '":")\w+', actual_respone_str)
                if depend_str_list != []:
                    depend_str = depend_str_list[0]
                    if re.findall(r"【a】",match_string) != []:
                        if re.findall(r"[a-zA-Z]+",depend_str) == []:
                            depend_str = "对应值格式错误！"
                    if re.findall(r"【d】", match_string) != []:
                        depended_total_str = depended_total_str.replace('"【d】"', '【d】', 1)
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
                    depend_str = "json中无此键！"
                depended_total_str = depended_total_str.replace(match_string , depend_str, 1)
                depended_total_str = ReplaceHeaderBodyExpectresponse(excel_case_path,username, depended_total_str, actual_respone_str, i_index)
                return depended_total_str
            elif "【+" in match_string: # 请求体才会有这种数据
                if "||" not in match_string:
                    global_key = match_string[2:-1]
                    global_value = get_global_value(excel_case_path, global_key)
                    depend_str = global_value
                if "||" in match_string:
                    global_key = match_string.split("||")[1][0:-1]
                    global_value = get_global_value(excel_case_path, global_key)
                    depend_str = match_string.split("||")[0][2::] + global_value
                depended_total_str = depended_total_str.replace(match_string, depend_str, 1)
                depended_total_str = ReplaceHeaderBodyExpectresponse(excel_case_path,username, depended_total_str, actual_respone_str, i_index)
                return depended_total_str
            elif re.findall(r"\$\|\|\w+",match_string) != []: # 请求头、请求体、预期返回值，都会有这种数据
                depend_function = match_string[1:-1].split("||")[1]
                for iin in range(i_index,1,-1):
                    if ins_excel.get_value("用例","A"+str(iin)) == "$":
                        if ins_excel.get_value("用例","D"+str(iin)) == depend_function:
                            depend_str_path = ins_excel.get_value("用例","I"+str(iin))
                            for i_iin in range(iin,1,-1):
                                if ins_excel.get_value("用例","A"+str(i_iin)) != "$":
                                    depend_actual_response = ins_excel.get_value("用例","J"+str(i_iin))
                                    try:
                                        depend_str = eval(depend_actual_response + depend_str_path)
                                        if isinstance(depend_str,int) == 1:
                                            is_remove_yinhao = 1
                                    except:
                                        depend_str = "json中无此键！"
                                    break
                            break
                # print("depend_str=",depend_str)
                # if "【+" in depend_str:
                #     print("depend_str1=",depend_str,depend_str[2:-1])
                #     if "||" not in depend_str:
                #         global_key = depend_str[2:-1]
                #         print("global_key0=",global_key)
                #         global_value = get_global_value(excel_case_path, global_key)
                #         depend_str = global_value
                #     if "||" in depend_str:
                #         global_key = depend_str.split("||")[1][0:-1]
                #         print("global_key1=",global_key)
                #         global_value = get_global_value(excel_case_path, global_key)
                #         depend_str = depend_str.split("||")[0][2::] + global_value
                #     print("depend_str=",depend_str)
                # elif re.findall(r"【a】|【d】|【ad】|【a\|\|\d+】|【d\|\|\d+】|【ad\|\|\d+】",depend_str) != []:
                #     # 获取预期返回json中被替换的值的键
                #     print("depended_total_str=",depended_total_str)
                #     expectresponse_key = re.findall(r'(?<=")\w+?(?=":"【)', depended_total_str)[0]
                #     # expectresponse_key = depend_key
                #     print("expectresponse_key=",expectresponse_key)
                #     # 通过预期json中被替换的值的键来获取实际json中对应的值
                #     # depend_str_list = re.findall('(?<=' + str(expectresponse_key) + '":).*?(?=,")|(?<=' + str(
                #     #     expectresponse_key) + '":).*?(?=})', actual_respone_str)
                #     actual_respone_str_depend = ins_excel.get_value("用例","J" + str(i_iin))
                #     actual_respone_str_depend = RemoveSpaces(actual_respone_str_depend)
                #     if re.findall(r"【d|【d\|\|\d+】",depend_str) != []:
                #         print("actual_respone_str_depended=",actual_respone_str_depend)
                #         depend_str_list = re.findall('(?<="' + str(expectresponse_key) + '":)\w+', actual_respone_str_depend)
                #         is_remove_yinhao = 1
                #     else:
                #         depend_str_list = re.findall('(?<="' + str(expectresponse_key) + '":")\w+', actual_respone_str_depend)
                #     print("depend_str_list=",depend_str_list)
                #     if depend_str_list != []:
                #         depend_str = depend_str_list[0]
                #         if re.findall(r"【a】", match_string) != []:
                #             if re.findall(r"[a-zA-Z]+", depend_str) == []:
                #                 depend_str = "对应值格式错误！"
                #         if re.findall(r"【d】", match_string) != []:
                #             if re.findall(r"\d+", depend_str) == []:
                #                 depend_str = "对应值格式错误！"
                #         if re.findall(r"【ad】", match_string) != []:
                #             if re.findall(r"\w+", depend_str) == []:
                #                 depend_str = "对应值格式错误！"
                #         if re.findall(r"【a\|\|\d+】", match_string) != []:
                #             str_len = match_string[0:-1].split("|")[1]
                #             if re.findall("[a-zA-Z]{" + str_len + "}", depend_str) == []:
                #                 depend_str = "对应值格式错误！"
                #         if re.findall(r"【d\|\|\d+】", match_string) != []:
                #             str_len = match_string[0:-1].split("|")[1]
                #             if re.findall("\d{" + str_len + "}", depend_str) == []:
                #                 depend_str = "对应值格式错误！"
                #         if re.findall(r"【ad\|\|\d+】", match_string) != []:
                #             str_len = match_string[0:-1].split("|")[1]
                #             if re.findall("\w{" + str_len + "}", depend_str) == []:
                #                 depend_str = "对应值格式错误！"
                #     elif depend_str_list == []:
                #         depend_str = "json中无此键！"
                if is_remove_yinhao == 0 or depend_str == "json中无此键！":
                    depended_total_str = depended_total_str.replace(match_string,str(depend_str),1)
                elif is_remove_yinhao == 1:
                    depended_total_str = depended_total_str.replace('"' + match_string + '"', str(depend_str), 1)
                depended_total_str = ReplaceHeaderBodyExpectresponse(excel_case_path,username, depended_total_str, actual_respone_str, i_index)
                return depended_total_str
    return depended_total_str