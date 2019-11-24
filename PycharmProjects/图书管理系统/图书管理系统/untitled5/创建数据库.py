import sqlite3

conn = sqlite3.connect("c:/books.db")
print("connetion database successfully")

sqlstr = "create table if not exists books (bookid varchar(5) primary key, bookname varchar(10), publish varchar(10),price double ,bookmatch int)"
conn.execute(sqlstr)
print("create table successfully")

cur = conn.cursor()
sqlstr1 = "insert into books(bookid,bookname,publish,price,bookmatch) values('9787517042099','Photoshop入门到创意','2016-04-01',45.0,5)"
cur.execute(sqlstr1)
sqlstr2 = "insert into books(bookid,bookname,publish,price,bookmatch) values('9787115480354','SSM轻量级框架应用实战','2018-05-01',66.8,4)"
cur.execute(sqlstr2)
sqlstr3 = "insert into books(bookid,bookname,publish,price,bookmatch) values('9787517042242','HTML5+CSS3前端技术','2016-04-01',52.0,7)"
cur.execute(sqlstr3)
conn.commit()
print("Records created successfully")

conn.close()

