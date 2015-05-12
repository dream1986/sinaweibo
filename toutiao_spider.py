#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8


import urllib2
import urllib
import codecs
import re
import os
from BeautifulSoup import BeautifulSoup

import jd_utils
import wb_cfg


tt_main_url = "http://toutiao.io/"
tt_headers = { "Host":"toutiao.io",
               "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0",
               "Connection":"keep-alive"
               }


class Toutiao:
    def __init__(self):
	if os.path.exists(wb_cfg.TTFILE):
	    os.remove(wb_cfg.TTFILE)
        pass
    
    def get_toutiao(self):
	fetch_result = []
	try:
	    request = urllib2.Request(tt_main_url, headers = tt_headers)
	    html = urllib2.urlopen(request).read()
	except UnicodeDecodeError:
	    print u"GBK/Unicode编解码错误!"
	    return
	except Exception:
	    print u"未知错误!"
	    return	
	soup = BeautifulSoup(html)
	contents = soup.findAll('div', attrs = {"class":"content"} )
	for item in contents:
	    title = item.find('h3', attrs = {"class":"title"})
	    summary = item.find('p', attrs = {"class":"summary"})
	    if title and summary:
		if title.a.string and title.a['href'] and summary.a.string:
		    #str_msg = u"{'title':'%s', 'summary':'%s', 'link':'%s'}" % (title.a.string, summary.a.string, title.a['href'])
		    fetch_item = dict(TITLE=title.a.string.encode('utf-8'), SUMMARY=summary.a.string.encode('utf-8'), LINK=title.a['href'].encode('utf-8'))
		    fetch_result.append(fetch_item)
	print u"今天抓取结束！"
	print u"总共抓取%d条头条！" % len(fetch_result)
	
	try:
	    fp = codecs.open(wb_cfg.TTFILE, 'wb',encoding = 'utf-8')
	    msg = repr(fetch_result)
	    fp.write(msg)
	except Exception:
	    print u"读写文件错误!"
	finally:
	    fp.close()
		
if __name__ == "__main__":
    tt = Toutiao()
    tt.get_toutiao()
	
	
        
