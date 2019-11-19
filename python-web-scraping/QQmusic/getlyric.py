import requests, lxml, html, re, json, sqlite3, time

def getGenre_and_SongID(url):

    pattern = r'info.?:.?({.*})'
    headers = {
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
              }
    for index in range(10):
        try:
            req = requests.get(url, headers=headers)
            time.sleep(1)
            break
        except:
            print('\ntry url:{} again\n'.format(url))

    if index == 9:
        return None   
    if req.status_code == 200:
        if req.text == None:
            print('\nwrong: {}\n'.format(url))
            return None
        info = re.search(pattern, req.text).group(1)
        info = json.loads(info)
        try:
            genre = info['genre']['content'][0]['value']
        except:
            genre = None
        
        pattern_id = r'songid=\d+'
        song_id = re.findall(pattern_id, req.text)[0]
        song_id = int(song_id.split('=')[-1])

        return (song_id, genre)

def getLyric(lyricurl, url, params=None):
    headers = {
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'referer':url
              }
    for index in range(10):
        try:
            req = requests.get(lyricurl, headers=headers, params=params)
            time.sleep(1)
            break
        except:
            print('\nget lyric:{} again\n'.format(url))
    if index == 9:
        return None
    if req.status_code == 200:
        content = req.text[7:-1]
        content = json.loads(content)
        try:
            lyric = content['lyric']
            lyric = lyricPretty(lyric)
        except:
            lyric = None
        return lyric

def lyricPretty(lyric):
    lyric = html.unescape(lyric)
    pattern = r'\[[^\[\]]*\]'
    lyric = re.sub(pattern, '', lyric)
    lyric = lyric.strip()
    return lyric
i=0
LYRICURL = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric.fcg'
conn = sqlite3.connect("totalsongsinfo.db")
cursor = conn.cursor()
cursor.execute('create table if not exists songs (id long primary key, name varchar(30), song_url tinytext, lyric mediumtext, genre varchar(20))')
cursor.execute('create table if not exists errorsongs (id long , name varchar(30) primary key, song_url tinytext, lyric mediumtext, genre varchar(20))')
cursor.close()
conn.commit()
conn.close()

with open("songinfo.json", 'r') as f:
    s = f.read()
data= json.loads(s)

songs = []

tmp = data[2785:]
for index, elem in enumerate(tmp):
    
    name = elem["name"]
    url = elem["url"]

    print("window:----the {}th URL:{}\n".format(index, url))
    info = getGenre_and_SongID(url)
    if info!=None:
        params = {
                "nobase64": 1,
                "musicid": info[0],
                "callback": "jsonp1",
                "g_tk": 5381,
                "jsonpCallback": "jsonp1",
                "loginUin": 0,
                "hostUin": 0,
                "format": "jsonp",
                "inCharset": "utf8",
                "outCharset": "utf-8",
                "notice": 0,
                "platform": "yqq",
                "needNewCode": 0
             }

        lyric = getLyric(LYRICURL, url, params=params)


        song = {
                'song_id':info[0],
                'name':name,
                'song_url':url,
                'lyric':lyric,
                'genre':info[1]
            }
        conn = sqlite3.connect("totalsongsinfo.db")
        cursor = conn.cursor()
        sql = '''insert OR IGNORE into songs (id, name,song_url,lyric,genre) values (?,?,?,?,?)'''
        para = (song["song_id"],song["name"],song["song_url"],song["lyric"],song["genre"])
        cursor.execute(sql, para)
        cursor.close()
        conn.commit()
        conn.close()
        #songs.append(song)
    else:
        conn = sqlite3.connect("totalsongsinfo.db")
        cursor = conn.cursor()
        sql = '''insert OR IGNORE into songs (id, name,song_url,lyric,genre) values (?,?,?,?,?)'''
        para = (None,name,url,None,None)
        cursor.execute(sql, para)
        cursor.close()
        conn.commit()
        conn.close()
