import sqlite3

conn1 = sqlite3.connect("final.db")
cursor1 = conn1.cursor()
'''
cursor1.execute('create table if not exists songs (id long primary key, name varchar(30), song_url tinytext, lyric mediumtext, genre varchar(20))')

conn2 = sqlite3.connect("total.db")
cursor2 = conn2.cursor()
cursor2.execute("select * from songs")
TotalSongs = cursor2.fetchall()
for index,elem in enumerate(TotalSongs):
	sql = 'insert OR IGNORE into songs (id, name,song_url,lyric,genre) values (?,?,?,?,?)'
	cursor1.execute(sql,elem)
conn1.commit()
conn1.close()
conn2.close()
'''
cursor1.execute('select * from songs where id is ?',['1437744'])
result = cursor1.fetchall()
print(result)
conn1.close()
