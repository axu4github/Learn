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
    result = model.most_similar([u'客服', u'态度', u'不好'])
    for r in result:
        print r[0], r[1]

    # print(model.similarity(u"客服", u"坐席"))

    # print model.doesnt_match(u"早餐 服务 客服 坐席".split())
