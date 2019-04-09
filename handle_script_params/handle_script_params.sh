#!/bin/bash


function a()
{
	echo a take: $*
}

function b()
{
	echo b take: $*
}



if [ $# -ne 0 ]; then						#if no params for deploy.sh
	echo $1 | grep "^:" > /dev/null
	if [ $? -eq 0 ] ; then					#if first param contains :
		funcName=`echo $1|sed "s%^:%%"`			#remove start : to get function name
		paramsForFunc=`echo $*|sed "s%$1 %%"`
		$funcName $paramsForFunc
		if [ $? -ne 0 ] ; then				#if execute function failed
			echo "Funciton not found!"
		fi
	else
		echo "Normal params for auto process."	
	fi
else
	echo no param
fi
