# -*- coding: UTF-8 -*-

'''
通过python控制远程的服务器

准备安装：
- pip install pycrypto
- pip install paramiko
- pip install ssh
'''

import ssh

if __name__ == "__main__":
     # 新建一个ssh客户端对象
    myclient = ssh.SSHClient()
    # 设置成默认自动接受密钥
    myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())
    # 连接远程主机
    myclient.connect("10.0.3.45", port=22,
                     username="root", password="root123")
    # 在远程机执行shell命令
    stdin, stdout, stderr = myclient.exec_command("ls -l")
    # 读返回结果
    print stdout.read()
    print stderr.read()
