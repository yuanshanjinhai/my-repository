# coding=utf-8
from ProjectVar.var import log_path

class Writelog():
    def __init__(self):
        self.log_path=log_path
        self.fp=open(log_path,"a",encoding="utf-8")

    def writelog(self,*args):
        for i in args:
            self.fp.write(i)
            self.fp.write(" ")

    def closefp(self):
        self.fp.close()

if __name__=="__main__":
    from Util.excel import *
    from ProjectVar.var import *
    logpath = "D:\\test\\test.log"
    wl=Writelog(logpath)
    wl.writelog("hello2")
    wl.closefp()
    #writelog(date_time()+ ",用户" + userins.get_value("B2") + "创建了联系人：" + eins.get_value("B2").decode("utf-8"))
