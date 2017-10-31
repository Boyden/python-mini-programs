import requests, os
from multiprocessing import Pool

headers = {"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
filename = "C:/Users/acer/Desktop/nanains.txt"
path = "C:/Users/acer/Desktop/nana/"
all_link = []
failed_link = []
def downloader(url):
    try:
        data = requests.get(url, headers=headers).content
        img_name = os.path.basename(url)
        with open(path+img_name, "wb") as f:
            f.write(data)
        print(img_name + " downloaded successfully!\n")
    except:
        failed_link.append(url)

with open(filename, "rt") as f:
    all_link = f.read().split("\n")
    all_link.pop()

if __name__ == '__main__':
    pool = Pool()
    pool.map(downloader, all_link)

    s = '\n'.join(failed_link)
    with open("failed_link.txt", "wt") as f:
        f.write(s)
