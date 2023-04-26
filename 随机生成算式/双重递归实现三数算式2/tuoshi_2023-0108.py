# coding=utf-8
import random
import copy

def get_chengfa99_result():
    rlist=[]
    for i in range(1,10):
        for i1 in range(1,i+1):
            rlist.append(i*i1)
    return list(set(rlist))

def get_chengfa99_suanshi():
    rlist=[]
    for i in range(1,10):
        for i1 in range(1,i+1):
            rlist.append((i,i1))
    return rlist

def judge_shu(shu0,shu1,fuhao,max_):
    if fuhao == "+":
        if shu0 + shu1 > max_:
            return -1
    if fuhao == "-":
        if shu0 - shu1 < 0:
            return -1
    if fuhao == "*":
        if shu0 not in range(1,11) or shu1 not in range(11):
            return -1
    if fuhao == "//":
        if shu0 not in get_chengfa99_result() or shu1 not in range(1,11) or shu0 % shu1 != 0 or shu0//shu1 > 10 or shu0 < shu1:
            return -1

def get_one_yuanshi_suanshi_list(shu_count,max_):
    yuanshi_suanshi_list = []
    for i in range(shu_count):
        shu = random.choice(range(2, max_ + 1))
        yuanshi_suanshi_list.append(shu)
        fuhao = random.choice(['+', '-', '*', '//'])
        yuanshi_suanshi_list.append(fuhao)
    yuanshi_suanshi_list = yuanshi_suanshi_list[0:-1]
    # print('yuanshi_suanshi_list=', yuanshi_suanshi_list, type(yuanshi_suanshi_list))
    if ('*' not in yuanshi_suanshi_list and '//' not in yuanshi_suanshi_list) or ('+' not in yuanshi_suanshi_list and '-' not in yuanshi_suanshi_list):
        return get_one_suanshi_list(shu_count, max_)
    else:
        for i in range(len(yuanshi_suanshi_list)):
            chengfa99_suanshi_list = get_chengfa99_suanshi()
            shu01_list = []
            for i1 in chengfa99_suanshi_list:
                shu01_list.append(i1[0])
                shu01_list.append(i1[1])
            if yuanshi_suanshi_list[i] == "*":
                if yuanshi_suanshi_list[i-1] not in shu01_list:
                    yuanshi_suanshi_list[i-1] = random.choice(range(1, 10))
                yuanshi_suanshi_list[i+1] = random.choice(range(1, 10))
            if yuanshi_suanshi_list[i] == "//":
                chengfa99_suanshi = random.choice(chengfa99_suanshi_list)
                shu0 = chengfa99_suanshi[0] * chengfa99_suanshi[1]
                shu1 = chengfa99_suanshi[random.choice([0,1])]
                if yuanshi_suanshi_list[i-1] not in get_chengfa99_result():
                    yuanshi_suanshi_list[i - 1] = shu0
                    yuanshi_suanshi_list[i+1] = shu1
                elif yuanshi_suanshi_list[i-1] in get_chengfa99_result():
                    shu1_list = []
                    for i2 in range(1,11):
                        if shu0 % i2 == 0:
                            shu1_list.append(i2)
                    yuanshi_suanshi_list[i + 1] = random.choice(shu1_list)
    return yuanshi_suanshi_list

def get_one_suanshi_list(shu_count,max_):
    yuanshi_suanshi_list = get_one_yuanshi_suanshi_list(shu_count,max_)
    for i in range(len(yuanshi_suanshi_list)):
        if isinstance(yuanshi_suanshi_list[i],int) != 1:
            if judge_shu(yuanshi_suanshi_list[i - 1], yuanshi_suanshi_list[i + 1], yuanshi_suanshi_list[i], max_) == -1:
                get_one_suanshi_list(shu_count, max_)
                break
    result = eval(''.join(list(map(lambda x:str(x),yuanshi_suanshi_list))))
    if result > max_ or result < 0:
        return get_one_suanshi_list(shu_count, max_)
    else:
        return yuanshi_suanshi_list

def get_suanshi_and_result(yuanshi_suanshi_list):
    suanshi_str = ''.join(list(map(lambda x:str(x),yuanshi_suanshi_list)))
    result = eval(suanshi_str)
    suanshi_str = suanshi_str.replace("*", "×")
    suanshi_str = suanshi_str.replace("//", "÷")
    suanshi_str += '='
    return (suanshi_str,result)

def get_suanshi_result(shu_count,max_,loop_count):
    tem_list = []
    rlist = []
    for i in range(loop_count):
        one_suanshi_list = get_one_suanshi_list(shu_count,max_)
        tem_tuple = get_suanshi_and_result(one_suanshi_list)
        tem_list.append(tem_tuple)
        if len(tem_list) == 20:
            tem_list1 = copy.deepcopy(tem_list)
            rlist.append(tem_list1)
            tem_list = []

    count_zu = 1
    rstr = ''
    for i in rlist:
        rstr += "第" + str(count_zu) + "组算式：\n\n\n\n"
        count5 = 0
        for i1 in i:
            if count5 < 3:
                rstr += i1[0]+'         '
            if count5 >= 3:
                rstr += i1[0]
                rstr += '\n\n\n\n\n'
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
    suanshi_list = get_suanshi_result(3,1000,1000)
    print(suanshi_list)

