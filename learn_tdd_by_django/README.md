学习测试驱动开发(Test-Driven Development,TDD)

来源：《Python Web开发：测试驱动方法》

---

# 笔记

# 功能测试

- 功能测试（Function Test）
- 验收测试（Acceptance Test）
- 端到端测试（End-to-End Test）
- 黑箱测试（Black Box Test）

# 有用的 TDD 概念
- 用户故事
  - 从用户的角度描述应用应该如何运行。用来组织功能测试。

- 预期失败
  - 意料之中的失败。

# 单元测试及其与功能测试的区别
功能测试站在用户的角度从外部测试应用,单元测试则站在 程序员的角度从内部测试应用。

# TDD编写测试流程

- 1. 先写功能测试，从用户的角度描述应用的新功能
- 2. 功能测试失败后,想办法编写代码让它通过(或者说至少让当前失败的测试通过)。此时,使用一个或多个单元测试定义希望代码实现的效果,保证为应用中的每一行代码 (至少)编写一个单元测试。
- 3. 单元测试失败后,编写最少量的应用代码,刚好让单元测试通过。有时,要在第2步和第3步之间多次往复,直到我们觉得功能测试有一点进展为止。
- 4. 然后,再次运行功能测试,看能否通过,或者有没有进展。这一步可能促使我们编写一些新的单元测试和代码等。

### Tips: 每一次修改的代码要尽量少,让失败的测试通过即可。

# 遵守“不测试常量”规则
单元测试的规则之一是“不测试常量”。以文本形式测试 HTML很大程度上就是测试常量。，单元测试要测试的其实是逻辑、流程控制和配置。编写断言检测HTML字符串中是否有指 定的字符序列,不是单元测试应该做的。

# TDD流程
- 功能测试；
- 单元你测试；
- “单元测试/编写代码”循环；
- 重构。

# 程序中添加空行
```python
def test_home_page_can_save_a_POST_request(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item'

    response = home_page(request)
    self.assertIn('A new list item', response.content.decode())
```
你想知道为什么要在测试中添加一个空行吗?我把开头三行放在一起,作用是设置测试的背景;然后在中间添加一行调用要测试的函数;最后编写断言。这么做并不是强制要求,但可以看清测试的结构。“设置配置 - 执行代码 - 编写断言”是单元测试的典型结构。

# “遇红 / 变绿 / 重构”和三角法
“单元测试 / 编写代码”循环有时也叫“遇红 / 变绿 / 重构”:
- 先写一个会失败的单元测试(遇红);
- 编写尽可能简单的代码让测试通过(变绿),就算作弊也行;
- 重构,改进代码,让其更合理。

# 事不过三,三则重构
编程中有个原则叫作“不要自我重复”(Don’t Repeat Yourself, DRY),按照真言“事不过三,三则重构”的说法,运用这个原则。复制粘贴一次,可能还不用删除重复,但如果复制粘贴了三次,就该删除重复了。

# 更好的单元测试实践方法:一个测试只测试一件事
现在视图函数处理完 POST 请求后会重定向,这是习惯做法,而且单元测试也一定程度上缩短了,不过还可以做得更好。良好的单元测试实践方法要求,一个测试只能测试一件事。因为这样便于查找问题。如果一个测试中有多个断言,一旦前面的断言导致测试失 败,就无法得知后面的断言情况如何。下一章会看到,如果不小心破坏了视图函数,我们想知道到底是保存对象时出错了,还是响应的类型不对。

# 有用的 TDD 概念

## 回归
新添加的代码破坏了应用原本可以正常使用的功能。

## 意外失败
测试在意料之外失败了。这意味着测试中有错误,或者测试帮我们发现了一个回归,因此要在代码中修正。

## 遇红/变绿/重构
描述 TDD 流程的另一种方式。先编写一个测试看着它失败(遇红),然后编写代码 让测试通过变绿),最后重构,改进实现方式。

