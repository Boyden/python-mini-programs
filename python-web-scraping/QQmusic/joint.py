import sqlite3
db = ["totalsongsinfo0.db","totalsongsinfo1.db","totalsongsinfo2.db","totalsongsinfo3.db","totalsongsinfo4.db"]
conn1 = sqlite3.connect("total.db")

cursor1 = conn1.cursor()

cursor1.execute('create table if not exists songs (id long primary key, name varchar(30), song_url tinytext, lyric mediumtext, genre varchar(20))')
cursor1.execute('create table if not exists errorsongs (id long primary key, name varchar(30), song_url tinytext, lyric mediumtext, genre varchar(20))')
for i in range(5):
    conn2 = sqlite3.connect(db[i])
    cursor2 = conn2.cursor()
    sql2 = '''select * from songs'''
    cursor2.execute(sql2)
    total = cursor2.fetchall()
    for index,elem in enumerate(total):
        sql = '''insert OR IGNORE into songs (id, name,song_url,lyric,genre) values (?,?,?,?,?)'''
        cursor1.execute(sql, elem)
    cursor2.close()
    conn2.close()
conn1.commit()
conn1.close()