#!/bin/bash

#this can be simply achieved by following, con: matches showing in bad view, cannot detect matches in nested archive(more than 1 depth)
#$ zgrep -an deploy *
#1.txt:1:deployment
#2.txt:1:deployment
#3.txt:1:deployment
#a.tar.gz:1:1.txt0000644000000000000000000000001313672711266010462 0ustar  rootrootdeployment
#b.tar.gz:3:àÖ셞(2.txt0000644000000000000000000000001313672711275010463 0ustar  rootrootdeployment
#c.tar.gz:6:FÁ(£`Açî(3.txt0000644000000000000000000000001313672711300010451 0ustar  rootrootdeployment



cd `dirname $0` > /dev/null
exeScriptPath=`pwd`
cd - > /dev/null

. $exeScriptPath/lib/com.sh
#echo $archiveTypeToMatch



sPath="$1"
sFileName="$2"
sText="$3"



echo -e "\n\n\n>>>matches in text files"
#grep $sText $sPath -nR --exclude=\*.jar
#grep $sText $sPath -nR | grep -v ".jar matches"
grep $sText $sPath -nR | grep -v " matches"



echo -e "\n\n\n>>>matches in jars"
$exeScriptPath/jar_grep.sh "$sPath" "$sFileName"
#$exeScriptPath/jar_grep.sh "$sPath" "$sFileName" "$sText"


echo -e "\n\n\n>>>matches in archives"
matchedArchiveList=$(find . -regex "$archiveTypeToMatch")
while read line; do
	#echo "  ${line}"
	absoluteArchivePath=$(realpath $line)
	. $exeScriptPath/rexpand.sh -a $absoluteArchivePath -s
	#grep $sFileName $tmpDir -nR
	grep $sFileName $tmpDir -nR | sed "s|^$tmpDir|$line|g" | sed 's|\[||g; s|\]||g'
	echo
done < <(echo "$matchedArchiveList")






exit 0











archiveList=$(find . -regex "$archiveTypeToMatch")


$exeScriptPath/rexpand.sh


archive="$1"
#new_archive="$2"
keyword="$2"






tmpdir=$(mktemp -d) 
cd "$tmpdir"

#tar -xaf "$OLDPWD/$archive" &&
tar -xaf "$archive" &&
if [ $? -eq 0 ]; then
	find . -regex "$archiveTypeToMatch" -print0 | rexpand
	if [ $? -eq 0 ]; then
		#tar -caf "$OLDPWD/$new_archive" *

		#grep $keyword . -nR

		#output=$(grep $keyword . -lR)
		#output=$(grep $keyword . -lR --include=\*.{cpp,h})
		#output=$(grep $keyword . -lR --exclude=\*.jar)
		#while read line; do echo "  ${line}"; done < <(echo "$output")
		#exit 0

		output=$(grep $keyword . -nR)
		if [ $? -eq 0 ]; then
			for out in grep $output; do
				if [[ $out == *"/"* ]]; then
					if [[ "$out" == *"jar" ]]; then
						sArchiveName="${out}"
						zipgrep "$sText" "$sArchiveName" 2>/dev/null | awk -F ':' '{print "	 "$2}'
					else
						echo $out
					fi
				fi
			done			
			cd -- "$OLDPWD"
			rm -rf $tmpdir
		else
			echo "parse output error"
		fi
	else
		echo "recursive expansion error"
	fi
else
	echo "source expansion error"
fi
