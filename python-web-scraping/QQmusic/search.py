import sqlite3

conn1 = sqlite3.connect("total.db")
cursor1 = conn1.cursor()
sql='select count(*) from songs'
cursor1.execute(sql)
num = cursor1.fetchone()
print(num)
conn1.close()
'''
db = ["totalsongsinfo0.db","totalsongsinfo1.db","totalsongsinfo2.db","totalsongsinfo3.db","totalsongsinfo4.db"]
for i in range(4):
    conn2 = sqlite3.connect(db[i])
    cursor2 = conn2.cursor()
    sql2 = select count(*) from songs'
    cursor2.execute(sql2)
    total = cursor2.fetchall()
    for index,elem in enumerate(total):
        print(elem)
    cursor2.close()
    conn2.close()
'''