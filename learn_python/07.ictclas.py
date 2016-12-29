# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pynlpir

if __name__ == '__main__':
    pynlpir.open()
    s = '欢迎科研人员、技术工程师、企事业单位与个人参与NLPIR平台的建设工作。'
    s = u'我爱北京天安门'
    s = u'云计算和大数据技术是2016年的技术'
    r = ''
    for word, tag in pynlpir.segment(s):
        r += "%s/%s, " % (word, tag)

    print(r)
