import urllib.request
import io
import sys
from bs4 import BeautifulSoup
from urllib import error
import http
import shadow_useragent
from fake_useragent import UserAgent
import http_client
import random
import requests
import time
import numpy as np
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"
proxyUser = "H3E31R76U6Y797JD"
proxyPass = "436657633E05294E"
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
        "user" : proxyUser,
        "pass" : proxyPass,
}
proxy_handler = urllib.request.ProxyHandler({
        "http"  : proxyMeta,
        "https" : proxyMeta,
})
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
root_url = "https://www.dict.com/%E8%A5%BF%E7%8F%AD%E7%89%99%E8%AF%AD-%E6%B1%89%E8%AF%AD/"
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",



]

#word = input()
fr = open("new 2.txt", 'r', encoding='gb18030')
# 读取文件所有内容
arrayOLines = fr.readlines()
# 去掉UTF-8文件的BOM
arrayOLines[0] = arrayOLines[0].lstrip('\ufeff')
len_array = len(arrayOLines)
fw = open("Spanish-Chinese.txt",'w',encoding="utf-8")
i = 0
flag = False
for line in arrayOLines:

    line = line.strip()
    listFromLine = line.split(",")
    print(listFromLine)
    for list in listFromLine:
        list = list.strip()
        word = list

        #fw.write(word)
        #fw.write("\n")

        user_agent = random.choice(user_agent_list)
        #user_agent = UserAgent().opera
        #user_agent = shadow_useragent.ShadowUserAgent().edge
        #user_agent = 'Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
        print(user_agent)
        headers = {
            'Cookie': 'guid=LWNT756I9L; lang=cn; set=_spcn; _ga=GA1.2.750325472.1576742024; _gid=GA1.2.447993579.1577416199; h_spcn=%e9%aa%a8%e6%8a%98%7cfilial%7csucesion%7cunion%7creducto%7c%e9%aa%a8%7cfronton%7cregresar%7ccuarto%7cfoguear%7crumorearse%7cbanqueta%7cut%c3%b3pico%2fca%7cepiceno%2fna%7cbienio; _gat=1',
            'User-Agent': user_agent
        }
        try:
            proxy_handler = urllib.request.ProxyHandler({
                "http": proxyMeta,
                "https": proxyMeta,
            })
            opener = urllib.request.build_opener(proxy_handler)
            urllib.request.install_opener(opener)

            url = root_url + urllib.parse.quote(word)
            req = urllib.request.Request(url, headers=headers)

            response = urllib.request.urlopen(req)
            print(response.status)
            # response = urllib.request.urlopen(url)
            html = response.read().decode("utf-8")
            soup = BeautifulSoup(html, 'lxml')
            tag = soup.find(class_='entry')
            tag1 = soup.find(class_='lex_ful_morf')

            if (tag == None) or (tag1 == None):
                print("单词不存在释义")
            else:
                tag_soup = tag.find_all(name='tr')
                result = []
                for i in range(len(tag_soup)):
                    if (tag_soup[i].find(class_='lex_ful_morf') != None):
                        result_v = tag_soup[i].find(class_='lex_ful_morf').get_text().strip()
                        result_v = result_v + "."
                        result.append(result_v)

                    elif (tag_soup[i].find(class_='lex_ful_tran w l2') != None):
                        result_v = tag_soup[i].find(class_='lex_ful_tran w l2').get_text()
                        result_v.strip()
                        result_v = result_v.replace(",", ";")
                        result_v = result_v.replace(" ", "")
                        if i != len(tag_soup) - 1:
                            result_v = result_v + ';'

                        result.append(result_v)
                        print(result_v)
                fw = open("Spanish-Chinese.txt", 'a', encoding="utf-8")
                fw.write(word)
                fw.write("\n")
                #tag_soup[i] = tag_soup[i].get_text().strip() + "."
                #print(tag_soup[i])
                fw.write(''.join(result))
                fw.write("\n")
                fw.write("\n")
                fw.close()
                time.sleep(1)
        except error.HTTPError as e:
            print("HTTPError")
        except error.URLError as e:
            print("URLError")
        except http.client.IncompleteRead as e:
            html = e.partial
        except http.client.RemoteDisconnected as e:
            fw = open("YiLou.txt", 'a', encoding="utf-8")
            fw.write(word)
            fw.write("\n")
            fw.close()
fr.close()
"""
url = root_url + urllib.parse.quote(word)
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")
soup = BeautifulSoup(html, 'lxml')
tag_soup = soup.find(class_='entry')
tag_soup[i] = soup.find(class_='lex_ful_morf')
tag_soup[i] = tag_soup[i].get_text() + "."
meanings = tag_soup.find_all(class_='lex_ful_tran w l2')
print(meanings)
print(tag_soup[i], end="")
for i in range(len(meanings)):
    translation = meanings[i].get_text()
    translation = translation.strip()
    translation = translation.replace(',', ';')
    sys.stdout.write(translation)
    if i != len(meanings) - 1:
        print(";", end="")

"""
