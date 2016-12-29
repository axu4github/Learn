# encoding=utf-8
import nltk
# from nltk.book import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba

if __name__ == '__main__':
    content = u'''
    本章分为完全不同风格的两部分。在“语言计算”部分,我们将选取一些语言相关的编程任务而不去解释它们是如何实现的。在“近观 Python”部分,我们将系统地回顾关键的编程概念。两种风格将按章节标题区分,而后面几章将混合两种风格而不作明显的区分。我们希望这种风格的介绍能使你对接下来将要碰到的内容有一个真实的体味,与此同时,涵盖语言学与计算机科学的基本概念。如果你对这两个方面已经有了基本的了解,可以跳到1.5节。我们将在后续的章节中重复所有要点,如果错过了什么,你可以很容易地在 http://www.nltk.org上查询在线参考材料。如果这些材料对你而言是全新的,那么本章将引发比解答本身更多的问题,这些问题将在本书的其余部分讨论。
    '''
    content = '我爱北京天安门'
    print('=' * 40)
    words = " ".join(jieba.cut(content, cut_all=True))
    print(words)
    print('=' * 40)
    print('语言识别：')
    from polyglot.detect import Detector
    detector = Detector(words)
    print(detector.language)
    print('=' * 40)
    print('实体识别：')
    from polyglot.text import Text
    text = Text(words)
    print(text.entities)
    print('=' * 40)
    print('分词：')
    text = Text(content)
    for word in text.words:
        print(word)

    print('=' * 40)
    print('词性标注：')
    for word, tag in text.pos_tags:
        print("%s/%s" % (word, tag))

    print('=' * 40)
