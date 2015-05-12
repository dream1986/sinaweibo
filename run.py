#!/usr/bin/env python
# coding:utf-8
# manning  2015-5-12
import time
import os
import sys
import codecs

from sinaweibo import SinaWeibo
import jd_utils
import wb_cfg
from toutiao_spider import Toutiao

if __name__ == "__main__":
    tt = Toutiao()
    tt.get_toutiao()
    if os.path.exists(wb_cfg.TTFILE):
        try:
            fp = codecs.open(wb_cfg.TTFILE, 'rb',encoding = 'utf-8')
            content = eval(fp.read())
	except Exception:
	    print u"读写文件错误!"
	    sys.exit(-1)
	finally:
	    fp.close()
        
	sw = SinaWeibo()
        for item in content:
            web_msg = u"标题：" + item['TITLE'].decode('utf-8') + \
            u"\n主题：" + item['SUMMARY'].decode('utf-8') + \
            u"\n链接：" + item['LINK'].decode('utf-8') + \
            u"\n[By Nicol's Robot %s]" % (jd_utils.current_time())
            sw.post_statuses(web_msg)
	    print u"已经自动发送1条微博！"
            time.sleep(200)  #200秒自动发送一条          
	    
	print u"今天推荐结束！"		
	sys.exit(0)