#爬虫爬取图片
import urllib
import urllib.request
import re #正则匹配的库
import random

def load_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)#请求页面
    data = response.read()#获取返回的数据
    return data

def get_image(html):
    regx = r'http://[\S]*jpg' #存储正则表达式
    pattern = re.compile(regx)#py正则匹配的方法
    get_image = re.findall(pattern,repr(html))#repr() 函数将对象转化为供解释器读取的形式。
    #根据正则表达式把所有的图片链接抓出来 存在get_image中 数组形式
    num = 1
   # name = random.randint(9999,999999)
    for img in get_image:
        image = load_page(img)#把链接对应的图片下载
        with open('C:\\Users\\jiaxing\\Desktop\\Photo\\%s.jpg' %num,'ab') as fb:#这个with：事先设置，事后做清理
            fb.write(image)
            print('正在下载第%s张图片'%num)
            num = num+1
           # name = name+1
    print('下载完成！')

url = 'http://pic.haibao.com/piclist/10137/'
#url = 'http://www.mmonly.cc/gqbz/mnbz/9698.html'
#url = 'http://p.weather.com.cn/'
html = load_page(url)
get_image(html)
