#从百度图片中抽取王祖贤的照片
# coding:utf-8
import urllib
import urllib.request
import urllib.parse
import re
from urllib.request import quote, unquote


def get_html(url):
    page = urllib.request.urlopen(url)
    html_code = page.read()
    # pageFile = open('pageCode.txt', 'w')  # 以写的方式打开pageCode.txt
    # pageFile.write(html_code)  # 写入
    # pageFile.close()  # 开了记得关
    return html_code

def get_image(html_code):
    html_code = html_code.decode('utf-8')
    #print(html_code)
    reg = r'middleURL":"(.+?\.jpg)",'
    reg_img = re.compile(reg)
    #print(html_code)
    img_list = reg_img.findall(html_code)
    #print(img_list)
    x = 0
    for img in img_list:
        urllib.request.urlretrieve(img, 'imgs/%s.jpg' % x)
        x += 1
        print(img)

print('-------网页图片抓取-------')
# print('请输入url:')
#
# url = input()
# if url:
#     pass
# else:
#      print('---没有地址输入正在使用默认地址---')
#      url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'

url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
print('----------正在获取网页---------')
values = {}
values['word'] = '王祖贤'
# data = urllib.parse.urlencode(values)
# print(data)
# url = url+'&'+data
# print(url)
url = url +'&word='+'王祖贤'
ret1 = quote(url, safe=";/?:@&=+$,", encoding="gbk")
print(ret1)

html_code = get_html(ret1)
print('----------正在下载图片---------')
get_image(html_code)
print('-----------下载成功-----------')
exit()
