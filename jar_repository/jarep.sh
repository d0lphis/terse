#!/bin/bash

# .jarep.sh <path_containing_bunch_of_jars>

for jar in $1/*.jar; do
	pomPropertiesFilePathInfo=$(unzip -l $jar | grep pom.properties)
	if [ $? -ne 0 ]; then
		echo "[NEED MANUAL PROCESS] $1$jar doesn't have pom.properties."
	else
		pomPropertiesFilePath=$(echo $pomPropertiesFilePathInfo | awk '{print $4}')
		jarInfo=`unzip -p $jar $pomPropertiesFilePath`
		gid=$(echo -e "$jarInfo" | grep -oP 'groupId=\K(.*)' | tr -cd '\11\12\40-\176')
		aid=$(echo -e "$jarInfo" | grep -oP 'artifactId=\K(.*)' | tr -cd '\11\12\40-\176')
		ver=$(echo -e "$jarInfo" | grep -oP 'version=\K(.*)' | tr -cd '\11\12\40-\176')
		echo -e "<dependency>\n\t<groupId>$gid</groupId>\n\t<artifactId>$aid</artifactId>\n\t<version>$ver</version>\n</dependency>" 
	fi
done
