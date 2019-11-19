import urllib, re, datetime, random, json, os, csv, time
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from lxml import etree

def getnextURL(html):
    li = html.cssselect(".paginator .next a")
    if li:
        li = "https://book.douban.com" + li[0].get("href")
        print("Got The Link:" + li+"\n")
        li = urllib.parse.quote(li, safe="/:?=&")
        return li
    else:
        return None

def DealData(url):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }
    )
    print("Start crawling the url:" + url + "\n")

    try:
        print("Getting The Data!\n")
        html = urlopen(req)
    except:
        print("SomeThing Wrong!")
        print("link:" + url + "\n")
        return None

    data = html.read()
    data = data.decode("utf-8", "ignore")
    html = etree.HTML(data)
    article = html.cssselect(".article .subject-list .info")

    for art in article:
        rate = art.cssselect(".rating_nums")
        if rate:
            rate = rate[0].text
            if float(rate) >= 8.0:
                print("Parsing The Data\n")
                GetData(art, rate)

    link = getnextURL(html)
    if link:
        time.sleep(2)
        DealData(link)
    else:
        print("Done\n")


def prettify(stri):
    stri = stri.replace("\n", " ").replace("/", " ")
    stri = re.sub("(\b|)\s+(\b|)", " ", stri)
    return stri

def GetData(art, rate):
    href = "None"
    title = "None"
    artors = "None"
    description = "None"
    rate = "rate:" + rate + "\r\n"

    if art.cssselect("a"):
        href = art.cssselect("a")[0].get("href")
        href = "href:" + href + '\r\n'

    if art.cssselect("a"):
        title = art.cssselect("a")[0].xpath("string()")
        title = prettify(title)
        title = "title:" + title + "\r\n"

    if art.cssselect(".pub"):
        artors = art.cssselect(".pub")[0].xpath("string()")
        artors = prettify(artors)
        artors = "authors:" + artors + "\r\n"

    if art.cssselect("p"):
        description = art.cssselect("p")[0].text
        description = "description:" + description + "\r\n\r\n"

    href = href.encode("utf-8")
    title = title.encode("utf-8")
    artors = artors.encode("utf-8")
    rate = rate.encode("utf-8")
    description = description.encode("utf-8")

    file = open("book.txt", "ab")
    file.write(href)
    file.write(title)
    file.write(artors)
    file.write(rate)
    file.write(description)
    file.close()



DealData("https://book.douban.com/tag/%E5%8E%86%E5%8F%B2")
