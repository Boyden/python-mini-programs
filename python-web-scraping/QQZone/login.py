import requests, time, getpass, requests, re, random

from lxml import etree
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def wait_func(name, t):
    print("please wait:" + name + "\n")
    time.sleep(t)
    return t

def get_all_urls(etreeObj):
    links = []
    for elem in etreeObj:
        if elem.get("src") != None:
            links.append(elem.get("src"))
        else:
            links.append(elem.get("data-src"))
    return links

def downloader(links):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"}
    linkscopy = links.copy()
    for link in links:
        link = link.replace("/m/", "/b/").replace("/psbe?", "/psb?").replace("&rf=photolist&t=5", "&rf=viewer_4").replace("&rf=photolist", "&rf=viewer_4")
        print("Link:" + link + "\n")
        try:
            req = requests.get(link, headers=headers)
        except:
            return linkscopy

        if linkscopy != []:
            linkscopy.remove(linkscopy[0])
        name = get_file_name()
        print("Downloading:" + name + "\n")
        file = open("./pic/" + name, "wb")
        file.write(req.content)
        file.close()
        print("Downloaded!\n")
        time.sleep(random.randint(1, 6))
    return linkscopy

def get_file_name():
    global i
    name = str(i) + ".jpg"
    i += 1
    return name

def write_file(str, filename):
    with open(filename, "wb") as file:
        file.write(str.encode("utf-8"))

def get_win_title(html):
	return html.cssselect("title")[0].text

def cookie_dict_to_str(**cookie):
    return '; '.join(map('='.join, cookie.items()))

def cookie_str_to_dict(cookie):
    return dict(map(lambda s: s.partition('=')[::2], cookie.split('; ')))

def make_g_tk(p_skey, __cache={}, **cookie):
    if p_skey in __cache:
        return __cache[p_skey]
    tk = 5381
    for c in p_skey:
        tk += (tk<<5) + ord(c)
    tk &= 0x7fffffff
    __cache[p_skey] = tk
    return tk

random.seed(time.time())

url = "http://i.qq.com/"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
capabilities = DesiredCapabilities.PHANTOMJS.copy()
capabilities["phantomjs.page.settings.userAgent"] = userAgent
capabilities["phantomjs.page.settings.loadImages"] = False
driver = webdriver.PhantomJS(desired_capabilities=capabilities)
driver.maximize_window()
css = driver.find_elements_by_css_selector

driver.get(url)
while True:
    try:
        iframe = css("#login_frame")[0]
    except:
        print("finding the login iframe\nWAIT A MOMENT!\n")
        continue
    else:
        driver.switch_to.frame(iframe)
        break
driver.execute_script("var elem = document.getElementById('switcher_plogin'); elem.click()")
user = input("Username:")
password = getpass.getpass()
driver.execute_script('var user = document.getElementById("u"); user.value="' + user + '";')
driver.execute_script('var password = document.getElementById("p");password.value ="' + password + '";')

while driver.title == 'QQ空间-分享生活，留住感动':
    wait_func("Login", 5)
    try:
        driver.execute_script('var submit = document.getElementById("login_button"); submit.click()')
    except:
        print(driver.title + " Logined Successfully!\n")
        break

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
cookies = {}
driver_cookies = driver.get_cookies()
for c in driver_cookies:
    cookies[c["name"]] = c["value"]
s = requests.Session()
s.cookies.update(cookies)
req = s.get("https://user.qzone.qq.com/787359142/myhome/friends", headers=headers)
g_tk = make_g_tk(**cookies)
fri_url = "https://h5.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin=787359142&do=1&fupdate=1&clean=1&g_tk=" + str(g_tk)
req = s.get(fri_url, headers=headers)
write_file(req.text, "friends_list.txt")
