from tkinter import ttk
import pandas as pd
from tkinter import * # 下拉菜单控件在ttk中
import os

import ctypes
import sys

if getattr(sys, 'frozen', False):
    # Override dll search path.
    ctypes.windll.kernel32.SetDllDirectoryW(r'E:\Pythondeanaconda\pkgs\mkl-2021.4.0-haa95532_640\Library\bin')
    # Init code to load external dll
    ctypes.CDLL('mkl_intel_thread.1.dll')


    # Restore dll search path.
    ctypes.windll.kernel32.SetDllDirectoryW(sys._MEIPASS)
###########################获取路径下所有csv格式文件#############
def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.csv':  # 想要保存的文件格式
                L.append(os.path.join(file))
    return L
# print(file_name(r'G:\2021.12'))

##############窗体#######################################
global path
global a
tk=Tk()
tk.title("统药小程序 ver1.0  developed by.XYL")
tk.geometry("600x700+600+200")
tk.resizable(width=False, height=False)
#标签控件，显示文本和位图，展示在第一行
Label(tk, text="文档路径：",font=8).grid(row=0, sticky=W)  # 靠右
Label(tk, text="医生姓名：",font=8).grid(row=1, sticky=W)  # 左
Label(tk, text="查询条件：",font=8).grid(row=2, sticky=W)  #
Label(tk, text="药物名称：",font=8).grid(row=3, sticky=W)  #
Label(tk, text="查询结果：",font=8).grid(row=5, sticky=W)  #
cmb=ttk.Combobox(tk,width=46,font=8)
cmb['value'] = ('点此下拉框选择查询条件','门诊','住院' )
cmb.current(0)
#输入控件
p = StringVar()#文件路径
r = StringVar()#人名
y = StringVar()#药名
path1 = Entry(tk, width=48,font=8,textvariable=p)
path1.grid(row=0, column=1)
name_ren=Entry(tk, width=48,font=8,textvariable=r)
name_ren.grid(row=1,column=1)
cmb.grid(row=2,column=1)
name_yao=Entry(tk, width=48,font=8,textvariable=y)
name_yao.grid(row=3,column=1)
text_jieguo=Text(tk, width=60,height=36,font=5)
text_jieguo.grid(row=5,column=1)

###############查询统计指定药物数量#############
def chaxun(path):
    global a
    duiying_num=[]
    with open(path)as file:
    #取出药名和数量列
        data1=pd.read_csv(file,usecols=[3,6])
        data=data1.iloc[1:]
    # print(data)
    #把药名转为列表
    name=list(data.iloc[:,0])
    # print(name)
    #数量转化为列表
    num=list(data.iloc[:,1])
    # print(num)
    n=r.get()
    a=y.get()
    lei=cmb.get()
    list1=[i for i, j in enumerate(name) if j == a]#某一药品行索引
    for i in list1:
        duiying_num.append(float(num[i]))
    text_jieguo.insert('insert',n+"在"+lei+a+"的数量是: "+str(sum(duiying_num))+"\n")

##############核心函数，实现前端输入获取和后端对文件的查询##############
def submit():
    global path
    path=p.get()
    list_biaoge=file_name(path)
    # print(list_biaoge)
    name=r.get()
    list_ren=[l for l in list_biaoge if name in l]
    # print(list_ren)
    leibie=cmb.get()
    list_end = [l for l in list_ren if leibie in l]
    # print(list_end)
    for i in list_end:
        chaxun(path+'\\'+i)


button = Button(tk, text="点击查询", font=8,command=submit, default='active')
button.grid(row=4, column=1)

#主事件循环
mainloop()




        
