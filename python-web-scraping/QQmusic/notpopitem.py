import sqlite3

conn1 = sqlite3.connect("total.db")
cursor1 = conn1.cursor()

sql = "select lyric,song_url from songs where genre <> 'Pop'"
#sql = "select genre from songs group by genre"
cursor1.execute(sql)
results = cursor1.fetchall()
conn1.close()


conn1 = sqlite3.connect("noPOPmusicitem.db")

cursor1 = conn1.cursor()
cursor1.execute('create table if not exists songs (id long primary key, item varchar(30))')
cursor1.close()

conn1.commit()
conn1.close()


itemset = set({})
i = 0
for index,elem in enumerate(results):
    
    if elem[0] == None :
        continue
    arrelem = elem[0].split('\n')
    if len(arrelem)<5:

        print("This is a very short song.  index:", index, "  url: ",elem[1])

        continue
    print("index:",index,"  url: ",elem[1])
    for item in arrelem:
        if '：' in item:
            val = item.split('：')[0]
            if val not in itemset:
                itemset.add(val)
                conn2 = sqlite3.connect('noPOPmusicitem.db')
                cursor2 = conn2.cursor()
                sql2 = '''insert into songs (id, item) values (?, ?)'''
                para2 = [i, val]
                cursor2.execute(sql2,para2)
                conn2.commit()
                conn2.close()
                i = i + 1



'''
sql = "select count(*) from songs"
cursor1.execute(sql)
num = cursor1.fetchone()
print("total:{}".format(num))
for index,elem in enumerate(genre):
    sql = "select count(*) from songs where genre=?"
    cursor1.execute(sql,elem)
    num = cursor1.fetchone()
    print('genre:{}\tnum:{}'.format(elem, num))
'''