# coding=utf-8
import random
import string

def creat_word(word_lenth,word_type):
    result_str = ""
    if word_type == "中文":
        # chinese_str = "我爱你中国"
        # chinese_list = list(map(lambda x:x,chinese_str))
        for ir in range(word_lenth-1):
            result_str += random.choice("你")
        result_str += "好"

    if word_type == "英文":
        englist_str = string.ascii_lowercase + string.ascii_uppercase
        englist_list = list(map(lambda x:x,englist_str))
        for ir in range(word_lenth):
            result_str += random.choice(englist_list)

    if word_type == "数字":
        digit_str = "0123456789"
        digit_list = list(map(lambda x:x,digit_str))
        for ir in range(word_lenth):
            result_str += random.choice(digit_list)

    if word_type == "符号":
        punctuation_str = string.punctuation
        punctuation_list = list(map(lambda x:x,punctuation_str))
        for ir in range(word_lenth):
            result_str += random.choice(punctuation_list)

    if word_type == "综合":
        chinese_str = "我爱你中国"
        chinese_list = list(map(lambda x: x, chinese_str))
        englist_str = string.ascii_lowercase + string.ascii_uppercase
        englist_list = list(map(lambda x: x, englist_str))
        digit_str = "0123456789"
        digit_list = list(map(lambda x: x, digit_str))
        punctuation_str = string.punctuation
        punctuation_list = list(map(lambda x: x, punctuation_str))

        result_str = punctuation_str + "我A0"
        for ir in range(word_lenth - 35):
            result_str += random.choice(chinese_list + englist_list + digit_list + punctuation_list)

    return [result_str]

def creat_punctuation(every_lenth=None):
    result_list = []
    if every_lenth == None:
        result_list.append(string.punctuation)
        return result_list
    else:
        if 32 % every_lenth == 0:
            how_many = 32 // every_lenth
        else:
            how_many = 32 // every_lenth +1
        start = 0
        for ir in range(how_many):
            if ir != how_many:
                result_list.append(string.punctuation[start:start+every_lenth])
                start += every_lenth
            else:
                result_list.append(string.punctuation[start::])
        return result_list


if __name__ == '__main__':
    print(creat_word(40,"综合"))
    print(string.punctuation)
    print(creat_punctuation(3))