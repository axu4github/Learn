# -*- coding: utf-8 -*-

import os
import commands
from solrcloudpy.connection import SolrConnection

BASE = os.path.dirname(os.path.abspath(__file__))
SOLR_NODES = ["10.0.3.49:8983", "10.0.3.51:8983"]
SOLR_VERSION = "5.5.1"
SOLR_COLLECTION = "collection1"


def remote_solr_restart(host):
    """远程执行重启命令"""
    command = "fab -f {fabfile} -H {host} restart".format(
        fabfile=BASE + "/solr_actions.py",
        host=host
    )
    commands.getstatusoutput(command)


def restart_stoped_solr_node():
    """重启已经停止的节点"""
    coll = SolrConnection(SOLR_NODES, version=SOLR_VERSION)[SOLR_COLLECTION]
    shards = coll.state.shards.dict
    for _, shard in shards.items():
        for _, replica in shard["replicas"].items():
            # print replica["base_url"], replica["node_name"], replica["state"]
            ip_address = replica["node_name"].split(":")[0]
            print ip_address, replica["state"]
            if replica["state"] in ["down"]:
                remote_solr_restart(ip_address)


def main():
    restart_stoped_solr_node()


if __name__ == '__main__':
    main()
