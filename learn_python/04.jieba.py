# encoding=utf-8

import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba.posseg as pseg
import jieba.analyse

jieba.load_userdict('00.fixtures/01.jieba_dicts/customer.txt')
jieba.add_word("到北", freq=2000000000, tag='v')
jieba.add_word("来到", freq=3000000000, tag='v')
jieba.add_word("清华")
# print(jieba.suggest_freq('京清', True))
# print(jieba.suggest_freq(('华', '大'), True))

words = "我来到北京清华大学了"
# words = "华夏银行"
seg_list = jieba.cut(words, cut_all=True, HMM=True)
# 我/ 来到/ 到北/ 北京/ 清华/ 清华大学/ 华大/ 大学/ 了
print("/ ".join(seg_list))

print("=" * 60)
for word, flag in pseg.cut(words):
    print('%s/%s' % (word, flag))

print("=" * 60)

for x, w in jieba.analyse.textrank(words, withWeight=True):
    print('%s %s' % (x, w))

exit()
# seg_list = jieba.cut(words, cut_all=True, HMM=False)
# print("/ ".join(seg_list))

# seg_list = jieba.cut(words, cut_all=True, HMM=True)
# print("/ ".join(seg_list))

# seg_list = jieba.cut(words, cut_all=False)
# # 我/ 来到/ 北京/ 清华大学/ 了
# print("/ ".join(seg_list))

# seg_list = jieba.cut(words)
# # 我/ 来到/ 北京/ 清华大学/ 了
# print("/ ".join(seg_list))

# seg_list = jieba.cut_for_search(words)
# # 我/ 来到/ 北京/ 清华/ 华大/ 大学/ 清华大学/ 了
# print("/ ".join(seg_list))

jieba.add_word('石墨烯', tag='v')
# jieba.add_word('石墨', tag='n')
jieba.add_word('凱特琳')
jieba.del_word('自定义词')

test_sent = (
    "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
    "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)
words = jieba.cut(test_sent)
print('/'.join(words))

print("=" * 40)

result = pseg.cut(test_sent)

for w in result:
    print(w.word + "/" + w.flag + ", ")

import jieba.analyse

content = '网易是中国领先的互联网技术公司,为用户提供免费邮箱、游戏、搜索引擎服务,开设新闻、娱乐、体育等30多个内容频道,及博客、视频、论坛等互动交流,网聚人的力量。'
tags = jieba.analyse.extract_tags(content, topK=10)

print(",".join(tags))

print('=' * 40)
print('3. 关键词提取')
print('-' * 40)
print(' TF-IDF')
print('-' * 40)

s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

print('-' * 40)
print(' TextRank')
print('-' * 40)

for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))

for w in pseg.cut(s):
    print(w.word + "/" + w.flag + ", ")
