# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from gensim.models import word2vec
import logging

if __name__ == '__main__':

    if True:
        # if not True:
        corpus_path = '/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/03.word2vec/02.formateds/word2vec_segment.txt'
        models_path = '/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/03.word2vec/03.models/trained_model.bin'
    else:
        corpus_path = '/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/03.word2vec/02.formateds/word2vec_non_stop_words_segment.txt'
        models_path = '/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/03.word2vec/03.models/non_stop_words_model.bin'

    # 主程序
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    sentences = word2vec.Text8Corpus(corpus_path)  # 加载语料
    # 训练skip-gram模型; 默认window=5
    model = word2vec.Word2Vec(sentences, size=500, min_count=1)
    model.save_word2vec_format(models_path, binary=True)

    # result = model.most_similar(u'信用卡')
    # for r in result:
    #     print r[0], r[1]

    print('-EOF-')
