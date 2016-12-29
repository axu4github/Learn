# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from jpype import *


def show(content, title=None):
    if title is not None:
        print('-' * 40)
        print(title)
        print('-' * 40)

    print(content)

    print('=' * 60)

if __name__ == '__main__':
    try:
        startJVM(
            '/Library/Java/JavaVirtualMachines/jdk1.7.0_09.jdk/Contents/MacOS/libjli.dylib',
            '-Djava.class.path=/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/02.hanlp/hanlp-portable-1.3.1.jar',
            '-Xms1g',
            '-Xmx1g'
        )

        s = '中国科学院计算技术研究所的宗成庆教授正在教授自然语言处理课程'
        doc = '''
        水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，
        根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，
        有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，
        严格地进行水资源论证和取水许可的批准。
        '''

        HanLP = JClass('com.hankcs.hanlp.HanLP')
        show(HanLP.segment(s), '分词')

        NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
        show(NLPTokenizer.segment(s), '命名实体识别与词性标注')

        show(HanLP.extractKeyword(doc, 2), '关键词提取')
        show(HanLP.extractSummary(doc, 3), '自动摘要')
    except Exception as e:
        print(e)
    finally:
        shutdownJVM()
