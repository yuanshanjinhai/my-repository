# coding=utf-8

def TransformXpathShuangyinhao(thisxpath): # 把action字符串里的双引号全部替换成单引号
    tem_list=[]
    for ia in thisxpath:
        if ia=="\"":
            tem_list.append("'")
            continue
        tem_list.append(ia)
    return "".join(tem_list)

if __name__ == '__main__':
    print(TransformXpathShuangyinhao("""jds'dfs'fd"dfas"fdfas"""))