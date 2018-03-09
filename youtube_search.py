import requests, sys

from lxml import etree


base_url = "https://www.youtube.com"
query_list = sys.argv[1:]


def getUrl(url, base_url=None, headers='''{"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36"}'''):

    if url.find("http") == -1:
        if url[0] != "/":
            url = base_url + "/" + url
        else:
            url = base_url + url

    print(f"getting {url}")
    print("\n")

    results = []

    req = requests.get(url, headers=headers)

    doc = etree.HTML(req.text)

    li = doc.cssselect(".yt-lockup-content h3 a")
    
    for elem in li:
        title = elem.get("title")
        href = elem.get("href")

        if href.find("http") == -1:
            href = base_url + href
        
        results.append({"title":title, "href":href})
        print(f"title:{title}")
        print(f"href:{href}")
        print("\n")

getUrl("https://www.youtube.com/results?search_query=" + query_list[0], base_url = base_url, headers=None)