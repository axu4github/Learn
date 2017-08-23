# -*- coding: utf-8 -*-

from __future__ import with_statement

from fabric.api import (
    run, cd, env
)

env.user = "root"
env.password = "root123"

SOLR_HOME = "/opt/solr-5.5.1"
SOLR_RESTART_COMMAND = "bin/solr restart -c -m 8g -d smartv"
SOLR_STOP_COMMAND = "bin/solr stop"


def stop():
    """节点停止"""
    with cd(SOLR_HOME):
        run(SOLR_STOP_COMMAND)


def restart():
    """节点重启"""
    with cd(SOLR_HOME):
        run(SOLR_RESTART_COMMAND)
