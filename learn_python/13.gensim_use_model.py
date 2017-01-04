# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from gensim.models import word2vec
import logging

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    if True:
        # if not True:
        models_path = '/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/03.word2vec/03.models/trained_model.bin'
    else:
        models_path = '/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/03.word2vec/03.models/non_stop_words_model.bin'

    model = word2vec.Word2Vec.load_word2vec_format(models_path, binary=True)
    words = [u'信用卡', u'余额', u'不足', u'不好', u'北京', u'客服']
    for word in words:
        result = model.most_similar(word)
        print '=' * 10 + word + '=' * 10
        for r in result:
            print r[0], r[1]

        print '=' * 20

    # print(model.similarity(u"客服", u"坐席"))

    # print model.doesnt_match(u"早餐 服务 客服 坐席".split())
    print('-EOF-')
