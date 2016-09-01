---
title: Spark
date: 2016-08-01 19:54:29
tags:
---
<!-- # 快速开始 -->
{% cq %} 快速开始 {% endcq %}

- 通过Spark Shell进行互动分析
    - 基础
    - 使用RDD进行更多的操作
    - 缓存
- Self-Contained Applications
- Where to Go from Here

<!-- more -->

本教程提供了一个快速的Spark使用介绍；首先我们通过Spark Shell介绍Spark API（Python/Scala），其次展示如何（通过Java，Scala，Python）编写应用；[the programming guide]  会有更多参考。

跟随本教程，首先从[Spark官网]下载一个Spark发布版本。因为之后我们不需要使用HDFS，所以你可以下载任意一个Hadoop版本的包。

{% quote %}
Spark下载包说明
(img)
上图Spark官网下载截图（当前最新版本为1.6.2），解释如下：
''Source Code： 源代码（需要自己编译）
''Pre-build with user-provided Hadoop：未验证（个人理解应该是针对其他Hadoop版本编译，比如 [hortonworks] 的Hadoop发行版）
''Pre-build for Hadoop 2.6：针对Hadoop2.6版本编译
''Pre-build for Hadoop 2.4：针对Hadoop2.4版本编译
''Pre-build for Hadoop 2.3：针对Hadoop2.3版本编译
''Pre-build for Hadoop 1.x：针对Hadoop1.x版本编译
''Pre-build for CDH4：针对CDH4版本预编译
{% endquote %}

```blockquote 
Spark下载包说明
(img)
上图Spark官网下载截图（当前最新版本为1.6.2），解释如下：
''Source Code： 源代码（需要自己编译）
''Pre-build with user-provided Hadoop：未验证（个人理解应该是针对其他Hadoop版本编译，比如 [hortonworks] 的Hadoop发行版）
''Pre-build for Hadoop 2.6：针对Hadoop2.6版本编译
''Pre-build for Hadoop 2.4：针对Hadoop2.4版本编译
''Pre-build for Hadoop 2.3：针对Hadoop2.3版本编译
''Pre-build for Hadoop 1.x：针对Hadoop1.x版本编译
''Pre-build for CDH4：针对CDH4版本预编译
```

### Spark Shell 互动分析
#### 基础
Spark Shell 提供一个简单的方式去学习Spark API，以及提供一个强大的工具进行数据的交互式分析。它适用于任何Scala（运行在Java虚拟机上）和Python。可以开始运行它在Spark下载的目录中：
``` python
./bin/pyspark
```
Spark的最主要抽象是一个叫做RDD（_Resilient Distributed Dataset_ - 弹性分布式数据集）的分布式集合。RDD可以从_Hadoop InputFormats_（HDFS文件）中被创建，也可以从其他RDD转换。让我们使用Spark下载目录中的_README.md_文件创建一个新的RDD：
``` py
>>> textFile = sc.textFile("README.md")
```
``` bash
>>> textFile = sc.textFile("README.md")
```
RDD包含可以返回结果的_actions_类型方法和返回一个指向新的RDD指针的transformations类型的方法。让我们从一些actions类型的方法开始。
``` python
>>> textFile.count() # 计算README.md文件的行数
95 

>>> textFile.first() # 返回这个RDD第一项
u'# Apache Spark'
```
下面，让我们使用一个transformation类型的方法。我们将使用filter方法返回一个新的RDD。
``` python
>>> linesWithSpark = textFile.filter(lambda line: "Spark" in line) # filter为transformation类型方法，返回一个新的RDD
>>> linesWithSpark.count() # count为action类型方法，返回计算结果
17
```
我们可以将transformations类型的方法和actions类型的方法链接起来调用
``` python
>>> textFile.filter(lambda line: "Spark" in line).count() # 返回README.md中多少行中出现"Spark"关键字
17
```
### 使用RDD进行更多的操作
RDD的actions方法和transformations方法可以用于更多复杂的计算上。让我们找出”README.md” 文件单行中最多单词的数量。
``` python
>>> textFile.map(lambda line: len(line.split())).reduce(lambda a, b: a if (a > b) else b) # 找到单行中最多单词的数量
14
```
第一个map方法返回一个包括每行单词数量的整数集合（该集合是一个新的RDD）。reduce方法被作用在这个新的RDD上，目的是找出最大的单词数量。map和reduce方法的参数均为Python语言的[匿名方法（lambdas）]，不过我们也可以通过定义顶级方法完成我们想要的。举例说明，我们可以定义一个max方法从而使得程序更容易理解。
```python
>>> def max(a, b):
...     if a > b:
...             return a
...     else:
...             return b
... 
>>> textFile.map(lambda line: len(line.split())).reduce(max)
14
```
---
{% code title lang:python function %}
>>> def max(a, b):
...     if a > b:
...             return a
...     else:
...             return b
... 
>>> textFile.map(lambda line: len(line.split())).reduce(max)
14
{% endcode %}

Hadoop推广时，一个常用的MapReduce方法（Word Count）。在Spark中被如此容易的实现：
``` python
>>> wordCounts = textFile.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b) # 计算 Word Count
```
在这里，我们结合flatMap，map和reduceByKey (它们都属于transformation)方法计算出”README.md”文件中每个单词的数量，并将它们存储在一个含有一系列(string, int)模式的RDD(wordCounts)中。如果想要将计算结果展示在Spark Shell上，我们需要使用collect方法（action）：
``` python
>>> wordCounts.collect()
[(u'when', 1), (u'R,', 1), (u'including', 3), (u'computation', 1), (u'using:', 1), (u'guidance', 2), ...]
```
### 缓存
Spark也支持将数据缓存在集群的内存中。这是一个非常有用的方法，当数据经常重复使用，比如当查询一个规模小并且经常被访问的数据集，或者当运行一个类似于“PagePank”的迭代计算。举一个简单的例子，让我们缓存linesWithSpark数据集：
``` python
>>> linesWithSpark.cache()

>>> linesWithSpark.count()
17

>>> linesWithSpark.count()
17
```
使用Spark缓存只有100行的文件可能看起来会很愚蠢，但是有趣的是这个同样的方法也可以缓存很大的数据集，甚至它们是横跨数十或者数百个服务器节点。如[programming guide]中描述一样，你也可以使用这种交互式的脚本（bin/pyspark）去连接到这么一个集群中。
