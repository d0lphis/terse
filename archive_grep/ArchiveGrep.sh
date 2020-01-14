#!/bin/bash

#search in all jars under current path recursively, list if file contained has name like "Resources.properties", list if the file contain text like "The message to match"
#./ArchiveGrep.sh . "Resources.properties" "The message to match"
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
#./ArchiveGrep.sh . "Resources.properties"
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
#output=$(find . -name "*.jar" -exec bash -c 'unzip -l {} | grep -H --label {} 'Resources.properties'' \;)
output=$(find "$sPath" -name "*.jar" -exec bash -c 'unzip -l {} | grep -H --label {} '$sFileName'' \; 2>/dev/null)
#echo $output

sLastArchiveName=
sLastArchiveFileName=
for out in grep $output; do
	if [[ $out == *"/"* ]]; then
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
