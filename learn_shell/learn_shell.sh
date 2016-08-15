#!/usr/bin/env bash
#
#
# 学习SHELL

SPARK_HOME='foo'

echo ${SPARK_HOME}A

echo $SPARK_HOME

echo $0

echo $(dirname $0)

echo cd "$(dirname "$0")"/..

echo $(cd "$(dirname "$0")"/..; pwd)
