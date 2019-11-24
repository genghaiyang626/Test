from tkinter import *
import tkinter as tk
import sqlite3

def test():
    def mClick():
        sql="insert into books(bookid,bookname,publish,price,bookmatch) values('"+entry1.get()+"','"+entry2.get()+"','"+entry3.get()+"',"+entry4.get()+","+entry5.get()+")"
        print(sql)
        conn = sqlite3.connect("c:/books.db")
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Records created successfully")
        conn.close()



    win = Tk()
    win.geometry('500x230')
    win.title('图书库存管理系统')
    monty = tk.LabelFrame(win, text="图书库存管理系统")
    monty.grid(column=0, row=0, padx=10, pady=10)
    lab1 = Label(monty, text="书号：", font=('华文新魏', '16')).grid(row=1, column=0)
    lab2 = Label(monty, text="书名：", font=('华文新魏', '16')).grid(row=2, column=0)
    lab3 = Label(monty, text="出版时间：", font=('华文新魏', '16')).grid(row=3, column=0)
    lab4 = Label(monty, text="价格：", font=('华文新魏', '16')).grid(row=4, column=0)
    lab5 = Label(monty, text="库存：", font=('华文新魏', '16')).grid(row=5, column=0)
    txt1 = StringVar()
    txt2 = StringVar()
    txt3 = StringVar()
    txt4 = StringVar()
    txt5 = StringVar()

    entry1 = Entry(monty, textvariable=txt1, width=16, font=('宋体', '16'))
    entry2 = Entry(monty, textvariable=txt2, width=16, font=('宋体', '16'))
    entry3 = Entry(monty, textvariable=txt3, width=16, font=('宋体', '16'))
    entry4 = Entry(monty, textvariable=txt4, width=16, font=('宋体', '16'))
    entry5 = Entry(monty, textvariable=txt5, width=16, font=('宋体', '16'))
    entry1.grid(row=1, column=1)
    entry2.grid(row=2, column=1)
    entry3.grid(row=3, column=1)
    entry4.grid(row=4, column=1)
    entry5.grid(row=5, column=1)

    button = Button(monty, text='提交', font=('宋体', '16'),command=mClick).grid(row=6, column=2)
    lab6 = Label(monty, text="添加图书信息",relief='ridge',width=30, font=('华文新魏', '16')).grid(row=6, column=0,columnspan=2)
    win.mainloop()













