import sqlite3, re, time

conn1 = sqlite3.connect("total.db")
cursor1 = conn1.cursor()

sql = "select lyric,song_url from songs where genre = 'Pop'"
#sql = "select genre from songs group by genre"
cursor1.execute(sql)
results = cursor1.fetchall()
cursor1.close()
conn1.close()

conn2 = sqlite3.connect("popclean.db")

cursor2 = conn2.cursor()
cursor2.execute('create table if not exists songs (id long primary key, song_url tinytext, lyric mediumtext)')
cursor2.close()

conn2.commit()
conn2.close()


index_id = 0
for index, elem in enumerate(results):
    #Some songs dont have lyric
    #Some songs have '\r\n'
    elem = list(elem)
    if elem[0] == None:
        continue
    elem[0] = elem[0].replace('\r', '')
    elem[0] = elem[0].strip('\n')
    lyric_arr = elem[0].split('\n')

    if len(lyric_arr) < 5:
        #some songs have very short lyric
        print("This is a very short song.  index:", index, "  url: ",elem[1])
        continue
    print("index:",index,"  url: ",elem[1])

    if '词' in lyric_arr[1] and '曲' in lyric_arr[2]:

        lyric_li = elem[0].split('\n\n')[1:]
        lyric = '\n\n'.join(lyric_li)
        if len(lyric) == 0:
            print(lyric_arr)
            continue
        s = re.sub(r'[\n+|\s+]', '', lyric)
        check = re.search(u'[^\u4e00-\u9fa5]', s)

        #check == None, the lyric only contains Chinese
        if check == None:
            conn3 = sqlite3.connect("popclean.db")

            cursor3 = conn3.cursor()
            sql = '''insert into songs (id, song_url, lyric) values (?, ?, ?)'''
            para = [index_id, elem[1], lyric]

            cursor3.execute(sql, para)
            cursor3.close()

            conn3.commit()
            conn3.close()
            index_id = index_id + 1





