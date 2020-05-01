#!/bin/sh

#progress_str=$1
#progress_pid=`pgrep -o $progress_str`
<<<<<<< HEAD
progress_pid=`ps -ef|grep "node\.name=master"|awk '{print $2}'`
=======
progress_pid=`ps -ef|grep elasticsearch|grep client|grep node.name=client|awk '{print $2}'`
>>>>>>> 0bc735ddf9a2cf809bf7319d6f15f7638aa0332b
while [ "$progress_pid" = "" ]; do
#  progress_pid=`pgrep -o $progress_str`
   progress_pid=`ps -ef|grep "node\.name=master"|awk '{print $2}'`
done
#gdb -ex continue -p $progress_pid
<<<<<<< HEAD
#gdb -p $progress_pid
gdb -ex 'b Java_com_platform_common_gui_VEMJni_authVemUserToken' -p $progress_pid
=======
#gdb -ex 'b Java_com_platform_common_gui_VEMJni_authVemUserToken' -p $progress_pid
gdb -p $progress_pid
>>>>>>> 0bc735ddf9a2cf809bf7319d6f15f7638aa0332b
