#!/bin/bash

#create nested archive(compressed tar ball in compressed tar bar)
#$ touch 1.txt
#$ cp 1.txt 2.txt
#$ cp 1.txt 3.txt
#$ tar -cvzf a.tar.gz 1.txt
#$ tar -cvzf b.tar.gz a.tar.gz 2.txt
#$ tar -cvzf c.tar.gz b.tar.gz 3.txt
#$ ls
#  1.txt  2.txt  3.txt  a.tar.gz  b.tar.gz  c.tar.gz

#recursively uncompress nested archive to tmp dir
#$ ./rexpand.sh c.tar.gz
#done: recursively extracted c.tar.gz to /tmp/tmp.Mwp9VjCoNH
#/tmp/tmp.Mwp9VjCoNH
#├── 3.txt
#└── [b.tar.gz]
#    ├── 2.txt
#    └── [a.tar.gz]
#        └── 1.txt
#2 directories, 3 files

#flatten nested archive
#$ ./rexpand.sh c.tar.gz d.tar.gz
#done: recursively extracted c.tar.gz to /tmp/tmp.Pna23LrwqD
#/tmp/tmp.Pna23LrwqD
#├── 3.txt
#└── [b.tar.gz]
#    ├── 2.txt
#    └── [a.tar.gz]
#        └── 1.txt
#2 directories, 3 files
#
#done: nested archive c.tar.gz flattened as d.tar.gz
#-rw-r--r-- root/root         0 0000-00-00 00:00 3.txt
#drwxr-sr-x root/root         0 0000-00-00 00:00 [b.tar.gz]/
#drwxr-sr-x root/root         0 0000-00-00 00:00 [b.tar.gz]/[a.tar.gz]/
#-rw-r--r-- root/root         0 0000-00-00 00:00 [b.tar.gz]/[a.tar.gz]/1.txt
#-rw-r--r-- root/root         0 0000-00-00 00:00 [b.tar.gz]/2.txt



cd `dirname $0` > /dev/null
exeScriptPath=`pwd`
cd - > /dev/null

. $exeScriptPath/lib/com.sh

function rexpand(){
        retval=0
        while read -rd '' path; do
                if [ -e "$path" ]; then
                        nested_archive=${path##*/}
                        #if cd "${path%/*}" && tar -xakf "$nested_archive"; then
			#archive_container=${nested_archive//\./_}
			archive_container="[${nested_archive}]"
                        if cd "${path%/*}" && mkdir "$archive_container" && tar -xakf "$nested_archive" -C "$archive_container"; then
                                rm "$nested_archive"
                                find . -regex "$archiveTypeToMatch" -print0 | rexpand
                                retval=$?
                        else
                                echo "Error extracting $nested_archive, not removing"
                                retval=1
                        fi
                fi
        done
        return $retval
}



#------Variables initialization
OPTS=`getopt -o a:b:s --long archive:,new-archive:,silent-mode -n 'parse-options' -- "$@"`
if [ $? != 0 ] ; then echo "Failed parsing options." >&2 ; exit 1 ; fi
#echo "$OPTS"
eval set -- "$OPTS"
while true; do
        case "$1" in
                -a | --archive ) ARCHIVE="$2"; shift; shift;;
                -b | --new-archive ) NEW_ARCHIVE="$2"; shift; shift;;
                -s | --silent-mode ) SILENT=true; shift;;
                -- ) shift; break;;
                * ) break;;
        esac
done



absoluteArchivePath=$(realpath $ARCHIVE)

tmpDir=$(mktemp -d) 
cd "$tmpDir"

#tar -xaf "$archive" &&
#	find . -regex "$archiveTypeToMatch" -print0 | rexpand &&
#	#tar -caf "$OLDPWD/$newArchive" * &&
#	grep $keyword . -nR &&
#	#result=$(grep $keyword . -nR) &&
#	#while read line; do echo "  ${line}"; done < <(echo "$result") &&
#	cd -- "$OLDPWD" &&
#	rm -rf $tmpdir ||
#	echo "Errors, please review $tmpdir"

tar -xaf "$absoluteArchivePath"
if [ $? -eq 0 ]; then
	find . -regex "$archiveTypeToMatch" -print0 | rexpand
	if [ $? -eq 0 ]; then
		if [ "$SILENT" != true ]; then
			echo "done: recursively extracted $archive to $tmpdir"
			tree $tmpdir
		fi
		if [ "$newArchive" != "" ]; then
			tar -caf "$OLDPWD/$newArchive" *
			if [ $? -eq 0 ]; then
				if [ "$SILENT" != true ]; then
					echo "done: nested archive $archive flattened as $newArchive"
				fi
				tar -tvf "$OLDPWD/$newArchive"
			else
				echo "error: flatten archive $newArchive creation failure, review $tmpdir"
			fi
			rm -rf $tmpdir
		fi
	else
		echo "error: recursively extraction for $archive failure, review $tmpdir"
	fi
else
	echo "error, provided package extraction failure"
fi

cd -- "$OLDPWD"
