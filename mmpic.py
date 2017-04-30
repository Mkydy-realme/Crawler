# -*- coding:utf-8 -*-
import os
from bs4 import BeautifulSoup
import requests
import random
import sys




User_Agent = [

        'Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',

        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',

        'Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0',
        'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
                                                                                                                                                    'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/34.0.1847.18 Mobile/11B554a Safari/9537.53',
        'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
        'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
]

def random_desktop_user_agent():
    return random.choice(User_Agent) + str(random.randint(0, 10000))
headers = {
    'User-Agent': random_desktop_user_agent(),
    'Cookie':'2780141445=cd4edcCmhUC8ysTMauRWAnLQ0RzX4%2FRLTmNrj0z4; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1468829500; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1468830320; jdna=5dcd59f6fbeba61d9e42fbac17e43442#1468884922223; Hm_lvt_80cbcbf4e9167bc878bc1158463bab9d=1468884923; Hm_lpvt_80cbcbf4e9167bc878bc1158463bab9d=1468884923; _ga=GA1.2.18541939.1468829500; _gat=1'
                                                                                                                                            }

if(os.name == 'nt'):
        print(u'你正在使用win平台')
else:
        print(u'你正在使用linux平台')

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
#http请求头
url='http://www.mmjpg.com/'
path='D:\img\imgpic'
star_html=requests.get(url,headers=headers)
'''输入你想下载的页数'''
pages=int(input('请输入你要下载的页数(1~65)：'))
for i in range(1,pages+1):
    ul=url+'home/'+str(i)               #获取每一页链接
    star_html=requests.get(ul,headers=headers)
    soup=BeautifulSoup(star_html.text,'lxml')
    all_a=soup.find('div',class_='pic').find_all('a',target='_blank')      #获取每个套图的链接
    for a in all_a:
        alt=a.get_text()
        if (alt != ''):
            print("准备扒取：" + alt)

            # win不能创建带？的目录
            if (os.path.exists(path + alt.strip().replace('?', ''))):
                # print('目录已存在')
                flag = 1
            else:
                os.makedirs(path + alt.strip().replace('?', ''))
                flag = 0
            os.chdir(path + alt.strip().replace('?', ''))
            href=a['href']
            #print(alt,href)
            html = requests.get(href, headers=headers)
            mess = BeautifulSoup(html.text, "lxml")
            pic_max=mess.find('div',class_='page').find_all('a')
            pic_max=pic_max[-2].text            #每个套图图片最大页数
            if (flag == 1 and len(os.listdir(path + alt.strip().replace('?', ''))) >= int(pic_max)):
                print('已经保存完毕，跳过')
                continue
            for num in range(1, int(pic_max) + 1):
                pic=href+'/'+str(num)
                html=requests.get(pic,headers = headers)
                mess=BeautifulSoup(html.text,'lxml')
                pic_url=mess.find('img')           #每张图片的链接
                #print(pic_url)
                #picsrc=pic_url['src']
                
                html=requests.get(pic_url['src'],headers=headers)
                file_name = pic_url['src'].split(r'/')[-1]
                f = open(file_name, 'wb')
                f.write(html.content)
                f.close()
            print('完成')
    print('第',i,'几页完成')





