# coding=utf-8
import random
import copy

def get_chengfa99_result():
    rlist=[0]
    for i in range(1,10):
        for i1 in range(1,i+1):
            rlist.append(i*i1)
    rlist = list(set(rlist))
    return rlist

def judge_shu(shu0,shu1,fuhao,max_):
    if fuhao == "+":
        if shu0 + shu1 > max_:
            return -1
    if fuhao == "-":
        if shu0 - shu1 < 0:
            return -1
    if fuhao == "*":
        if shu0 not in range(11) or shu1 not in range(11):
            return -1
    if fuhao == "//":
        if (shu0 not in get_chengfa99_result() or shu1 not in range(1,11)) or shu0 % shu1 != 0 or shu0//shu1 > 10:
            return -1

def jisuan_suanshi(suanshi_list,max_):
    if len(suanshi_list) == 1:
        return suanshi_list[0]
    elif '*' not in suanshi_list and '//' not in suanshi_list:
        for i in range(len(suanshi_list)):
            if suanshi_list[i] == '+' or suanshi_list[i] == '-':
                if judge_shu(suanshi_list[i - 1], suanshi_list[i + 1], suanshi_list[i], max_) == -1:
                    return -1
                else:
                    tem_suanshi_str = str(suanshi_list[i - 1]) + suanshi_list[i] + str(suanshi_list[i + 1])
                    tem_r = eval(tem_suanshi_str)
                    if tem_r < 0 or tem_r > max_:
                        return -1
                    else:
                        new_suanshi_list = suanshi_list[0:i - 1] + [tem_r, ] + suanshi_list[i + 2::]
                return jisuan_suanshi(new_suanshi_list, max_)

    for i in range(len(suanshi_list)):
        if suanshi_list[i] == '*' or suanshi_list[i] == '//':
            if judge_shu(suanshi_list[i-1],suanshi_list[i+1],suanshi_list[i],max_) == -1:
                return -1
            else:
                tem_suanshi_str = str(suanshi_list[i-1]) + suanshi_list[i] + str(suanshi_list[i+1])
                tem_r = eval(tem_suanshi_str)
                if tem_r > max_:
                    return -1
                else:
                    new_suanshi_list = suanshi_list[0:i-1] + [tem_r,] + suanshi_list[i+2::]
            return jisuan_suanshi(new_suanshi_list, max_)

def get_suanshi(shu_count,max_):
    suanshi_list = []
    for i in range(shu_count):
        shu = random.choice(range(0,max_+1))
        suanshi_list.append(shu)
        fuhao = random.choice(['+', '-', '*', '//'])
        suanshi_list.append(fuhao)
    suanshi_list = suanshi_list[0:-1]
    r = jisuan_suanshi(suanshi_list,max_)
    if r == -1:
        return get_suanshi(shu_count, max_)
    else:
        suanshi_str = ""
        for i in suanshi_list:
            suanshi_str += str(i)
        suanshi_str = suanshi_str.replace("*","×")
        suanshi_str = suanshi_str.replace("//","÷")
        return (suanshi_str + "=",r)

def get_suanshi_result(shu_count,max_,loop_count):
    tem_list = []
    rlist = []
    for i in range(loop_count):
        tem_tuple = get_suanshi(shu_count,max_)
        tem_list.append(tem_tuple)
        if len(tem_list) == 20:
            tem_list1 = copy.deepcopy(tem_list)
            rlist.append(tem_list1)
            tem_list = []

    count_zu = 1
    rstr = ''
    for i in rlist:
        rstr += "第" + str(count_zu) + "组算式：\n"
        count5 = 0
        for i1 in i:
            if count5 < 3:
                rstr += i1[0]+'       '
            if count5 >= 3:
                rstr += i1[0]
                rstr += '\n\n\n\n'
                count5 = 0
                continue
            count5 += 1
        count_zu += 1
        # rstr += "\n"

    count_zu = 1
    for i in rlist:
        rstr += "第" + str(count_zu) + "组答案：\n"
        count5 = 0
        for i1 in i:
            if count5 < 3:
                temr = i1[0]+str(i1[1]) +'；'
                rstr += temr
            if count5 == 3:
                temr = i1[0] + str(i1[1]) + '\n'
                rstr += temr
                count5 =0
                continue
            count5 += 1
        count_zu += 1

    return rstr

if __name__ == '__main__':
    # print( get_suanshi(3,1000) )
    print( get_suanshi_result(3,999,1000) )