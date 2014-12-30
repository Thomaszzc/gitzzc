#-*- encoding=UTF-8 -*-

from Tkinter import *
from ttk import *
import os  

def get_sub_path(path):
    if os.path.isdir(path):
        for sub_path in os.listdir(path):
            get_sub_path(path+'\\'+sub_path)
    else:
        if os.path.splitext(path)[1].find('java')>0:
            count_line(path)

def count_line(path):
    count_p=0
    global count
    with open(path,'r')as f:
        while f.readline():
            count_p+=1;
    temp_path=os.path.split(path)[1]
    temp=temp_path+' 共 '+str(count_p)+' 行\r\n'
    app.text.insert(1.0,temp)
    print path,'共',count_p,'行'
    count+=count_p

class App:
    def __init__(self, master):
        #构造函数里传入一个父组件(master),创建一个Frame组件并显示
        frame = Frame(master)
        frame.pack()
        #创建两个button，并作为frame的一部分
        self.path=Entry(frame)
        self.path['width']=80
        self.path.pack()
        self.count = Button(frame, text="统计", command=self.count)
        self.count.pack()
        self.text_scroll_y = Scrollbar(frame, orient=VERTICAL)  #文本框-竖向滚动条
        self.text =Text(frame, yscrollcommand=self.text_scroll_y.set,wrap='none')
        self.text_scroll_y.config(command=self.text.yview)
        self.text_scroll_y.pack(fill="y", expand=0, side=RIGHT, anchor=N)
        self.text.pack()
        global val
        self.label=Label(frame,textvariable=var)
        
        self.label.pack()
    def count(self):
        global var
        get_sub_path(self.path.get())
        var.set('该文件下共有：'+str(count)+'行')
        
    
win = Tk()
win.title('代码行数计数器')    #定义窗体标题
win.geometry('600x400')     #定义窗体的大小，是400X200像素
var=StringVar()
app = App(win)

count=0;


win.mainloop()
print count
