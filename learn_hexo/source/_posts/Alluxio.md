---
title: Alluxio
---

## Alluxio安装

> **注意:** 若想要使用 [容错模式](http://www.alluxio.org/docs/master/cn/Running-Alluxio-Fault-Tolerant.html) 或者想使用 [HDFS作为底层存储系统的话(UNDERFS)](http://www.alluxio.org/docs/master/cn/Configuring-Alluxio-with-HDFS.html) 都需要使用Hadoop，则下载Alluxio时需要选择下载对应Hadoop版本的预编译安装包（下文中因为要使用 `CDH5` 的HDFS，所以下载 `alluxio-1.2.0-cdh5-bin.tar.gz` 的安装包）。

<!-- more -->

### 安装步骤

#### 进入安装目录

```bash
cd /opt
```

#### 下载安装文件

> **注意:** 要下载对应 hadoop 版本的预编译安装包
> 本例使用 `cdh5` 的 `hdfs`，所以下载针对 `cdh5` 的预编译安装包 `alluxio-1.2.0-cdh5-bin.tar.gz`。
> 若使用其他版本的 hadoop，请自行在[Download](http://www.alluxio.org/download)页面选择。

```bash
wget http://downloads.alluxio.org/downloads/files/1.2.0/alluxio-1.2.0-cdh5-bin.tar.gz
```

#### 解压下载文件

```bash
tar -zxvf alluxio-1.2.0-cdh5-bin.tar.gz
```

#### 进入下载目录

```bash
cd alluxio-1.2.0
```

#### 检查下载目录

> **注意:** 若系统提示没有 `ll` 命令，则使用 `ls -l`

```bash
> ll
total 124
drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 assembly
drwxr-xr-x.  2 501 games  4096 Jul 22 05:51 bin
drwxr-xr-x.  5 501 games  4096 Jul 22 05:51 build
drwxr-xr-x.  2 501 games  4096 Jul 22 05:51 conf
drwxr-xr-x.  5 501 games  4096 Jul 22 05:51 core
drwxr-xr-x.  3 501 games  4096 Jul 22 05:51 deploy
drwxr-xr-x. 13 501 games  4096 Jul 22 05:51 docs
drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 examples
drwxr-xr-x.  6 501 games  4096 Jul 22 05:51 integration
drwxr-xr-x.  5 501 games  4096 Jul 22 05:51 keyvalue
drwxr-xr-x.  2 501 games  4096 Jul 22 05:51 libexec
-rw-r--r--.  1 501 games 26847 Jul 22 05:51 LICENSE
drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 minicluster
-rw-r--r--.  1 501 games  4352 Jul 22 05:51 NOTICE
-rw-r--r--.  1 501 games 23665 Jul 22 05:51 pom.xml
-rw-r--r--.  1 501 games  2416 Jul 22 05:51 README.md
drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 shell
drwxr-xr-x.  4 501 games  4096 Jul 22 05:52 tests
drwxr-xr-x. 10 501 games  4096 Jul 22 05:51 underfs
```
#### 修改权限

通过上面的 **检查下载目录** 的输出结果，我们可以看到文件的 **用户** 和 **用户组** 不对，所以需要将下载目录用户和用户组改成 `root`。

```bash
chown -R root:root /opt/alluxio-1.2.0
```

#### 检查权限修改

> **注意:** 若系统提示没有 `ll` 命令，则使用 `ls -l`

```bash
> ll
total 124
drwxr-xr-x.  4 root root  4096 Jul 22 05:52 assembly
drwxr-xr-x.  2 root root  4096 Jul 22 05:51 bin
drwxr-xr-x.  5 root root  4096 Jul 22 05:51 build
drwxr-xr-x.  2 root root  4096 Jul 22 05:51 conf
drwxr-xr-x.  5 root root  4096 Jul 22 05:51 core
drwxr-xr-x.  3 root root  4096 Jul 22 05:51 deploy
drwxr-xr-x. 13 root root  4096 Jul 22 05:51 docs
drwxr-xr-x.  4 root root  4096 Jul 22 05:52 examples
drwxr-xr-x.  6 root root  4096 Jul 22 05:51 integration
drwxr-xr-x.  5 root root  4096 Jul 22 05:51 keyvalue
drwxr-xr-x.  2 root root  4096 Jul 22 05:51 libexec
-rw-r--r--.  1 root root 26847 Jul 22 05:51 LICENSE
drwxr-xr-x.  4 root root  4096 Jul 22 05:52 minicluster
-rw-r--r--.  1 root root  4352 Jul 22 05:51 NOTICE
-rw-r--r--.  1 root root 23665 Jul 22 05:51 pom.xml
-rw-r--r--.  1 root root  2416 Jul 22 05:51 README.md
drwxr-xr-x.  4 root root  4096 Jul 22 05:52 shell
drwxr-xr-x.  4 root root  4096 Jul 22 05:52 tests
drwxr-xr-x. 10 root root  4096 Jul 22 05:51 underfs
```

从上面的输出中，我们可以看出 **用户** 和 **用户组** 已经修改为 `root`

#### 生成配置文件

本例使用`hdfs`作为alluxio的 **底层存储系统(UNDERFS)**

```bash
bin/alluxio bootstrapConf $(hostname) hdfs 
```

> **注意:** 上面执行命令中的 `$(hostname)` 位置是设置 `ALLUXIO_MASTER` 的主机名，因为在本例中，`ALLUXIO_MASTER` 节点就是本机，所以使用 `$(hostname)` 命令获取本机的主机名。
> 若你的 `ALLUXIO_MASTER` 是其他服务器，请将执行命令中 `$(hostname)` 位置的值替换成其他服务器的主机名（一般情况第一个安装的主机都应为 `ALLUXIO_MASTER`）。

#### 查看生成配置文件

```bash
> cat conf/alluxio-env.sh
[...]
ALLUXIO_MASTER_HOSTNAME=${ALLUXIO_MASTER_HOSTNAME:-"server08"}
ALLUXIO_WORKER_MEMORY_SIZE=${ALLUXIO_WORKER_MEMORY_SIZE:-"42933MB"}
ALLUXIO_RAM_FOLDER=${ALLUXIO_RAM_FOLDER:-"/mnt/ramdisk"}
ALLUXIO_UNDERFS_ADDRESS=${ALLUXIO_UNDERFS_ADDRESS:-"hdfs://localhost:9000/alluxio/"} 
```

#### 修改配置文件

在本例中，因为 `hdfs namenode` 不在本机，所以需要修改 `ALLUXIO_UNDERFS_ADDRESS` 参数
将 `ALLUXIO_UNDERFS_ADDRESS` 参数中的 `localhost:9000` 替换为 `server03:8020`

```bash
vim conf/alluxio-env.sh
```

##### 配置文件参数说明

参数 | 说明
--- | ---
`ALLUXIO_MASTER_HOSTNAME` | master（管理）节点的hostname
`ALLUXIO_WORKER_MEMORY_SIZE` | worker（工作）节点可使用内存大小，alluxio可使用的内存存储大小为所有worker（工作）该参数设置的大小之和
`ALLUXIO_RAM_FOLDER` | worker（工作）节点内存存储文件放置目录（和内存存储（一级存储）相关，具体存储内容不知）
`ALLUXIO_UNDERFS_ADDRESS` | 底层存储系统，当内存不足或者某些数据优先级不高的时候，可以将它们设置存储在底层存储系统中，底层存储系统支持很多具体可以查看文档，我们现使用hdfs作为底层存储系统

#### 检查修改内容

``` bash
> cat conf/alluxio-env.sh
[...]
ALLUXIO_MASTER_HOSTNAME=${ALLUXIO_MASTER_HOSTNAME:-"server08"}
ALLUXIO_WORKER_MEMORY_SIZE=${ALLUXIO_WORKER_MEMORY_SIZE:-"42933MB"}
ALLUXIO_RAM_FOLDER=${ALLUXIO_RAM_FOLDER:-"/mnt/ramdisk"}
ALLUXIO_UNDERFS_ADDRESS=${ALLUXIO_UNDERFS_ADDRESS:-"hdfs://server03:8020/alluxio/"} 
```
> **注意:** 需要查看是否可以ping通server03，若不通检查是否有没有配置/etc/hosts文件

#### 设置主机名

##### 设置`ALLUXIO_MASTER`主机名

> **注意:** 在本例中 `ALLUXIO_MASTER` 就是本机，所以可以使用 `$(hostname)` 获取本机主机名

```bash
echo "10.0.1.13 $(hostname)" >> /etc/hosts
```

##### 检查

```bash
> cat /etc/hosts
[...]
10.0.1.13 server08
```

##### 设置`HDFS`主机名

> **注意:** 因为在本例中，使用了`hdfs`作为alluxio的 **底层存储系统(UNDERFS)** （详见  **修改配置文件** 以及 **配置文件参数说明** 章节），所以也需要将`hdfs namenode`的主机名设置到`/etc/hosts`文件中

```bash
echo "10.0.1.8 server03" >> /etc/hosts
```

##### 检查

```bash
> cat /etc/hosts
[...]
10.0.1.13 server08
10.0.1.8 server03
```

> **注意:**
> - `server08`为配置文件（`conf/alluxio-env.sh`）中`ALLUXIO_MASTER_HOSTNAME`配置项的内容
> - `server03`为配置文件（`conf/alluxio-env.sh`）中`ALLUXIO_UNDERFS_ADDRESS`配置项的部分内容
> 
> 具体配置项的意义，请详见 **配置文件参数说明**

#### 格式化

> **注意:** 在执行命令的时候，会提示要输入服务器密码是因为没有创建和`ALLUXIO_MASTER`的`SSH`信任关系，**如何建立信任关系请自行搜索**
> `Waiting for MASTER tasks to finish...`
> `root@localhost's password:`
> `All MASTER tasks finished, please analyze the log at /opt/alluxio-1.2.0/logs/task.log.`
> `Formatting Alluxio Master @ server08`

```bash
bin/alluxio format
```

#### 启动服务

> **注意:** 在执行命令的时候，会提示要输入服务器密码是因为没有创建和`ALLUXIO_MASTER`的`SSH`信任关系，**如何建立信任关系请自行搜索**
> `Killed 0 processes on server08`
> `Killed 0 processes on server08`
> `Waiting for WORKERS tasks to finish...`
> `root@localhost's password:`
> `All WORKERS tasks finished, please analyze the log at /opt/alluxio-1.2.0/logs/task.log.`
> `Starting master @ server08. Logging to /opt/alluxio-1.2.0/logs`
> `Formatting RamFS: /mnt/ramdisk (42933mb)`
> `Starting worker @ server08. Logging to /opt/alluxio-1.2.0/logs`

```bash
bin/alluxio-start.sh local
```

#### 访问浏览器

启动成功后，可以在浏览器中访问 (http://server08:19999) 查看服务内容

![](media/14730423864733/14730637166654.jpg)￼

#### 执行测试用例

```bash
> bin/alluxio runTests
[...]
runTest Basic NO_CACHE ASYNC_THROUGH
2016-09-05 16:16:54,017 INFO  type (BasicOperations.java:writeFile) - writeFile to file /default_tests_files/Basic_NO_CACHE_ASYNC_THROUGH took 9 ms.
2016-09-05 16:16:54,025 INFO  type (BasicOperations.java:readFile) - readFile file /default_tests_files/Basic_NO_CACHE_ASYNC_THROUGH took 8 ms.
Passed the test!
runTest BasicNonByteBuffer NO_CACHE ASYNC_THROUGH
Passed the test!
```

#### 查看测试用例执行结果

##### 通过`alluxio-cli`查看

```bash
>  bin/alluxio fs ls /
24.00B    09-05-2016 16:26:48:993  Directory      /default_tests_files

> bin/alluxio fs ls /default_tests_files
80.00B    09-05-2016 16:26:48:994  In Memory      /default_tests_files/Basic_CACHE_PROMOTE_MUST_CACHE
84.00B    09-05-2016 16:26:49:106  In Memory      /default_tests_files/BasicNonByteBuffer_CACHE_PROMOTE_MUST_CACHE
80.00B    09-05-2016 16:26:49:124  In Memory      /default_tests_files/Basic_CACHE_PROMOTE_CACHE_THROUGH
84.00B    09-05-2016 16:26:50:156  In Memory      /default_tests_files/BasicNonByteBuffer_CACHE_PROMOTE_CACHE_THROUGH
80.00B    09-05-2016 16:26:50:207  In Memory      /default_tests_files/Basic_CACHE_PROMOTE_THROUGH
84.00B    09-05-2016 16:26:50:280  In Memory      /default_tests_files/BasicNonByteBuffer_CACHE_PROMOTE_THROUGH
80.00B    09-05-2016 16:26:50:331  In Memory      /default_tests_files/Basic_CACHE_PROMOTE_ASYNC_THROUGH
84.00B    09-05-2016 16:26:50:362  In Memory      /default_tests_files/BasicNonByteBuffer_CACHE_PROMOTE_ASYNC_THROUGH
80.00B    09-05-2016 16:26:50:384  In Memory      /default_tests_files/Basic_CACHE_MUST_CACHE
84.00B    09-05-2016 16:26:50:410  In Memory      /default_tests_files/BasicNonByteBuffer_CACHE_MUST_CACHE
80.00B    09-05-2016 16:26:50:433  In Memory      /default_tests_files/Basic_CACHE_CACHE_THROUGH
84.00B    09-05-2016 16:26:50:513  In Memory      /default_tests_files/BasicNonByteBuffer_CACHE_CACHE_THROUGH
80.00B    09-05-2016 16:26:50:559  In Memory      /default_tests_files/Basic_CACHE_THROUGH
84.00B    09-05-2016 16:26:50:609  In Memory      /default_tests_files/BasicNonByteBuffer_CACHE_THROUGH
80.00B    09-05-2016 16:26:50:657  In Memory      /default_tests_files/Basic_CACHE_ASYNC_THROUGH
84.00B    09-05-2016 16:26:50:677  In Memory      /default_tests_files/BasicNonByteBuffer_CACHE_ASYNC_THROUGH
80.00B    09-05-2016 16:26:50:696  In Memory      /default_tests_files/Basic_NO_CACHE_MUST_CACHE
84.00B    09-05-2016 16:26:50:714  In Memory      /default_tests_files/BasicNonByteBuffer_NO_CACHE_MUST_CACHE
80.00B    09-05-2016 16:26:50:730  In Memory      /default_tests_files/Basic_NO_CACHE_CACHE_THROUGH
84.00B    09-05-2016 16:26:50:776  In Memory      /default_tests_files/BasicNonByteBuffer_NO_CACHE_CACHE_THROUGH
80.00B    09-05-2016 16:26:50:841  Not In Memory  /default_tests_files/Basic_NO_CACHE_THROUGH
84.00B    09-05-2016 16:26:50:885  Not In Memory  /default_tests_files/BasicNonByteBuffer_NO_CACHE_THROUGH
80.00B    09-05-2016 16:26:50:928  In Memory      /default_tests_files/Basic_NO_CACHE_ASYNC_THROUGH
84.00B    09-05-2016 16:26:50:948  In Memory      /default_tests_files/BasicNonByteBuffer_NO_CACHE_ASYNC_THROUGH
```

##### 通过`web-ui`查看

![](media/14730423864733/14730647082352.jpg)￼

![](media/14730423864733/14730647169708.jpg)￼

##### 通过`hdfs`查看

![](media/14730423864733/14730647745804.jpg)￼

![](media/14730423864733/14730647812403.jpg)￼

> **注意:** 我们可以通过alluxio的`web-ui`看到`/default_tests_files`的文件列表中，`Persistence State`列有`PERSISTED`和`NOT_PERSISTED`区别，也就是该文件是否已经持久化。
> 若文件是`PERSISTED`则该文件会存储到设置的持久化存储中（在本例中是`hdfs`），所以但凡标注的是`PERSISTED`的文件，在`hdfs`的页面中都是可以查到的；但是标注`NOT_PERSISTED`的文件，在`hdfs`的页面中是无法查到的。









