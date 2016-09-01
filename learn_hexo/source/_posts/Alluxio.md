---
title: Alluxio
---

# Alluxio部署
## 目录
[TOC]

## Alluxio安装
> **注意:** 若想要使用 [容错模式](http://www.alluxio.org/docs/master/cn/Running-Alluxio-Fault-Tolerant.html) 或者想使用 [HDFS作为底层存储系统的话(UNDERFS)](http://www.alluxio.org/docs/master/cn/Configuring-Alluxio-with-HDFS.html) 都需要使用Hadoop，则下载Alluxio时需要选择下载对应Hadoop版本的预编译安装包（下文中因为要使用 `CDH5` 的HDFS，所以下载 `alluxio-1.2.0-cdh5-bin.tar.gz` 的安装包）。

<!-- more -->

### 安装步骤
```bash
# 进入安装目录
cd /opt

# 下载安装文件
# 注意要下载对应 hadoop 版本的预编译安装包
# 本例使用 cdh5 的 hdfs，所以下载针对 cdh5 的预编译安装包 alluxio-1.2.0-cdh5-bin.tar.gz
# 若使用其他版本的 hadoop，请自行在Download页面（http://www.alluxio.org/download）选择
wget http://downloads.alluxio.org/downloads/files/1.2.0/alluxio-1.2.0-cdh5-bin.tar.gz

# 解压
tar -zxvf alluxio-1.2.0-cdh5-bin.tar.gz

# 进入下载目录
cd alluxio-1.2.0

# 检查（若系统提示没有ll，则使用ls -l）
# > ll
# total 124
# drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 assembly
# drwxr-xr-x.  2 501 games  4096 Jul 22 05:51 bin
# drwxr-xr-x.  5 501 games  4096 Jul 22 05:51 build
# drwxr-xr-x.  2 501 games  4096 Jul 22 05:51 conf
# drwxr-xr-x.  5 501 games  4096 Jul 22 05:51 core
# drwxr-xr-x.  3 501 games  4096 Jul 22 05:51 deploy
# drwxr-xr-x. 13 501 games  4096 Jul 22 05:51 docs
# drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 examples
# drwxr-xr-x.  6 501 games  4096 Jul 22 05:51 integration
# drwxr-xr-x.  5 501 games  4096 Jul 22 05:51 keyvalue
# drwxr-xr-x.  2 501 games  4096 Jul 22 05:51 libexec
# -rw-r--r--.  1 501 games 26847 Jul 22 05:51 LICENSE
# drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 minicluster
# -rw-r--r--.  1 501 games  4352 Jul 22 05:51 NOTICE
# -rw-r--r--.  1 501 games 23665 Jul 22 05:51 pom.xml
# -rw-r--r--.  1 501 games  2416 Jul 22 05:51 README.md
# drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 shell
# drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 tests
# drwxr-xr-x. 10 501 games  4096 Jul 22 05:51 underfs
ll 

# 可以看到文件的 用户 和 用户组 不对，所以需要修改用户和用户组
# 将下载目录用户和用户组改成root
chown -R root:root /opt/alluxio-1.2.0

# 检查（若系统提示没有ll，则使用ls -l）
# > ll
# total 124
# drwxr-xr-x.  4 root root  4096 Jul 22 05:52 assembly
# drwxr-xr-x.  2 root root  4096 Jul 22 05:51 bin
# drwxr-xr-x.  5 root root  4096 Jul 22 05:51 build
# drwxr-xr-x.  2 root root  4096 Jul 22 05:51 conf
# drwxr-xr-x.  5 root root  4096 Jul 22 05:51 core
# drwxr-xr-x.  3 root root  4096 Jul 22 05:51 deploy
# drwxr-xr-x. 13 root root  4096 Jul 22 05:51 docs
# drwxr-xr-x.  4 root root  4096 Jul 22 05:52 examples
# drwxr-xr-x.  6 root root  4096 Jul 22 05:51 integration
# drwxr-xr-x.  5 root root  4096 Jul 22 05:51 keyvalue
# drwxr-xr-x.  2 root root  4096 Jul 22 05:51 libexec
# -rw-r--r--.  1 root root 26847 Jul 22 05:51 LICENSE
# drwxr-xr-x.  4 root root  4096 Jul 22 05:52 minicluster
# -rw-r--r--.  1 root root  4352 Jul 22 05:51 NOTICE
# -rw-r--r--.  1 root root 23665 Jul 22 05:51 pom.xml
# -rw-r--r--.  1 root root  2416 Jul 22 05:51 README.md
# drwxr-xr-x.  4 root root  4096 Jul 22 05:52 shell
# drwxr-xr-x.  4 root root  4096 Jul 22 05:52 tests
# drwxr-xr-x. 10 root root  4096 Jul 22 05:51 underfs
#
# 可以看出用户和用户组已经修改完成
ll

# 生成配置文件
# 本例使用hdfs作为alluxio的底层存储系统(UNDERFS)
bin/alluxio bootstrapConf $(hostname) hdfs 

# 查看生成配置文件
# > cat conf/alluxio-env.sh
# [...]
# ALLUXIO_MASTER_HOSTNAME=${ALLUXIO_MASTER_HOSTNAME:-"server08"}
# ALLUXIO_WORKER_MEMORY_SIZE=${ALLUXIO_WORKER_MEMORY_SIZE:-"42933MB"}
# ALLUXIO_RAM_FOLDER=${ALLUXIO_RAM_FOLDER:-"/mnt/ramdisk"}
# ALLUXIO_UNDERFS_ADDRESS=${ALLUXIO_UNDERFS_ADDRESS:-"hdfs://localhost:9000/alluxio/"} 
cat conf/alluxio-env.sh

# 修改配置文件
# 配置文件参数说明
# - ALLUXIO_MASTER_HOSTNAME：master（管理）节点的hostname
# - ALLUXIO_WORKER_MEMORY_SIZE：worker（工作）节点可使用内存大小，alluxio可使用的内存存储大小为所有worker（工作）该参数设置的大小之和
# - ALLUXIO_RAM_FOLDER：worker（工作）节点内存存储文件放置目录（和内存存储（一级存储）相关，具体存储内容不知）
# - ALLUXIO_UNDERFS_ADDRESS：底层存储系统，当内存不足或者某些数据优先级不高的时候，可以将它们设置存储在 底层存储系统 中，底层存储系统支持很多具体可以查看文档，我们现使用hdfs作为底层存储系统
# 
# 根据配置文件说明修改配置参数
# 在本例中，因为 hdfs namenode 不在本机，所以需要修改 ALLUXIO_UNDERFS_ADDRESS 参数
# 将 ALLUXIO_UNDERFS_ADDRESS 参数中的 localhost:9000 替换为 server06:8020
vim conf/alluxio-env.sh

# 修改完成后检查
# > cat conf/alluxio-env.sh
# [...]
# ALLUXIO_MASTER_HOSTNAME=${ALLUXIO_MASTER_HOSTNAME:-"server08"}
# ALLUXIO_WORKER_MEMORY_SIZE=${ALLUXIO_WORKER_MEMORY_SIZE:-"42933MB"}
# ALLUXIO_RAM_FOLDER=${ALLUXIO_RAM_FOLDER:-"/mnt/ramdisk"}
# ALLUXIO_UNDERFS_ADDRESS=${ALLUXIO_UNDERFS_ADDRESS:-"hdfs://server06:8020/alluxio/"} 
# 
# #!# 注意需要查看是否可以ping通server06，若不通检查是否有没有配置/etc/hosts文件
cat conf/alluxio-env.sh


```


