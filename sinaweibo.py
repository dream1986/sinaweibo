#!/usr/bin/env python
# coding:utf-8
# manning  2015-5-12
import os
import urllib
import urllib2

import wb_cfg
import jd_utils
import time
from weibo import Client


class SinaWeibo:
    def __init__ (self):
        self.APP_KEY = wb_cfg.APP_KEY
        self.APP_SECRET = wb_cfg.APP_SECRET
        self.CALLBACK = wb_cfg.CALLBACK
        self.client = ""
        if os.path.exists(os.getcwd()+"/token"):
            print u"已发现token，调用之！"
            fp = open(os.getcwd()+"/token",'r')
            self.token = eval(fp.read())
            fp.close()
            self.client = Client(self.APP_KEY, self.APP_SECRET, self.CALLBACK,
                                 token = self.token)
            
    def init_once(self):
        client = Client(self.APP_KEY, self.APP_SECRET, self.CALLBACK)
        print u"需要认证的页面为:", client.authorization_url
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0",
                  "Refer": 'https://api.weibo.com',
                  "Method": 'POST',
                  "Connection":"keep-alive"}
        
        postdata = {
            "grant_type":"authorization_code",
            "client_id": wb_cfg.APP_KEY,
            "client_secret": wb_cfg.APP_SECRET,
            "response_type": 'code',   
            "display":"client",
            "redirect_uri":wb_cfg.CALLBACK,
            "userId": wb_cfg.USER,
            "passwd": wb_cfg.PASSWD,
            }  
        
        req  = urllib2.Request(
            url = wb_cfg.AUTH_URL,
            data = urllib.urlencode(postdata),
            headers = headers
        )
        
        resp = urllib2.urlopen(req)
        print resp.geturl()
        print jd_utils.encoding(resp.read()).decode('utf-8')
     
    def get_timeline(self):
        if self.client:
            return self.client.get('users/show', uid=self.token['uid'])
    
    def post_status(self, str_msg):
        if self.client:
            self.client.post('statuses/update', status = str_msg)
        
        
        
if __name__ == "__main__":
    sw = SinaWeibo()
    for item in range(50):
        str_msg = u"自动转发自我的Python机器人，ID=%i AT %s" %(item, jd_utils.current_time())
        sw.post_statuses(str_msg)
        time.sleep(3600)