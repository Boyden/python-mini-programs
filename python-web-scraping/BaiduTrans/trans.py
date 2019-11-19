import requests, json, sys

text = sys.argv[1]
url = "http://fanyi.baidu.com/v2transapi"

headers = {
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
               "accept-language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
          }
params = {
          "from":"en",
          "to":"zh",
          "query":text,
          "simple_means_flag":"3"
    
}

def detectLan(text):
    url = "http://fanyi.baidu.com/langdetect"
    params = {
               "query":text[:50]
    }
    req = requests.post(url, headers=headers, params=params)
    data = json.loads(req.text)
    return data['lan']

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

req = requests.post(url, headers=headers, params=params)

data = json.loads(req.text)

trans = data["trans_result"]["data"][0]["dst"]
print(trans)
