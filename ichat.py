import itchat, requests, json
from itchat.content import *
from lxml import etree

binglen = 12

headers = {
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
               "accept-language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
          }
def detectLan(text):
    url = "http://fanyi.baidu.com/langdetect"
    params = {
               "query":text[:50]
    }
    req = requests.post(url, headers=headers, params=params)
    data = json.loads(req.text)
    return data['lan']


@itchat.msg_register([TEXT, PICTURE])
def text_reply(msg):
    global glo
    if msg['Type'] == 'Text':
        text = msg['Text']
        print(msg['Text'])
        req = requests.get("https://www.bing.com/dict/search?q=" + text, headers=headers)
        html = req.text
        document = etree.HTML(html)
        word = document.cssselect("meta[name='description']")[0].get("content")
        if len(word) == 2:
            lan = detectLan(text)
            if lan == 'zh':
                params = {
                            "from":"zh",
                            "to":"en",
                            "query":text,
                            "simple_means_flag":"3"
    
                }
            else:
                params = {
                            "from":lan,
                            "to":"zh",
                            "query":text,
                            "simple_means_flag":"3"
    
                         }
            req = requests.post("http://fanyi.baidu.com/v2transapi", headers=headers, params=params)
            data = json.loads(req.text)
            try:
                trans = data["trans_result"]["data"][0]["dst"]
                s = trans
            except:
                s = "No translation!"
        else:
            word = word[binglen+len(text):]
            word = word.split((b"\xef\xbc\x9b ").decode("utf-8"))
            word.pop()
            wor = word[0].split((b"\xef\xbc\x8c ").decode("utf-8"))
            wor = "\n".join(wor)
            word = "\n".join(word[1:])
            s = text + ":\n" + wor + "\n" + word
    elif msg['Type'] == 'Picture':
        print(msg)
        print("\n")
        text = "Picture:" + msg['FileName'] + ""
        xml = msg.get("Content")
        xml = etree.XML(xml)
        img_url = xml.cssselect("emoji")[0].get("cdnurl")
        if img_url == None:
            s = text
        else:
            s = text + "\nUrl:" + img_url
    friend = itchat.search_friends(userName=msg['FromUserName'])
    friend = friend.get("NickName")
    print(s)
    print("\n")
    itchat.send(s, toUserName=msg['FromUserName'])

itchat.auto_login(hotReload=True, enableCmdQR=True)
itchat.run()

#@eb2d8569667266b627785e90123836a9a042928f6b6839d3cdaad1d170e0dc98
'''
req = requests.get("https://www.bing.com/dict/search?q=" + text, headers=headers)
html = req.text
document = etree.HTML(html)
word = document.cssselect("meta[name='description']")[0].get("content")
if len(word) == 2:
    s = words[i] + ":null\n"
word = word[binglen:]
word = word.split((b"\xef\xbc\x9b ").decode("utf-8"))
word.pop()
wor = word[0].split((b"\xef\xbc\x8c ").decode("utf-8"))
wor = "\n".join(wor)
word = "\n".join(word[1:])
s = words[i] + ":\n" + wor + "\n" + word + "\n\n"
'''