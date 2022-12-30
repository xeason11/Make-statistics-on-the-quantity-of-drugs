from tkinter import ttk
import pandas as pd
from tkinter import *  # 下拉菜单控件在ttk中
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
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.csv':  # 想要保存的文件格式
                L.append(os.path.join(file))
    return L


# print(file_name(r'G:\2021.12'))

##############窗体#######################################
global path
global a
tk = Tk()
tk.title("统药小程序 ver1.1  developed by.XYL")
tk.geometry("600x700+600+200")
tk.resizable(width=False, height=False)
# 标签控件，显示文本和位图，展示在第一行
Label(tk, text="文档路径：",font=8).grid(row=0, sticky=W)  # 靠右
Label(tk, text="医生姓名：",font=8).grid(row=1, sticky=W)  # 左
Label(tk, text="查询条件：",font=8).grid(row=2, sticky=W)  #
Label(tk, text="药物名称：",font=8).grid(row=3, sticky=W)  #
Label(tk, text="查询结果：",font=8).grid(row=5, sticky=W)  #

cmb_namer=ttk.Combobox(tk,width=46,font=8)
cmb_namer['value']=('点此下拉框选择医生姓名','徐后庆','朱秀','徐蕊',
                    '李庆峰','李明洋','吕强','单凤伟','刘冬冬','许传贤',
                    '刘春生','马洪章','王敏','徐后玲','厉正恩','徐晖延',
                    '权太磊','桑宝营','王海涛')
cmb_namer.current(0)

cmb_fanwei = ttk.Combobox(tk, width=46, font=8)
cmb_fanwei['value'] = ('点此下拉框选择查询条件', '门诊', '住院')
cmb_fanwei.current(0)

cmb_namey=ttk.Combobox(tk,width=46,font=8)
cmb_namey['value']=('点此下拉框选择药物名称','正天胶囊','三九胃泰胶囊','细胞因子测定',
                    '降钙素原检测','超敏C反应蛋白测定','脂蛋白相关磷脂酶A2','通心络胶囊','参松养心胶囊','马来酸左旋氨氯地平片',
                    '速效救心丸','急支糖浆','地奥心血康胶囊','六神丸(水丸)','茶碱缓释片',
                    '血同型半胱氨酸测定','血清胃蛋白酶原I测定','粪便钙卫蛋白检测','血清肌钙蛋白Ⅰ测定（金标法）',
                    '血栓弹力图试验（TEG）','注射用克林霉素磷酸酯（冻干）')
cmb_namey.current(0)
# 输入控件
p = StringVar()  # 文件路径
# r = StringVar()  # 人名
# y = StringVar()  # 药名
path1 = Entry(tk, width=48,font=8,textvariable=p)
path1.grid(row=0, column=1)
# name_ren = Entry(tk,width=48,font=8,textvariable=r)#1.1更新：医生姓名改成下拉框
# name_ren.grid(row=1, column=1)
cmb_namer.grid(row=1,column=1)
cmb_fanwei.grid(row=2, column=1)
# name_yao = Entry(tk, width=48,font=8, textvariable=y)1.1更新，药名换成下拉框
# name_yao.grid(row=3, column=1)
cmb_namey.grid(row=3,column=1)

text_jieguo = Text(tk, width=48, height=27,font=5)
text_jieguo.grid(row=5, column=1)


###############查询统计指定药物数量#############
def chaxun(path):
    global a
    duiying_num = []
    with open(path) as file:
        # 取出药名和数量列
        data1 = pd.read_csv(file, usecols=[3, 6])
        data = data1.iloc[1:]
    # print(data)
    # 把药名转为列表
    name = list(data.iloc[:, 0])
    # print(name)
    # 数量转化为列表
    num = list(data.iloc[:, 1])
    # print(num)
    n = cmb_namer.get()
    a = cmb_namey.get()
    lei = cmb_fanwei.get()
    list1 = [i for i, j in enumerate(name) if j == a]  # 某一药品行索引
    for i in list1:
        duiying_num.append(float(num[i]))
    text_jieguo.insert('insert', n + "在" + lei + a + "的数量是: " + str(sum(duiying_num)) + "\n")


##############核心函数，实现前端输入获取和后端对文件的查询##############
def submit():
    global path
    path = p.get()
    list_biaoge = file_name(path)
    # print(list_biaoge)
    name = cmb_namer.get()
    list_ren = [l for l in list_biaoge if name in l]
    # print(list_ren)
    leibie = cmb_fanwei.get()
    list_end = [l for l in list_ren if leibie in l]
    # print(list_end)
    for i in list_end:
        chaxun(path + '\\' + i)


button = Button(tk, text="点击查询", font=8,command=submit, default='active')
button.grid(row=4, column=1)

# 主事件循环
mainloop()





