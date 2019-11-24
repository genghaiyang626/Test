from tkinter import *
from book_system.showMessage import *
#from tkinter.messagebox import showinfo
import 插入书籍信息 as two
import tkinter as tk

# def reply():
#     showinfo(title='新窗口', message='另一个窗口')

def showInfo():
    conn = sqlite3.connect("c:/books.db")
    cur = conn.cursor()
    sqlstr = "select * from  books"
    s = cur.execute(sqlstr)

win=Tk()
win.geometry('500x230')
win.title('图书库存管理系统')

monty=tk.LabelFrame(win,text="图书库存管理系统")
monty.grid(column=0,row=0,padx=10,pady=10)
# aLabel=tk.Label(monty,text="A Label")
# tk.Label(monty,text="请选择一个数字：").grid(column=1,row=0)
tmp=3
btnshow1=Button(monty,text="显示书目信息",font=('华文新魏','16'),command=showMessage).grid(column=1,row=0)
btnshow2=Button(monty,text="显示库存信息",font=('华文新魏','16'),command=showStock).grid(column=1,row=1)
btnadd=Button(monty,text="添加书目信息",font=('华文新魏','16'),command=two.test).grid(column=1,row=2)
btnexit=Button(monty,text="退       出",font=('华文新魏','16'),command=exit).grid(column=1,row=3)
# Entry(monty,textvariable="",width=16,font=('宋体','16')).grid(column=2,row=0)
#btnadd.grid(column=1,row=2)

win.mainloop()