import urllib, re, datetime, random, json, os, csv
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from lxml import etree

def getURLs(url):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }
    )
    try:
        print("Getting The URLS!\n")
        html = urlopen(req)
    except:
        print("SomeThing Wrong!\n")
        return None
    print("Parsing The URLS!\n")
    data = html.read()
    data = data.decode("utf-8", "ignore")
    html = etree.HTML(data)
    li = html.cssselect(".paginator > a")
    links = [url]
    for link in li:
        links.append(url + link.get("href"))
    print("Got The Links \n")
    print(links)
    return links

def DealData(url):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }
    )

    try:
        print("Getting The Data!\n")
        html = urlopen(req)
    except:
        print("SomeThing Wrong!\n")
        return None

    data = html.read()
    data = data.decode("utf-8", "ignore")
    html = etree.HTML(data)
    article = html.cssselect(".grid_view .item .info")


    for art in article:

        href = "None"
        title = "None"
        artors = "None"
        rate = "None"
        description = "None"

        if art.cssselect("a"):
            href = art.cssselect("a")[0].get("href")
        href = "href:"+href+'\r\n'

        if art.cssselect("a"):
            title = art.cssselect("a")[0].xpath("string()")
        title = prettify(title)
        title = "title:"+title+"\r\n"

        if art.cssselect(".bd p"):
            artors = art.cssselect(".bd p")[0].xpath("string()")
            artors = prettify(artors)
        artors = "actors:"+artors+"\r\n"

        if art.cssselect(".star .rating_num"):
            rate = art.cssselect(".star .rating_num")[0].text
        rate = "rate:"+rate+"\r\n"

        if art.cssselect(".inq"):
            description = art.cssselect(".inq")[0].text
        description = "description:"+description+"\r\n\r\n"

        href = href.encode("utf-8")
        title = title.encode("utf-8")
        artors = artors.encode("utf-8")
        rate = rate.encode("utf-8")
        description = description.encode("utf-8")

        file = open("movie.txt", "ab")
        file.write(href)
        file.write(title)
        file.write(artors)
        file.write(rate)
        file.write(description)
        file.close()

    print("Done!\n")

def spider(url):
    links = getURLs(url)
    for link in links:
        DealData(link)

def prettify(stri):
    stri = stri.replace("\n", " ").replace("/", " ")
    stri = re.sub("(\b|)\s+(\b|)", " ", stri)
    return stri


spider("https://movie.douban.com/top250")
