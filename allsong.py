#encoding='GB2312'
import requests
import os
from HTMLParser import HTMLParser


print '本脚本可以帮助您下载K歌之王中上传的歌曲'+'\n'


bourl = "http://bbs.byr.cn/board/KaraOK"
filepath= 'python/'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',      
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36' }

if os.path.exists(filepath):
    pass
else:
    os.makedirs(filepath)


print '--------------------------'


class PageParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        if tag=='a':
           global p_url
           str_temp='在新窗口打开此主题'
           for (key,val)in attrs:
               if key=='href':
                   p_url=val
               if (key=='title')&(val==str_temp):
                   downSong(p_url)
                
                    
class MyParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        global songHref
        if tag=='a':
            for (key,val)in attrs:
                if key=='href':
                    songHref=val
                    
    def handle_data(self,data):
        global flag
        global songName
        str_find='在新窗口打开'
        if data.find(str_find)>0:   
            flag=True
            songName=data
        else:
            flag=False
           
    def handle_endtag(self, tag):
        global songName
        global flag
      
        if flag&(tag=='a'):
            songName=songName[0:songName.index('(')]
            song =requests.get("http://bbs.byr.cn/"+songHref)
            with open(filepath+songName,'wb') as code:
                code.write(song.content)
            print songName,'downCompleted'
                        
        

def downSong(url):
    songParser=MyParser()
    try:
        songContent=requests.get("http://bbs.byr.cn"+url,headers=headers).content
        songParser.feed(songContent)
    except:
        print '下载错误！！！！！！！！！！！！！！！！'

    


    


p_url=''

flag=False
songName='';
songHref='';
p=80
while p<88:
    global p;
    p=p+1
    temp_url=bourl+"?p="+str(p)
    bbcount =requests.get(temp_url,headers=headers).content
    parser=PageParser()
    parser.feed(bbcount);
    print 'the'+str(p)+'completed------------------------------------------------------------'



