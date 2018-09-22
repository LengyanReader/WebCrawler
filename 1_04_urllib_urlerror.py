import os
os.getcwd()

#������
#4.2  ����ʹ��Urllib��ȡ��ҳ
#(1)
import urllib.request

#(2)
file=urllib.request.urlopen("http://news.baidu.com/")

#(3)
data=file.read() # all,string
dataline=file.readline()   # oneline list

#(4)
print(dataline)

#(5)
print(data)

#(6) -06
fhandle=open("D:\\DS_thing\\WebCrawler\\1_04_06.html","wb")

fhandle.write(data)

fhandle.close()

#(7)  
filename=urllib.request.urlretrieve("http://news.baidu.com/"
            ,filename="D:\\DS_thing\\WebCrawler\\1_04_07.html")

#(8)
urllib.request.urlcleanup()   # to clear cache
#-------------------------------------------------------------------
#(9)
file.info()
# <http.client.HTTPResponse at 0x2838706b550>

#(10)
file.getcode()
#200

#(11)
file.geturl()
#'http://news.baidu.com/'

#(12)
urllib.request.quote("http://www.sina.com.cn")  # code
# 'http%3A//www.sina.com.cn'

#(13)
urllib.request.unquote("http%3A//www.sina.com.cn")   # decode
#'http://www.sina.com.cn'
#########################################################################################
#4.3  ���������ȫģ��--Headers����
#(1)
import urllib.request
url= "http://blog.csdn.net/weiwei_pig/article/details/51178226"
file=urllib.request.urlopen(url)

#(2)
import urllib.request
url= "http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data=opener.open(url).read()

#(3)
fhandle=open("D:\\DS_thing\\WebCrawler\\1_043_03.html","wb")
fhandle.write(data)
fhandle.close()

#(4)  add header
import urllib.request
url= "http://blog.csdn.net/weiwei_pig/article/details/51178226"
req=urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
data=urllib.request.urlopen(req).read()

#4.4  ��ʱ����
#(1)
import urllib.request
for i in range(1,100):
    try:
        file=urllib.request.urlopen("http://yum.iqianyue.com",timeout=1) # s
        data=file.read()
        print(len(data))
    except Exception as e:
        print("�����쳣-->"+str(e))
#(2)
import urllib.request
for i in range(1,100):
    try:
        file=urllib.request.urlopen("http://yum.iqianyue.com",timeout=30)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("�����쳣-->"+str(e))

#4.5  HTTPЭ������ʵս
#(1)
import urllib.request
keywd="hello"
url="http://www.baidu.com/s?wd="+keywd
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open("D:\\DS_thing\\WebCrawler\\1_045_01.html","wb")
fhandle.write(data)
fhandle.close()

#(2)
import urllib.request
url="http://www.baidu.com/s?wd="
key="Τ����ʦ"
key_code=urllib.request.quote(key)
url_all=url+key_code
req=urllib.request.Request(url_all)
data=urllib.request.urlopen(req).read()
fh=open("D:\\DS_thing\\WebCrawler\\1_045_02.html","wb")
fh.write(data)
fh.close()

#(3) coding
import urllib.request
import urllib.parse
url = "http://www.iqianyue.com/mypost/"
postdata =urllib.parse.urlencode({
"name":"ceo@iqianyue.com",
"pass":"aA123456"
}).encode('utf-8') #������ʹ��urlencode���봦���ʹ��encode()����Ϊutf-8����
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
data=urllib.request.urlopen(req).read()
fhandle=open("D:/Python35/myweb/part4/6.html","wb")
fhandle.write(data)
fhandle.close()

#4.6  �������֮���������������
#(1)  
def use_proxy(proxy_addr,url):
    import urllib.request
    proxy= urllib.request.ProxyHandler({'http':proxy_addr})  
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr="101.94.1.155:8118"  #http://www.xicidaili.com/
data=use_proxy(proxy_addr,"http://news.baidu.com/")
print(len(data))

#4.7  DebugLogʵս
#(1)
import urllib.request
httphd=urllib.request.HTTPHandler(debuglevel=1)
httpshd=urllib.request.HTTPSHandler(debuglevel=1)
opener=urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data=urllib.request.urlopen("http://edu.51cto.com")

#4.8  �쳣��������--URLErrorʵս
#(1)
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)

#(2)
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)

#(3)
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.baidusss.net")
except urllib.error.HTTPError as e:
    print(e.reason)

#(4)
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.baidusss.net")
except urllib.error.URLError as e:
    print(e.reason)

#(5)
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.baidusss.net")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)

#(6)
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://www.baidussssss.net")
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)

#(7)
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)

