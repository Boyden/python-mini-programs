import requests, re, time, os
from lxml import etree
from PIL import Image

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

def downloader(url, filename):
    req = requests.get(url, headers)
    with open(filename, "wb") as f:
        f.write(req.content)

def get_url(s):
    links = s.split(";")
    pattern = re.compile(r"https\:\S+\.png")
    for li in links:
        if li.find("background-image") != -1:
            return pattern.findall(li)[0]

def de_alpha_channel(path):
    im = Image.open(path)
    im = im.convert("RGB")
    (row, col) = im.size
    chanel = [im.split()[i] for i in range(3)]
    for k in range(3):
        for x in range(row):
            for y in range(col):
                if chanel[k].getpixel((x, y)) == 0:
                    chanel[k].putpixel((x, y), 255)
    im = Image.merge("RGB", tuple(chanel))
    im.save(path)

def de_trans(path):
    im = Image.open(path)
    [row, col] = im.size
    im = im.convert("RGBA")
    white_im = Image.new(im.mode, im.size, (255,255,255))
    white_im.paste(im, (0, 0, row, col), im)
    white_im.save(path)

def crawler(url):
    req = requests.get(url, headers)
    doc = etree.HTML(req.text)
    links = doc.cssselect(".mdCMN09Image")

    for i in range(len(links)):
        url = get_url(links[i].get("style"))
        print(url)
        pattern = re.compile(r"\/\d+\/")
        downloader(url, "C:\\Users\\acer\\Desktop\\line\\" + pattern.findall(url)[0][1:-1] + ".png")
        print("Downloaded successfully!\n")
        time.sleep(2)

with open("C:\\Users\\acer\\Desktop\\link.txt", "rt") as f:
    url = f.read().split("\n")

for index, value in enumerate(url):
    crawler(value)
    time.sleep(10)

os.chdir("C:\\Users\\acer\\Desktop\\yating")
sticks = os.listdir()

for val in sticks:
    de_trans(os.getcwd() + "\\" + val)
    print(f"convert {val}!")