## 三角法
添加一个测试,专门为某些现有的代码编写用例,以此推断出普适的实现方式(在此之前的实现方式可能作弊了)。

## 事不过三,三则重构
判断何时删除重复代码时使用的经验法则。如果两段代码很相似,往往还要等到第三段相似代码出现,才能确定重构时哪一部分是真正共通、可重用的。

## 记在便签上的待办事项清单
在便签上记录编写代码过程中遇到的问题,等手头的工作完成后再回过头来解决。

# YAGNI（You aint gonna need it）
关于设计的思考一旦开始就很难停下来,我们会冒出各种想法:或许想给每个清单起个名字或加个标题,或许想使用用户名和密码识别用户,或许想给清单添加一个较长的备注和简短的描述,或许想存储某种顺序,等等。但是,要遵守敏捷理念的另一个信条:“YAGNI”(读作 yag-knee)。它是“You aint gonna need it”的简称(“你不需要这个”)。作为软件开发者,我们从创造事物中获得乐趣。有时我们冒出一个想法,觉得可能需要,便无法抵御内心的冲动想要开发出来。可问题是,不管想法有多好,大多数情况下最终你都用不到这个功能。应用中会残留很多没用的代码,还增加了应用的复杂度。YAGNI是个真言,可以用来抵御热切的创造欲。

# 元注释
``` python
[...]
# 页面再次更新,她的清单中显示了这两个待办事项 
self.check_for_row_in_list_table('2: Use peacock feathers to make a fly') self.check_for_row_in_list_table('1: Buy peacock feathers')
# 现在一个叫作弗朗西斯的新用户访问了网站
## 我们使用一个新浏览器会话 # ➊ 
## 确保伊迪丝的信息不会从cookie中泄露出来 # ➊ 
self.browser.quit()
self.browser = webdriver.Firefox()
# 弗朗西斯访问首页
# 页面中看不到伊迪丝的清单 
self.browser.get(self.live_server_url)
page_text = self.browser.find_element_by_tag_name('body').text 
self.assertNotIn('Buy peacock feathers', page_text) 
self.assertNotIn('make a fly', page_text)
[...]
```
➊ 按照习惯,我使用两个 # 号表示“元注释”。元注释的作用是说明测试的工作方式,以及为什么这么做。使用两个井号是为了和功能测试中解说用户故事的常规注释区分开。这个元注释是发给未来的自己的消息,如果没有这个消息,到时你可能会觉得奇怪,想知道到底为什么要退出浏览器再启动一个新会话。

---

``` python 
class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new', # ➊
             data={'item_text': 'A new list item'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        def test_redirects_after_POST(self):
            response = self.client.post(
                '/lists/new', # ➊
                data={'item_text': 'A new list item'}
            )

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
```
➊ 顺便说一句,这里也要注意末尾的斜线——/new后面不加斜线。我的习惯是,不在修改数据库的“操作”后加斜线。

---
# 有用的 TDD 概念和经验法则
- 测试隔离和全局状态
  - 不同的测试之间不能彼此影响,也就是说每次测试结束后都要还原所做的永久性操作。Django的测试运行程序可以帮助我们创建一个测试数据库,每次测试结束后都 会清空数据库(详情参见第 19 章)。
- 从一个可运行状态到另一个可运行状态(又叫测试山羊与重构猫)
  - 本能经常驱使我们直接动手一次修正所有问题,但如果不小心,最终可能像重构猫一样,改动了很多代码但都不起作用。测试山羊建议我们一次只迈一步,从一个可 运行状态走到另一个可运行状态。
- YAGNI
  - You ain’t gonna need it”(你不需要这个)的简称,劝诫你不要受诱惑编写当时看起来可能有用的代码。很有可能你根本用不到这些代码,或者没有准确预见未来的需求。第 18 章给出了一种方法,可以让你避免落入这个陷阱。
