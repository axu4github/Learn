#!/bin/sh
# - 功能说明
# - 1. 清理该文件所在目录的.class文件
# - 2. 通过scalac编译制定文件
# - 3. 调用object Enter类的main方法

LOCAL_DIR=$(dirname $0)
CMD="rm -rf $LOCAL_DIR/*.class"

echo "=== 开始清理 $LOCAL_DIR/*.class 文件 ==="
echo "..."
${CMD}
echo "..."
echo "=== 完成清理 $LOCAL_DIR/*.class 文件 ==="
echo ""
echo "=== 开始编译文件 [$1] ... ==="
echo ""
scalac $1
echo ""
echo "=== 完成编译文件 [$1] ... ==="
echo ""
echo "=== 调用 Enter 主方法 ... ==="
echo ""
scala Enter
echo ""
echo "-EOF-"
