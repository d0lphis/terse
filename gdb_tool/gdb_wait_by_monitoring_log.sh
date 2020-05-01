#!/bin/sh

logFile=$ELK_HOME/log/elasticsearch/elk-c20200225.log.master_red21.eng.platformlab.ibm.com
logKeyword=">>>>>>qqq:"
#logKeyword="orchestrator-security"
#logKeyword="======LISTENER:"
#logKeyword="started"
logKeyword="Request params:"
processKeyword="node\.name=master"
breakpoint="Java_com_platform_common_gui_VEMJni_authVemUserToken"

#wait until log file generated
while [ ! -f $logFile ]; do
	sleep 1
done
echo "Log file | $logFile | is detected.:"



#wait until keyword log generated(matching to the time of JNI calling)
#echo "( tail -f -n0 $logFile & ) | grep -q \"$logKeyword\""
( tail -f -n0 $logFile & ) | grep -q "$logKeyword"
echo "Log | $logKeyword | is detected."



#wait until process found
until pid=$(ps -ef | grep "$processKeyword" | awk '{print $2}')
do   
	sleep 1
done
echo "Process id | $pid | is found."



#progress_pid=`ps -ef|grep "node\.name=master"|awk '{print $2}'`
#while [ "$progress_pid" = "" ]; do
#   progress_pid=`ps -ef|grep "node\.name=master"|awk '{print $2}'`
#done



#attach gdb to java process
#gdb -p $pid
#gdb -ex continue -p $pid
gdb \
 -ex "set follow-fork-mode child" \
 -ex "set detach-on-fork off" \
 -ex "b $breakpoint" \
 -p $pid
