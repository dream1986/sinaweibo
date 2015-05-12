#!/usr/bin/env python
# coding:utf-8
# manning  2015-5-12

from sinaweibo import SinaWeibo
import jd_utils
import time

if __name__ == "__main__":
    sw = SinaWeibo()
    for item in range(50):
        print sw.get_timeline()
        str_msg = u"自动转发自我的Python机器人，ID=%i AT %s" %(item, jd_utils.current_time())
        sw.post_statuses(str_msg)
        time.sleep(3600)