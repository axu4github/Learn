#!/usr/bin/env bash

# ---
# 学习Linux Shell(Bash)
# ---

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

# 返回执行命令的返回值
# 输入：touch /tmp/test; echo $?
# 输出：若 touch /tmp/test 执行成功则返回0，失败则返回非0 
echo $?

# 返回当前所有输入参数
# 如果之前有执行shift操作，不返回已经被shift移除的参数
# 输入: ./learn_shell.sh 1 2 3 4 5
# 输出: 1 2 3 4 5
# 输入2: ./learn_shell.sh 1 2 3 4 5
#       shift (参数左移一位，第一个参数被移除)
# 输出2: 2 3 4 5 (因为执行过shift命令，所以参数1已经被移除，再执行$@时，则返回未被移除的所有参数)
echo "$@"

# ps 命令为返回进程信息命令
# -p 参数是指进程号
# -o 参数是指返回哪列，最后的"="号是指要不要返回列名
# 输入: ps -p 1 -o comm
# 输出: COMM（列名） 
#      /sbin/launchd（命令）
# 输入: ps -p 1 -o comm=
# 输出: /sbin/launchd （因为后面加入"="号）所以只输出命令，不输出列名
echo $(ps -p 1 -o comm=)

# set -a 设置变量为系统变量，和 export VAR="VALUE" 效果相同
# set +a 配合 set -a 在需要设置很多变量使用，-a是开始（打开）设置系统变量，+a是结束（关闭）设置系统变量
# grep -E "SPARK_HOME|SCALA_HOME" 的意思是查找 包含SPARK_HOME 或者 包含SCALA_HOME 的内容
set -a
SPARK_HOME="/Users/axu/opt/spark-2.0.0-bin-hadoop2.7"
SCALA_HOME="/Users/axu/opt/scala-2.10.4"
set +a

echo $(env)
echo $(env | grep -E "SPARK_HOME|SCALA_HOME")

# if -n 判断字符串不空（真），空（假）
# foo=""
if [ -n "${foo}" ]; then
    echo "${foo}"
else 
    echo "bar"
fi

# print "\0" 类似于数组的分隔符
build_command() {
    echo $(ls -a)
    printf "\0"
    echo "456"
    printf "\0"
    echo "789"
    printf "\0"
    printf "%d\0" $?
}

# 将build_command方法的输出作为输入写入（类似数组的方式）变量CMD中
CMD=()
while IFS= read -d '' -r ARG; do
  CMD+=("$ARG")
done < <(build_command)

# > echo "CMD: ${CMD}" 
# CMD: . .. learn_shell.sh
echo "CMD: ${CMD}"

# 带上'[@]'会将所有内容打出，游标是从0开始，例 echo ${CMD[1]} 输出为：456 
# > echo "CMD: ${CMD[@]}"
# CMD: . .. learn_shell.sh
#  456
#  789
#  0
echo "CMD: ${CMD[@]}"

