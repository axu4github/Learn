#!/usr/bin/env bash
#
#
# 学习SHELL

# 定义变量
SPARK_HOME='foo'

# 打印变量 ${SPARK_HOME} 和 $SPARK_HOME 输出结果一样
# 有无{}的区别之一是可以规范变量边界，如下例：
# 使用{}后，则打印结果为 [fooA]
echo ${SPARK_HOME}A
# 没有使用{}，则实际去查询变量${SPARK_HOMEA}，因为未声明所以没有结果
echo $SPARK_HOMEA

# 返回脚本名称，执行结果为 [./learn_shell.sh]
echo $0

# 返回当前目录，执行结果为 [.]
echo $(dirname $0)

# 输出执行命令，因为只有dirname "$0"被$()包含，所以只执行dirname "$0"部分
# 其余部分则直接字符串输出，结果为 [cd ./..]
echo cd "$(dirname "$0")"/..

# 输出整体执行结果，因为所有命令均被$()包括，所以输出整体结果
# 输出结果为 [/Users/axu/code/axuProject/Learn] （当前脚本的上一级目录）
echo $(cd "$(dirname "$0")"/..; pwd)

# 打印主机名
echo $(hostname)

# 输出传入参数总数
# 输入：./learn_shell.sh 1 2 3 4
# 输出：4
echo $#

# shift 参数左移
# 输入：./learn_shell.sh 1 2 3 4 5
# 输出： 1 #（1 2 3 4 5）每执行一次shift（相当于执行shift 1）另$0不变，其余参数左移一位
#       2 #（2 3 4 5）
#       3 #（3 4 5）
#       4 #（4 5）
#       5 #（5）
echo $1
shift
echo $1
shift
echo $1
shift
echo $1
shift
echo $1
shift

# 输出系统当前用户
echo $USER
