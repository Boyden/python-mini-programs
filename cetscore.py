import requests
from lxml import etree
from pprint import pprint

num = input('Your num:')
name = input('Your name:')

url = 'https://www.chsi.com.cn/cet/query'

headers = {
    'Host': "www.chsi.com.cn",
    'Referer': 'https://www.chsi.com.cn/cet/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}

params = {
    'zkzh': num,
    'xm': name
}

req = requests.get(url, headers=headers, params=params)
html = etree.HTML(req.text)

error = html.cssselect('.error')
if len(error) == 0:
    scores = html.cssselect('.cetTable td span')[0].text.strip()
    arr = html.cssselect('.cetTable th+td')
    score1 = arr[5].text.strip()
    score2 = arr[6].text.strip()
    score3 =arr[7].text.strip()

    content = {
        'total scores':scores,
        'listening':score1,
        'reading':score2,
        'writing and translating':score3
    }

    pprint(content)
else:
    print(error[0].text.strip())