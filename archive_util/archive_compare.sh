#!/bin/bash

#if two archives are different, ouptut diff, show the different message
#if two archives are the same, no diff, show the same message

echo $1
echo $2
if [[ ( $1 == *.jar ) && ( $2 == *.jar ) ]]; then
	echo "compare two zip files..."
	#a=$(unzip -l $1 | tr -s ' ' | cut -d ' ' -f 5 | uniq | sort);
	#b=$(unzip -l $2 | tr -s ' ' | cut -d ' ' -f 5 | uniq | sort);
	a=$(unzip -l $1 | awk '{print $4}' | uniq | sort);
	b=$(unzip -l $2 | awk '{print $4}' | uniq | sort);
	diff <(echo "$a") <(echo "$b")
elif [[ ( $1 == *.tar ) && ( $2 == *.tar ) ]]; then
	echo "compare two tar files..."
	a=$(tar -tvf $1 | awk '{print $9}' | uniq | sort);
	b=$(tar -tvf $2 | awk '{print $9}' | uniq | sort);
	diff <(echo "$a") <(echo "$b")
fi
if [ $? -eq 0 ]; then
	echo "two archives are the same"
else
	echo "two archives are different, refer above diff"
fi
