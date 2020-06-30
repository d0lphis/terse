#!/bin/bash

function GrepInArchiveFileContent(){
	result=$(tar xf "$archive" "$1" -O | grep "$2")
	if [ $? == 0 ]; then
		echo "$1"
		while read line; do
			echo "  ${line}"
		done < <(echo "$result")
	fi	
}

archive="$1"
keyword="$2"
tar tf $archive | while read -r FILE; do
	if [[ -f $FILE ]]; then
		if ( file $FILE | grep -q compressed ); then
			echo "Nested archive $FILE detected."
			#TODO: recursively grep here
		else
			GrepInArchiveFileContent $FILE $keyword
		fi
	fi
done

