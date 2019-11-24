import tkinter
import sqlite3
from tkinter import ttk  # 导入内部包

def showMessage():
   # li = ['9787115480354', 'SSM轻量级框架应用实战', '2018-05-01', '66.8', '4']
    conn = sqlite3.connect("c:/books.db")
    cur = conn.cursor()
    sqlstr = "select * from  books"
    s = cur.execute(sqlstr)

    root = tkinter.Tk()
    root.title('显示书目信息')
    tree = ttk.Treeview(root, columns=['1', '2', '3', '4'], show='headings')
    tree.column('1', width=150, anchor='center')
    tree.column('2', width=200, anchor='center')
    tree.column('3', width=100, anchor='center')
    tree.column('4', width=100, anchor='center')
   # tree.column('5', width=100, anchor='center')
    tree.heading('1', text='书号')
    tree.heading('2', text='书名')
    tree.heading('3', text='出版时间')
    tree.heading('4', text='价格')
    #tree.heading('5', text='库存')
   #tree.insert('', 'end', values=li)
    for row in s:
        tree.insert('', 'end', values=row)
    tree.grid()
    root.mainloop()

def showStock():
    conn = sqlite3.connect("c:/books.db")
    cur = conn.cursor()
    sqlstr = "select * from  books"
    s = cur.execute(sqlstr)

    root = tkinter.Tk()
    root.title('显示书目信息')
    tree = ttk.Treeview(root, columns=['1', '2', '3'], show='headings')
    tree.column('1', width=150, anchor='center')
    tree.column('2', width=200, anchor='center')
    tree.column('3', width=100, anchor='center')
    tree.heading('1', text='书号')
    tree.heading('2', text='书名')
    tree.heading('3', text='库存')

    for row in s:
        li=[row[0],row[1],row[4]]
        tree.insert('', 'end', values=li)
    tree.grid()
    root.mainloop()