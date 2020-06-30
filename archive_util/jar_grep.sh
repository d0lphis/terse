#!/bin/bash

#search in all jars under current path recursively, list if file contained has name like "Resources.properties", list if the file contains text like "The message to match"
#./jar_grep.sh . "Resources.properties" "The message to match"
#   ./ops-abs.jar
#      com/company/ops/view/web/Resources.properties
#   ./other-abs-1.2.3.jar
#      com/company/other/view/web/Resources.properties
#         The message to match
#   ./commons-abs.jar
#      com/company/common/view/web/Resources.properties
#      com/company/common/view/weba/Resources.properties
#         The message to match
#      com/company/common/view/webb/Resources.properties
#         The message to match
#         The message to match

#search in all jars under current path recursively, list if file contained has name like "Resources.properties"
#./jar_grep.sh . "Resources.properties"
#./jar_grep.sh . "io/netty/handler/codec/compression"
#   ./ops-abs.jar
#      com/company/ops/view/web/Resources.properties
#   ./other-abs-1.2.3.jar
#      com/company/other/view/web/Resources.properties
#   ./commons-abs.jar
#      com/company/common/view/web/Resources.properties
#      com/company/common/view/weba/Resources.properties

sPath="$1"
sFileName="$2"
sText="$3"
#echo $sPath
#echo $sFileName

#declare -A mArchives
#declare -A mFiles
#declare sArchiveFileName

#output=$(find "$sPath" -name '*.jar' | awk '{cmd="unzip -l"; file=$1; grepstr="grep $sFileName"; r=system(cmd" "file" | "grepstr" 2>/dev/null"); if (r==0){print file};}' 2>/dev/null)
#output=$(find . -name "*.jar" -exec bash -c 'unzip -l {} | grep -lH --label {} 'Resources.properties'' \;)
#	/wlfs/sre/nom.kn31rhel78x64.hostname.abs2500.20200614/scd/3.9/linux-x86_64/bin/utils/parallelupgrade.jar:     3797  06-14-2020 18:10   com/blatform/tool/upgrade/ApplicationResources.properties
#	/wlfs/sre/nom.kn31rhel78x64.hostname.abs2500.20200614/scd/wlp/19.0.0.12/lib/com.org.ws.jsp_1.0.35.jar:     3963  12-17-2007 10:06   org/apache/taglibs/standard/lang/jstl/Resources.properties
#	/wlfs/sre/nom.kn31rhel78x64.hostname.abs2500.20200614/scd/wlp/19.0.0.12/lib/com.org.ws.jsp_1.0.35.jar:     9748  12-17-2007 10:06   org/apache/taglibs/standard/resources/Resources.properties
output=$(find "$sPath" -name "*.jar" -exec bash -c 'unzip -l {} | grep -H --label {} '$sFileName'' \; 2>/dev/null)
#echo $output

sLastArchiveName=
sLastArchiveFileName=
for out in grep $output; do
	#if [[ $out == *"/"* ]]; then
	if [[ "${out}" =~ [/.] ]]; then
		if [[ "$out" == *"jar"* ]]; then
			sArchiveName="${out//:}"
			if [ "$sArchiveName" != "$sLastArchiveName" ]; then
				echo "   "$sArchiveName
				sLastArchiveName="$sArchiveName"
				sLastArchiveFileName=
			fi
		else
			#${mArchives["$sArchiveName"]}[i]="$out"
			sArchiveFileName="${out}"
			if [ "$sArchiveFileName" != "$sLastArchiveFileName" ]; then
				echo "      "$sArchiveFileName
				sLastArchiveFileName="$sArchiveFileName"
			fi
			zipgrep "$sText" "$sLastArchiveName" "$sLastArchiveFileName" 2>/dev/null | awk -F ':' '{print "         "$2}'
		fi
	fi
done


#declare -A mArchive
#declare -A mFile
#mFile=([1]="com/company/view/web/Resources.properties:abbe.Pref.description=The message to match." [2]="com/company/view/web/Resources.properties:cdde.Pref.abc.description=The message to match.")
#mArchive["common-abs-1.2.3.jar"]=mFile
#eval echo \${${mArchive["other-abs-1.2.3.jar"]}[1]}



#$ ./archive_grep.sh.ori /wlfs/sre/nom.kn31rhel78x64.hostname.abs2500.20200614/scd/conbuctorspark/conf/packages/Spark2.4.3-Conbuctor2.5.0/a/Spark2.4.3.tgz netty
#	./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/LICENSE:256:io.netty:netty
#	./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/LICENSE:257:io.netty:netty-all
#	./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/python/pyspark.egg-info/SOURCES.txt:350:deps/jars/netty-3.9.9.Final.jar
#	./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/python/pyspark.egg-info/SOURCES.txt:351:deps/jars/netty-all-4.1.17.Final.jar
#	./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/python/pyspark/streaming/flume.py:55:        :param enableDecompression:  Should netty server decompress input stream
#	./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/NOTICE:103:  * http://netty.io/
#	Binary file ./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/yarn/spark-2.4.3-yarn-shuffle.jar matches
#	Binary file ./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/jars/ego/spark-sharedcontext_2.11-2.4.3.jar matches
#	Binary file ./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/jars/ego/ss-spark-core_2.11-2.3.1.jar matches
#	Binary file ./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/jars/ego/spark-core_2.11-2.4.3.jar matches
#	Binary file ./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/jars/netty-3.9.9.Final.jar matches
#	Binary file ./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/jars/arrow-memory-0.10.0.jar matches
#	Binary file ./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/jars/netty-all-4.1.17.Final.jar matches
#	Binary file ./[spark-2.4.3-hadoop-2.7.tgz]/spark-2.4.3-hadoop-2.7/jars/spark-core_2.11-2.4.3.jar matches



#pak=Spark2.4.3.tgz; keyword=Deployment; for i in $(tar -tzf "$pak"); do results=$(tar -Oxzf "$pak" "$i" | grep --label="$i" -H "keyword") && echo "$results"; done

#tar xf Spark2.4.3.tgz -O | grep Deployment

#pak="Spark2.4.3.tgz"; keyword="Deployment"; tar tf $pak | while read -r FILE; do result=$(tar xf $pak $FILE -O | grep "$keyword"); if [ $? == 0 ] && [ "$result" != "" ] ;then echo "$FILE" && while read line; do echo "  ${line}"; done < <(echo "$result") && result=""; fi; done

#pak="a.tar.gz"; keyword="Deployment"; tar tf $pak | while read -r FILE; do result=$(tar xf $pak $FILE -O | grep "$keyword"); if [ $? == 0 ] && [ "$result" != "" ] ;then echo "$FILE" && while read line; do echo "  ${line}"; done < <(echo "$result") && result=""; fi; done

#pak="a.tar.gz"; keyword="Deployment"; tar tf $pak | while read -r FILE; do echo $FILE; done
