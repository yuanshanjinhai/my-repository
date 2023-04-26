# coding=utf-8
from ProjectVar.var import excel_path

class check_case():
    def __init__(self,ex):
        self.ex=ex

    def check(self):
        run_SheetList=[]

        for ir in range(12,self.ex.get_max_row("参数设置")+1): # 获得所有欲执行sheet名
            run_SheetList.append(self.ex.get_value("参数设置","A"+str(ir)))
        all_SheetList = self.ex.get_SheetList() # 获取到所有sheet
        error_list=[]
        isloop = 0 # 设置是否循环，0为不循环，1为循环
        for iall in all_SheetList:
            for irun in run_SheetList:
                if "||" in irun:
                    if int(irun.split("||")[1]) < 2 and isloop==0:
                        error_list.append("“参数设置”sheet中的“需要执行的sheet”列的循环次数不能小于2")
                        irun=irun.split("||")[0]
                        isloop=1
                if iall == irun:
                    case_id = 1 # 判断id是否连续，该值从1开始，每循环一次该值+1，每次循环都会取id列的值，如果与该值相等，则认为id连续
                    case_id_error_count = 0 # 判断id是否已出现不连续，如果id列出现一次不连续，则该值被设为1，设为1后，将不再判断id连续性
                    is_baifenhao = 0  # 用于记录用例的数据部分是否有百分号
                    for ir in range(2,self.ex.get_max_row(iall)+1):
                        if self.ex.get_value(iall,"A"+str(ir))=="None":
                            error_str="第"+str(ir)+"行："+"id不能为空"
                            error_list.append(error_str)

                        if self.ex.get_value(iall,"A" + str(ir)) != "None":
                            if str.isdigit(self.ex.get_value(iall,"A"+str(ir)))!=1:
                                error_str="“%s”sheet中，第%d行：用例id只能是数字"%(irun,ir)
                                error_list.append(error_str)
                            if case_id_error_count==0:
                                if str.isdigit(self.ex.get_value(iall,"A"+str(ir)))==1:
                                    if int(self.ex.get_value(iall,"A"+str(ir)))!=case_id:
                                        error_str="“%s”sheet中，第%d行：用例id从此行开始不连续"%(irun,ir)
                                        error_list.append(error_str)
                                        case_id_error_count=1

                        count_I=self.ex.get_value(iall,"I"+str(ir))
                        if count_I!="None":
                            count_space=0
                            for ic in count_I:
                                if ord(ic)==32:
                                    count_space+=1
                            if count_space>0:
                                error_str = "“%s”sheet中，第" % (irun) + str(ir) + "行：" + "是否必填列出现了"+str(count_space)+"个空格，该列可以输入除空格外的所有字符"
                                error_list.append(error_str)

                        loop_time = self.ex.get_value(iall, "J" + str(ir))
                        if loop_time != "None": # 执行失败后再执行的次数只能是数字，且不能小于1
                            if loop_time.isdigit() == 1:
                                if int(loop_time) <= 0:
                                    error_str = "“%s”sheet中，第" % (irun) + str(ir) + "行：" + "重复次数不能小于等于0"
                                    error_list.append(error_str)
                            else:
                                error_str = "“%s”sheet中，第" % (irun) + str(ir) + "行：" + "重复次数只能是数字"
                                error_list.append(error_str)

                        if self.ex.get_value(iall,"L"+str(ir))=="None":
                            error_str ="“%s”sheet中，第"%(irun)+str(ir)+"行："+"是否执行列不能为空"
                            error_list.append(error_str)

                        if self.ex.get_value(iall,"K"+str(ir))=="None":
                            error_str ="“%s”sheet中，第"%(irun)+str(ir)+"行："+"等待时间不能为空"
                            error_list.append(error_str)

                        if self.ex.get_value(iall,"K" + str(ir)) != "None":
                            if str.isdigit(self.ex.get_value(iall,"K" + str(ir))) != 1:
                                error_str = "“%s”sheet中，第%d行：等待时间只能是数字" % (irun,ir)
                                error_list.append(error_str)

                        if self.ex.get_value(iall,"E"+str(ir))=="None" and self.ex.get_value(iall,"E"+str(ir))=="y":
                            error_str ="“%s”sheet中，第"%(irun)+str(ir)+"行："+"函数名称不能为空"
                            error_list.append(error_str)

                        if self.ex.get_value(iall,"F"+str(ir))=="None" and self.ex.get_value(iall,"J"+str(ir))=="y" \
                                and self.ex.get_value(iall,"E"+str(ir))!="outframe" \
                                and self.ex.get_value(iall,"E"+str(ir))!="scroll_bar" \
                                and self.ex.get_value(iall,"E"+str(ir))!="scroll_bar_href" \
                                and self.ex.get_value(iall,"E"+str(ir))!="option_down_arrow" \
                                and self.ex.get_value(iall,"E"+str(ir))!="PageDown" \
                                and self.ex.get_value(iall,"E"+str(ir))!="Enter"\
                                and self.ex.get_value(iall,"E"+str(ir))!="Tab" \
                                and self.ex.get_value(iall, "E" + str(ir)) != "close_window" \
                                and self.ex.get_value(iall, "E" + str(ir)) != "switch_window":
                            error_str ="“%s”sheet中，第"%(irun)+str(ir)+"行："+"定位xpath不能为空"
                            error_list.append(error_str)

                        if self.ex.get_value(iall,"M"+str(ir))=="None" and self.ex.get_value(iall,"J"+str(ir))=="y":
                            error_str ="“%s”sheet中，第"%(irun)+str(ir)+"行："+"流程设计人不能为空"
                            error_list.append(error_str)

                        if self.ex.get_value(iall, "G" + str(ir))!="None" and "%" in self.ex.get_value(iall, "G" + str(ir)):
                            is_baifenhao=1

                        case_id += 1

                    if is_baifenhao==0 and "||" in irun:
                        error_list.append("你设置了“%s”sheet循环%s次，但在对应的sheet中的输入数据列里并未设置变"
                                          "量，这将导致你的输入数据无法通过系统的排重校验" % (irun.split("||")[0],irun.split("||")[1]))

                    break

        return error_list

if __name__=="__main__":
    from Util.ExcelAllSheet import *
    from ProjectVar.var import *
    ex=ExcelAllSheet(excel_path)
    eins=check_case(ex)
    eror_list=eins.check()
    for i in eror_list:
        print(i)