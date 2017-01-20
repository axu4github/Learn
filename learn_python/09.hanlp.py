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
            "/Library/Java/JavaVirtualMachines/jdk1.7.0_09.jdk/Contents/MacOS/libjli.dylib",
            # '-Djava.class.path=/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/02.hanlp/hanlp-portable-1.3.1.jar',
            "-Djava.class.path=/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/02.hanlp/hanlp-1.3.1.jar:/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/02.hanlp/",
            # "-Djava.class.path=/Users/axu/Downloads/data/hanlp-portable-1.3.1.jar",
            # "-Djava.class.path=/Users/axu/code/axuProject/Learn/learn_python/00.fixtures/02.hanlp/hanlp-1.3.1.jar",
            "-Xms1g",
            "-Xmx1g"
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

        test_str = '北京攻城狮逆袭单身狗，迎娶香港白富美，走上人生巅峰'
        show(HanLP.segment(test_str), '自定义词库之前')
        CustomDictionary = JClass(
            'com.hankcs.hanlp.dictionary.CustomDictionary')
        CustomDictionary.add('攻城狮')
        CustomDictionary.add('单身狗')
        CustomDictionary.add('身狗')
        CustomDictionary.insert('白富美', 'nz 1024')

        show(HanLP.segment(test_str), '自定义词库之后-标准分词')

        NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
        show(NLPTokenizer.segment(test_str), '自定义词库之后-NLP分词')

        IndexTokenizer = JClass('com.hankcs.hanlp.tokenizer.IndexTokenizer')
        show(IndexTokenizer.segment(test_str), '自定义词库之后-索引分词')

        # HMMSegment = JClass('com.hankcs.hanlp.seg.HMM.HMMSegment')
        # Segment = JClass('com.hankcs.hanlp.seg.Segment')
        # CRFSegment = JClass('com.hankcs.hanlp.seg.CRF.CRFSegment')
        # # _seg = Segment()
        # class_obj = HMMSegment
        # # print(_hmm)
        # print(class_obj.seg(test_str))

        CustomDictionary.add('自然语言处理')
        test_str = '教授正在北京教授自然语言处理课程'
        segment = HanLP.newSegment()
        show(segment.seg(test_str), '标注调整之前')
        segment.enablePartOfSpeechTagging(True)
        segment.enableOrganizationRecognize(True)
        segment.enablePlaceRecognize(True)
        segment.enableTranslatedNameRecognize(True)
        segment.enableNameRecognize(True)
        show(segment.seg(test_str), '标注调整之后')

        text = '小区居民有的反对喂养流浪猫，而有的居民却赞成喂养这些小宝贝'
        NotionalTokenizer = JClass(
            'com.hankcs.hanlp.tokenizer.NotionalTokenizer')
        show(NotionalTokenizer.segment(text), '停用词-之前')
        CoreStopWordDictionary = JClass(
            'com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary')
        CoreStopWordDictionary.add('居民')
        show(NotionalTokenizer.segment(text), '停用词-之后')
        word_list = IndexTokenizer.segment(text)
        CoreStopWordDictionary.apply(word_list)
        show(word_list, '停用词-基于索引分词结果')
        print(word_list[0])
        show(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"), '依存语法分析')
    except Exception as e:
        print(e)
    finally:
        shutdownJVM()
