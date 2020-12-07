import requests
from bs4 import BeautifulSoup

class b9:
    def __init__(self,url,head):
        self.u=url
        self.h=head
    def Print(self):
        headers={'User-Agent':self.h}
        response=requests.get(self.u,headers=headers)
        print(BeautifulSoup(response.content, 'lxml'))

browser1=b9("https://browsers.spb.ctf.su/",'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0')
browser2=b9("https://browsers.spb.ctf.su/",'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0')
browser3=b9("https://browsers.spb.ctf.su/",'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0')
browser4=b9("https://browsers.spb.ctf.su/",'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Lenovo TB2-X30L Build/LenovoTB2-X30L)')
browser5=b9("https://browsers.spb.ctf.su/",'Opera/9.80 (Android; Opera Mini/9.0.1829/189.71; U; ru) Presto/2.12.423 Version/12.16')
browser6=b9("https://browsers.spb.ctf.su/",'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0')
browser7=b9("https://browsers.spb.ctf.su/",'Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0')
browser8=b9("https://browsers.spb.ctf.su/",'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0')
browser9=b9("https://browsers.spb.ctf.su/",'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')

for b in [browser1,browser2,browser3,browser4,browser5,browser6,browser7,browser7,browser8,browser9]:
    b.Print()