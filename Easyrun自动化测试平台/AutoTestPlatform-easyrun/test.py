#encoding=utf-8
import os
import os.path
count_dir=0
count_file=0
mydir_list=[]
myfile_list=[]
for root,dir_list,file_list in os.walk(r"D:\test\2",topdown=False):
    pass
print("root=",root)
print("dir_list=",dir_list)
print("file_list=",file_list)
