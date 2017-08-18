# -*- coding: utf-8 -*-

from __future__ import with_statement

from fabric.api import local, run, cd


def hello():
    print("Hello world!")


def ll_something():
    local("ls -l")


def test_run_remote_server_command():
    run("ls -l")


def test_remote_context():
    """
    测试执行命令上下文

    用例

    ```bash
    > cd ${path_of_root}/learn_fabric
    > fab test_remote_context -H10.0.3.49 -uroot -proot123
    [10.0.3.49] Executing task 'test_remote_context'
    [10.0.3.49] run: ls -l
    [10.0.3.49] out: total 1252
    [10.0.3.49] out: drwxr-xr-x  3 root root   4096 Aug 16 11:08 bin
    [10.0.3.49] out: -rw-r--r--  1 root root 555321 May  1  2016 CHANGES.txt
    [10.0.3.49] out: drwxr-xr-x 13 root root   4096 May  1  2016 contrib
    [10.0.3.49] out: drwxr-xr-x  4 root root   4096 Jun 12  2016 dist
    [10.0.3.49] out: drwxr-xr-x 19 root root   4096 Jun 12  2016 docs
    [10.0.3.49] out: drwxr-xr-x  8 root root   4096 Jun 12  2016 example
    [10.0.3.49] out: drwxr-xr-x  2 root root  49152 Jun 12  2016 licenses
    [10.0.3.49] out: -rw-r--r--  1 root root  12646 Feb  1  2016 LICENSE.txt
    [10.0.3.49] out: -rw-r--r--  1 root root 590277 May  1  2016 LUCENE_CHANGES.txt
    [10.0.3.49] out: -rw-r--r--  1 root root  26529 Feb  1  2016 NOTICE.txt
    [10.0.3.49] out: -rw-r--r--  1 root root   7162 May  1  2016 README.txt
    [10.0.3.49] out: drwxr-xr-x 11 root root   4096 Jun 12  2016 server
    [10.0.3.49] out: drwxr-xr-x 12 root root   4096 Jun 23 16:57 smartv
    [10.0.3.49] out: 


    Done.
    Disconnecting from 10.0.3.49... done.
    ```
    """
    with cd("/opt/solr-5.5.1"):
        # run("bin/solr restart -c -m 8g -d smartv")
        run("ls -l")
