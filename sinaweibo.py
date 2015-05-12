#!/usr/bin/env python
# coding:utf-8
# manning  2015-5-12
import os
import urllib
import urllib2
import requests

import wb_cfg
from weibo import Client


class SinaWeibo:
    def __init__ (self):
        self.APP_KEY = wb_cfg.APP_KEY
        self.APP_SECRET = wb_cfg.APP_SECRET
        self.CALLBACK = wb_cfg.CALLBACK
        self.USER = wb_cfg.USER
        self.PASSWD = wb_cfg.PASSWD
        self.UID = wb_cfg.UID
        try:
            self.client = Client(self.APP_KEY, self.APP_SECRET, self.CALLBACK, 
                                token=None, 
                                username=self.USER, 
                                password=self.PASSWD)
            print u"用户%s登陆成功！" % self.USER
        except Exception:
            print u"用户认证失败。。。"
            pass
        
     
    def get_timeline(self):
        if self.client:
            return self.client.get('users/show', uid = self.UID)
    
    def post_statuses(self, str_msg):
        if self.client:
            self.client.post('statuses/update', status = str_msg, uid = self.UID)
        
        
        
