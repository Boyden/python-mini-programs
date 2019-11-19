import math, requests, json, time
from PIL import Image
from random import random
from io import BytesIO
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }

def getQR_url():
    t = "ptqrshow"
    e = "https://ssl."
    i = e + "ptlogin2.qq.com" + "/" +  t + "?"
    i += "appid=501004106&e=2&l=M&s=3&d=72&v=4&t=" + str(random())
    i += "&daid=164&pt_3rd_aid=0"
    return i


def hash2(uin,ptvfwebqq):
    
    ptb = [0 for i in range(4)]
    for i in range(len(ptvfwebqq)):
        ptbIndex = i % 4
        ptb[ptbIndex] ^= ord(ptvfwebqq[i])

    salt = ["EC", "OK"]
    uinByte = [None for i in range(4)]
    uinByte[0] = (((int(uin) >> 24) & 0xFF) ^ ord(salt[0][0]))
    uinByte[1] = (((int(uin) >> 16) & 0xFF) ^ ord(salt[0][1]))
    uinByte[2] = (((int(uin) >> 8) & 0xFF) ^ ord(salt[1][0]))
    uinByte[3] = ((int(uin) & 0xFF) ^ ord(salt[1][1]))
    result = [None for i in range(8)]
    for i in range(8):
        if (i % 2 == 0):
            result[i] = ptb[i >> 1]
        else:
            result[i] = uinByte[i >> 1]
    
    return byte2hex(result)


def hash33(t):
    e = 0
    for i in range(len(t)):
        e += (e << 5) + ord(t[i])
    return 2147483647 & e

    

def byte2hex(bytes):
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    buf = ""

    for i in range(len(bytes)):
       buf += hex[(bytes[i] >> 4) & 0xF]
       buf += hex[bytes[i] & 0xF]
       
    return buf

#get the value of "pgv_pvi"=>"" and "pgv_si"=>"s"
def r(c=""):
    return (c or "") + str(int(round(2147483647 * (random() or .5)) * int(time.time() * 1000) % 1e10))


#get the QR Code
url = getQR_url()
s = requests.Session()
req = s.get(url, headers=headers)
img = Image.open(BytesIO(req.content))
img.show()

#set the cookie
url = "https://xui.ptlogin2.qq.com/cgi-bin/xlogin"
params = {
    "daid": "164",
    "target": "self",
    "style": "40",
    "pt_disable_pwd": "1",
    "mibao_css": "m_webqq",
    "appid": "501004106",
    "enable_qlogin": "0",
    "no_verifyimg": "1",
    "s_url": "http://w.qq.com/proxy.html",
    "f_url": "loginerroralert",
    "strong_login": "1",
    "login_state": "10",
    "t": "201324001"
}
s.get(url, headers=headers, params=params)
cookiejar = requests.utils.dict_from_cookiejar(s.cookies)

#add "pgv_pvi" and "pgv_si" cookies to session s
s.cookies.set("pgv_pvi", r())
s.cookies.set("pgv_si", r("s"))


#get the script's file of the login info
cookiejar = requests.utils.dict_from_cookiejar(s.cookies)
url = "https://ssl.ptlogin2.qq.com/ptqrlogin"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    "Referer": "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?daid=164&target=self&style=40&pt_disable_pwd=1&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001"
    }
params = {
    "u1": "http://w.qq.com/proxy.html",
    "ptqrtoken": hash33(cookiejar["qrsig"]),
    "ptredirect": 0,
    "h": 1,
    "t": 1,
    "g": 1,
    "from_ui": 1,
    "ptlang": 2052,
    "action": "0-0-" + str(1000*time.time()),
    "js_ver": 10232,
    "js_type": 1,
    "login_sig": cookiejar["pt_login_sig"],
    "pt_uistyle": 40,
    "aid": 501004106,
    "daid": 164,
    "mibao_css": "m_webqq"
}
req = s.get(url, headers=headers, params=params)
data = req.text
data = data.split(",")
data = data[2]
data = data.split("?")[1].split("&")
for elem in data:
    if elem.split("=")[0] == "ptsigx":
        data = elem.split("=")[1]
        break

#check signature
cookiejar = requests.utils.dict_from_cookiejar(s.cookies)
uin = "787359142"
url = "http://ptlogin2.web2.qq.com/check_sig"
params = {
    "pttype": 1,
    "uin": uin,
    "service": "ptqrlogin",
    "nodirect": 0,
    "ptsigx": data,
    "s_url": "http://w.qq.com/proxy.html",
    "f_url":"",
    "ptlang": 2052,
    "ptredirect": 100,
    "aid": 501004106,
    "daid": 164,
    "j_later": 0,
    "low_login_hour": 0,
    "regmaster": 0,
    "pt_login_type": 3,
    "pt_aid": 0,
    "pt_aaid": 16,
    "pt_light": 0,
    "pt_3rd_aid": 0
}
req = s.get(url, headers=headers, params=params, allow_redirects=False)


cookiejar = requests.utils.dict_from_cookiejar(s.cookies)
url = "http://s.web2.qq.com/api/getvfwebqq"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    "Referer": "http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1"
}
params = {
    "ptwebqq":"",
    "clientid": 53999199,
    "psessionid":"",
    "t": int(1000*time.time())
}
req = s.get(url, headers=headers, params=params)
data = json.loads(req.text)

vfwebqq = data["result"]["vfwebqq"]
uin = "787359142"
url = "http://s.web2.qq.com/api/get_user_friends2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    "Referer":"http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1",
    "Origin":"http://s.web2.qq.com"
}
params = {
    "vfwebqq":vfwebqq,
    "hash":hash2(uin, "")
}
r = {}
r["r"] = json.dumps(params)
req = s.post(url, headers=headers, data=r)
data = json.loads(req.text)
print(data)

def request(s, url, method, headers=None, params=None, data=None):
    if method == "GET":
        req = s.get(url, headers=headers, params=params)
    elif methid == "POST":
        req = s.post(url, data=data)
    else:
        req = None
    return req
