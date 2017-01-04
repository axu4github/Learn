# -*- coding: utf-8 -*-
# import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from jpype import *

if __name__ == '__main__':
    try:
        source = '/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/03.word2vec/02.formateds/word2vec_integrate.txt'
        # dest = ''
        dest = '/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/03.word2vec/02.formateds/word2vec_non_stop_words_segment.txt'

        startJVM(
            '/Library/Java/JavaVirtualMachines/jdk1.7.0_09.jdk/Contents/MacOS/libjli.dylib',
            '-Djava.class.path=/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/02.hanlp/hanlp-portable-1.3.1.jar',
            '-Xms1g',
            '-Xmx1g'
        )

        # 停用词
        CoreStopWordDictionary = JClass(
            'com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary')
        HanLP = JClass('com.hankcs.hanlp.HanLP')
        segment = HanLP.newSegment()
        segment.enableOrganizationRecognize(True)  # 开启机构名识别
        segment.enablePlaceRecognize(True)  # 开启地名识别
        segment.enableNameRecognize(True)  # 开启人名识别

        f_read = open(source, 'r')
        f_write = open(dest, 'w+')

        for line in f_read:
            items = segment.seg(line)
            # CoreStopWordDictionary.apply(items)
            words = " ".join([item.word for item in items])
            f_write.write(words + "\n")

    except Exception as e:
        print(e)
    finally:
        f_read.close()
        f_write.close()
        shutdownJVM()
