# encoding=utf-8
'''
Mac安装JPype
1. 下载 https://sourceforge.net/projects/jpype/ 最新版本
2. 解压，进入目录
3. 执行 sudo python setup.py install

若存在 `error: command 'clang' failed with exit status 1` 的问题
则需要在 setup.py 文件的 `self.includeDirs` 中添加 `"/System/Library/Frameworks/JavaVM.framework/Versions/A/Headers/"` 以便可以找到 `jni.h` 等头文件。
具体可详见：http://blog.csdn.net/jerrychenly/article/details/20545995 说明
'''

from jpype import *

startJVM('/Library/Java/JavaVirtualMachines/jdk1.7.0_09.jdk/Contents/MacOS/libjli.dylib')
java.lang.System.out.println("hello world")
shutdownJVM()
