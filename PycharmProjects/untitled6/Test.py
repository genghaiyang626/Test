import sqlite3

conn = sqlite3.connect("c:/books.db")
cur = conn.cursor()
sqlstr = "select * from  books"
s = cur.execute(sqlstr)
for row in s:
    print("bookid=",row[0])
    print("bookname=",row[1])
    print("publish=",row[2])
    print("price=",row[3])
    print("bookmatch=",row[4],'\n')

conn.close()
