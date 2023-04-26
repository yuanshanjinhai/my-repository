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

def get_suanshi_result(max_):
    fuhao0 = random.choice(['+', '-', '*', '//'])
    fuhao1 = random.choice(['+', '-', '*', '//'])
    result = 0
    if fuhao0 in "*//":
        if fuhao0 == "*":
            shu0 = random.choice(range(11))
            shu1 = random.choice(range(11))
        if fuhao0 == "//":
            shu0 = random.choice(get_chengfa99_result())
            shu1 = random.choice(range(1,11))
            if shu0 <shu1 or shu0 %shu1 !=0 or shu0 // shu1 > 10:
                return get_suanshi_result(max_)
        suanshi0 = str(shu0) + fuhao0 +str(shu1)
        result += eval(suanshi0)
        if result > max_ or result < 0:
            return get_suanshi_result(max_)
        if fuhao1 in "+-":
            shu2 = random.choice(range(max_+1))
        if fuhao1 == "*":
            if result not in list(range(11)):
                return get_suanshi_result(max_)
            shu2 = random.choice(range(11))
        if fuhao1 == "//":
            shu2 = random.choice(range(1,11))
            if result not in get_chengfa99_result() or result//shu2 >10 or result < shu2 or result % shu2 != 0:
                return get_suanshi_result(max_)
        suanshi1 = str(result) + fuhao1 + str(shu2)
        result = eval(suanshi1)
        if result >max_ or result <0:
            return get_suanshi_result(max_)

    if fuhao0 in "+-" and fuhao1 in "+-":
        shu0 = random.choice(range(max_+1))
        shu1 = random.choice(range(max_+1))
        if fuhao0 == "-" and shu0 <shu1:
            return get_suanshi_result(max_)
        suanshi0 = str(shu0) + fuhao0 +str(shu1)
        result = eval(suanshi0)
        if result > max_ or result < 0:
            return get_suanshi_result(max_)
        shu2 = random.choice(range(max_ + 1))
        suanshi1 = str(result) + fuhao1 + str(shu2)
        result = eval(suanshi1)
        if result > max_ or result < 0:
            return get_suanshi_result(max_)

    if fuhao0 in "+-" and fuhao1 in "*//":
        if fuhao1 == "*":
            shu1 = random.choice(range(11))
            shu2 = random.choice(range(11))
            shu0 = random.choice(range(max_+1))
        if fuhao1 == "//":
            shu1 = random.choice(get_chengfa99_result())
            shu2 = random.choice(range(1,11))
            shu0 = random.choice(range(max_ // 2))
            if shu1 < shu2 or shu1 % shu2 != 0 or shu1 // shu2 >10:
                return get_suanshi_result(max_)
        suanshi = str(shu1) +fuhao1 +str(shu2)
        result = eval(suanshi)
        if fuhao0 == "//":
            if shu0 not in get_chengfa99_result() or shu0 < result or shu0 // result >10:
                return get_suanshi_result(max_)
        suanshi = str(shu0) + fuhao0 + str(result)
        result = eval(suanshi)
        if result > max_ or result < 0:
            return get_suanshi_result(max_)

    last_suanshi = str(shu0) + fuhao0 + str(shu1) + fuhao1 + str(shu2) +"="
    last_suanshi = last_suanshi.replace("*","×")
    last_suanshi = last_suanshi.replace("//", "÷")
    return [last_suanshi, result]

def get_jiajianchengchu_san(max_,loop_count):
    rlist = []
    tem_list = []

    for i in range(loop_count):
        suanshi_result_list = get_suanshi_result(max_)
        tem_list.append(suanshi_result_list)
        if len(tem_list) == 50:
            tem_list1 = copy.deepcopy(tem_list)
            rlist.append(tem_list1)
            tem_list = []

    count_zu = 1
    rstr = ''
    for i in rlist:
        rstr += "第" + str(count_zu) + "组算式：\n"
        count5 = 0
        for i1 in i:
            if count5 < 4:
                rstr += i1[0]+'   '
            if count5 == 4:
                rstr += i1[0]
                rstr += '\n\n'
                count5 = 0
                continue
            count5 += 1
        count_zu += 1
        rstr += "\n"

    count_zu = 1
    for i in rlist:
        rstr += "第" + str(count_zu) + "组答案：\n"
        count5 = 0
        for i1 in i:
            if count5 < 4:
                temr = i1[0]+str(i1[1]) +'；'
                rstr += temr
            if count5 == 4:
                temr = i1[0] + str(i1[1]) + '\n'
                rstr += temr
                count5 =0
                continue
            count5 += 1
        count_zu += 1
        # rstr += "\n"

    return rstr

print(get_jiajianchengchu_san(200,1000))