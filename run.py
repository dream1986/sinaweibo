#!/usr/bin/env python
# coding:utf-8
# manning  2015-5-12
import time
import os
import sys
import codecs

from jd_utils import log_info, log_warn
from sinaweibo import SinaWeibo
import jd_utils
import jd_logger
import wb_cfg
from toutiao_spider import Toutiao

if __name__ == "__main__":

    main_log = jd_logger.Jd_Logger(u"微博机器人", verbose = False)
    log_info(u"MAIN",u"Application Starting Up!", main_log)
    
    tt = Toutiao(logger = main_log)
    tt.get_toutiao()
    if os.path.exists(wb_cfg.TTFILE):
        try:
            fp = codecs.open(wb_cfg.TTFILE, 'rb',encoding = 'utf-8')
            content = eval(fp.read())
	except Exception:
	    log_warn(u"MAIN",u"Read Write File Error", main_log)
	    sys.exit(-1)
	finally:
	    fp.close()
        
	sw = SinaWeibo(logger = main_log)
        for item in content:
            web_msg = tt.encasp_toutiao(item)
	    try:
		ret = sw.post_statuses(web_msg)	
	    except Exception, e:
		log_warn(u"MAIN",u"Runtime Error:%s" % e, main_log)
		continue	    
	    
	    log_info(u"MAIN",u"Already Send a Status Message！", main_log)
            time.sleep(200)  #200秒自动发送一条          
	
	log_info(u"MAIN",u"Today's Toutiao Retwitter Finished！", main_log) 
	
	log_info(u"MAIN",u"Enter Repost Mode！", main_log) 
	sw.repost(12000)
	
	log_info(u"MAIN",u"Task Finieshed！", main_log) 
    
	sys.exit(0)