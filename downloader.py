import requests, os, re
from multiprocessing import Pool
from lxml import etree

headers = {"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
filename = "C:/Users/acer/Desktop/nanains.txt"
path = "C:/Users/acer/Desktop/nana/"
all_link = []
failed_link = []

def parse(path, reg = None):

    links = []
    req = requests.get(path, headers=headers)
    html = etree.HTML(req.text)

    li = html.cssselect('a')
    
    if reg == None:
        for i in range(len(li)):
            if li[i].get('href').find('http') == -1:
                links.append(path+li[i].get('href'))
            else:
                links.append(li[i].get('href'))
    else:
        for i in range(len(li)):
            if li[i].get('href').find('http') == -1:
                if re.search(reg, li[i].get('href')) !=None:
                    links.append(path+li[i].get('href'))
            else:
                if re.search(reg, li[i].get('href')) !=None:
                    links.append(li[i].get('href'))

    return links



def downloader(url):
    try:
        data = requests.get(url, headers=headers).content
        file_name = os.path.basename(url)
        with open(path+file_name, "wb") as f:
            f.write(data)
        print(file_name + " downloaded successfully!\n")
    except:
        failed_link.append(url)

def downloaderAll(urls):
    for url in urls:
        downloader(url)

with open(filename, "rt") as f:
    all_link = f.read().split("\n")
    all_link.pop()

if __name__ == '__main__':
    pool = Pool()
    pool.map(downloader, all_link)

    s = '\n'.join(failed_link)
    with open("failed_link.txt", "wt") as f:
        f.write(s)


#https://web.stanford.edu/class/cs231m/lectures/lecture-1-intro.pdf