from tkinter import *
win=Tk()
win.geometry('500x116')
win.title('学生登录信息')
#提交按钮事件
def mClick():
    txt=txt2.get()
    if(txt == '123'):
        txt3.set("登录成功")
#创建几个组件元素
lab1=Label(win,text="姓名：",font=('华文新魏','16'))
lab2=Label(win,text="学号：",font=('华文新魏','16'))
txt1=StringVar()
txt2=StringVar()
txt3=StringVar()
txt3.set("请输入姓名和学号")
entry1=Entry(win,textvariable=txt1,width=16,font=('宋体','16'))
entry2=Entry(win,textvariable=txt2,width=16,font=('宋体','16'),show='*')
button=Button(win,text='提交',command=mClick,font=('宋体','16'))
lab3=Label(win,textvariable=txt3,relief='ridge',width=30,font=('华文新魏','16'))
# a=["男生","女生"]
v=IntVar()
ra1=Radiobutton(win,text='男生',variable=v,value=1)
ra2=Radiobutton(win,text='女生',variable=v,value=2)

#布局设置
lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
lab3.grid(row=3,column=0,columnspan=2)
button.grid(row=3,column=2)
ra1.grid(row=2,column=0)
ra2.grid(row=2,column=1)
win.mainloop()