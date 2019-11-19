import json, time, requests
from lxml import etree
href = "https://www.instagram.com/komatsu7stagram/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }

html = requests.get(href, headers=headers)
html = etree.HTML(html.text)
script = html.cssselect("script")
js = script[1].text[len("window._sharedData = "):-1]
js = json.loads(js)
next_var = js["entry_data"]["ProfilePage"][0]["user"]["media"]["page_info"]["end_cursor"]
#next_var = "AQBspyhknVD326x2WxIl5s1Tk5FEQc2heK-e04smbT3XpMvhRogErWug4KE7ug30c5hKKwoS1uav7xgawVbSVTm3fjl1KLtIgOQhjU0sMWCRIg"
base_url = "https://www.instagram.com/graphql/query/?query_id=17888483320059182&variables=%7B%22id%22%3A%22685281537%22%2C%22first%22%3A12%2C%22after%22%3A%22"
next_url = base_url + next_var + "%22%7D"

class Ins():
    """docstring for """
    def __init__(self, href, pre_url):
        self.cur_url = href
        self.pre_url = pre_url

ins = Ins(next_url, href)
#https://www.instagram.com/graphql/query/?query_id=17888483320059182&variables=%7B%22id%22%3A%22685281537%22%2C%22first%22%3A12%2C%22after%22%3A%22AQDyo7kK8c9XGKqyvVmIcx56m5B_aJZ_k_0P3gyD0CyhyRDDuRNOY6jMZ7NJ14B_-tYNaVqeCiWEZKhQFbJ5wzVBOJTbdwccTjQ_-ZnZbKAhbQ%22%7D
while True:
    js = requests.get(ins.cur_url, headers=headers)
    data = json.loads(js.text)
    try:
        info = data['data']['user']['edge_owner_to_timeline_media']
        arr = info['edges']
        next_info = info['page_info']
    except:
        print("Some errors occur, using previous instead!")
        time.sleep(2)
        ins.cur_url = ins.pre_url
        continue
    
    with open("ins" + href[len("https://www.instagram.com/"):-1] + ".txt", "at") as f:
        for i in range(len(arr)):
            f.write(arr[i]['node']['display_url'] + "\n")
    if next_info['has_next_page'] == True:
        print(next_info['end_cursor'])
        ins.pre_url = ins.cur_url
        ins.cur_url = base_url + next_info['end_cursor'] + "%22%7D"
    else:
        print("All links already written in file!")
        break

