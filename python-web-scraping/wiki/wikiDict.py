import requests
from lxml import etree

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

start_url = "https://en.wikipedia.org/wiki/Brain"
hostname = "https://en.wikipedia.org"

with open("C:\\Users\\acer\\Desktop\\wiki\\wikiLink.dict", "rt") as f:
    list_url = f.read().split("\n")

with open("C:\\Users\\acer\\Desktop\\wiki\\wiki.dict", "rb") as f:
    dict_list = f.read().decode("utf-8").split("\n")

with open("C:\\Users\\acer\\Desktop\\wiki\\wikiNone.dict", "rb") as f:
    none_list = f.read().decode("utf-8").split("\n")

list_url.remove("")
dict_list.remove("")
none_list.remove("")

url_set = set(list_url)
dict_set = set(dict_list)
none_set = set(none_list)

url_set.add(start_url)



def getDict(url, headers):
    print("Get:" + url + "\n")
    html = requests.get(url, headers = headers).text
    html = etree.HTML(html)
    cur_eng = html.cssselect("title")[0].text[:-12]
    temp_tag = html.cssselect("#p-lang .body .interwiki-zh a")
    if temp_tag != []:
        cur_chi = temp_tag[0].attrib["title"][:-10]
    else:
        cur_chi = " "
    s = cur_eng + ":" + cur_chi
    if cur_chi == " " and cur_eng not in none_set:
        none_set.add(cur_eng)
        with open("C:\\Users\\acer\\Desktop\\wiki\\wikiNone.dict", "ab") as f:
            f.write((cur_eng + "\n").encode("utf-8"))
    elif s not in dict_set and cur_chi != " ":
        dict_set.add(s)
        with open("C:\\Users\\acer\\Desktop\\wiki\\wiki.dict", "ab") as f:
            f.write((s+"\n").encode("utf-8"))
        print("Write: " + s + " successfully!\n")

    next_urls = html.cssselect("#mw-content-text .mw-parser-output > p a")
    for next_url in next_urls:
        try:
            rel_url = next_url.attrib["href"]
        except:
            continue
        if rel_url[1:5] == "wiki" and "https://en.wikipedia.org" + rel_url not in url_set:
            url_set.add("https://en.wikipedia.org" + rel_url)

            with open("C:\\Users\\acer\\Desktop\\wiki\\wikiLink.dict", "ab") as f:
                f.write(("https://en.wikipedia.org" + rel_url + "\n").encode("utf-8"))
            getDict("https://en.wikipedia.org" + rel_url, headers)
if list_url == []:
    with open("C:\\Users\\acer\\Desktop\\wiki\\wikiLink.dict", "ab") as f:
        f.write((start_url+"\n").encode("utf-8"))
    getDict(start_url, headers)
else:
    getDict(list_url[-1], headers)