#!/bin/bash

################################################
# Generate files for analysis.
# Globals:
#   None
# Arguments:
#   Folder name to contains generated files.
# Returns:
#   None
################################################
function GenerateData()
{
	local current_path=`pwd`"/"
	local data_folder=$1
	if [ ! -d "$current_path$data_folder" ]; then
		mkdir -p $current_path$data_folder
		chmod 777 $current_path$data_folder
	fi

	local i=1
	until [ ! $i -le 3 ]
	do
		sudo su -c "echo info > $current_path$data_folder$i.$2" -s /bin/sh $3
		sudo su -c "chmod $4 $current_path$data_folder$i.$2" -s /bin/sh root

		i=`expr $i + 1`
	done
}

################################################
# Verrify test result: 0 PASS, other FAIL.
# Globals:
#   None
# Arguments:
#   Previous command exit code.
#   Expected exit code.
# Returns:
#   None
################################################
function Verify()
{
	if [ "$1" == "$2" ]; then
		echo -e "[TEST PASS]"
	else
		echo -e "[TEST FAIL]"
	fi
}

################################################
# Create database and tables.
# Globals:
#   None
# Arguments:
#   None
# Returns:
#   None
################################################
function CreateDB()
{
	_sql_clause="DROP DATABASE IF EXISTS $_db_base;"
	_sql_clause=" \
		${_sql_clause} \
		CREATE DATABASE IF NOT EXISTS $_db_base; \

		USE $_db_base; \
		CREATE TABLE TAG\
		( \
			TAG_ID				INT			NOT NULL	AUTO_INCREMENT, \
			TAG_NAME			VARCHAR(64)	NOT NULL, \
			TAG_VAL				VARCHAR(64)	NOT NULL, \
			TAG_TYPE			VARCHAR(64)	NOT NULL, \
			TAG_CREATE_TIME		DATETIME	NOT NULL, \
			PRIMARY KEY (TAG_ID) \
		) ENGINE=InnoDB; \
		ALTER TABLE TAG ADD UNIQUE (TAG_NAME, TAG_VAL); \

		CREATE TABLE FILE_TAG \
		( \
			FILE_ID				VARCHAR(64)		NOT NULL, \
			JOB_ID				NUMERIC(15)		NOT NULL, \
			FILE_TAGS			VARCHAR(1024)	NOT NULL, \
			FILE_USER			VARCHAR(64)		NOT NULL, \
			FILE_PATH			VARCHAR(1024)	NOT NULL, \
			FILE_SIZE			NUMERIC(15)		NOT NULL, \
			FILE_TYPE			VARCHAR(64)		NOT NULL, \
			FILE_MODE			VARCHAR(64)		NOT NULL, \
			FILE_LAST_MOD_TIME	VARCHAR(32)		NOT NULL, \
			TAG_FIRST_ACT_TIME	DATETIME		NOT NULL, \
			TAG_LAST_ACT_TIME	DATETIME		NOT NULL, \
			PRIMARY KEY (FILE_ID) \
		) ENGINE=InnoDB; \

		CREATE TABLE FILE_TAG_LOG \
		( \
			LOG_ID		INT				NOT NULL	AUTO_INCREMENT, \
			FILE_ID		VARCHAR(64)		NOT NULL, \
			JOB_ID		NUMERIC(15)		NOT NULL, \
			FILE_TAGS	VARCHAR(1204)	NOT NULL, \
			FILE_USER	VARCHAR(64)		NOT NULL, \
			FILE_PATH	VARCHAR(1024)	NOT NULL, \
			ACT_TYPE	VARCHAR(32)		NOT NULL, \
			ACT_TIME	DATETIME		NOT NULL, \
			PRIMARY KEY (LOG_ID) \
		) ENGINE=InnoDB; \

		SHOW TABLES;"
	ExecSQL "${_sql_clause}"
}






################################################
# Generate several sub folder and files for test.
# Globals:
#   None
# Arguments:
#   Test data spec array.
# Returns:
#   None
################################################
function InitialData()
{
	local arr=($1)
	local arr_size=${#arr[@]}

	local i=0
	until [ ! $i -lt $arr_size ]
	do
		# echo "${arr[$i]}"
		local path=`echo "${arr[$i]}" | cut -d "," -f1`
		local suffix=`echo "${arr[$i]}" | cut -d "," -f2`
		local un=`echo "${arr[$i]}" | cut -d "," -f3`
		local mod=`echo "${arr[$i]}" | cut -d "," -f4`

		GenerateData "$path" "$suffix" "$un" "$mod"

		i=`expr $i + 1`
	done
}

################################################
# Add several tags info to db for test.
# Globals:
#   None
# Arguments:
#   Test tags spec array.
# Returns:
#   None
################################################
function InitialTags()
{
	local arr=($1)
	local arr_size=${#arr[@]}

	local i=0
	until [ ! $i -lt $arr_size ]
	do
		# echo "${arr[$i]}"
		local name=`echo "${arr[$i]}" | cut -d "," -f1`
		local value=`echo "${arr[$i]}" | cut -d "," -f2`
		local typ=`echo "${arr[$i]}" | cut -d "," -f3`

		$SCRIPT_LIB_PATH/add_tag.sh "$name" "$value" "$typ"

		i=`expr $i + 1`
	done
}

########################################
# Add relation between tags and file into db.
# Globals:
#   None
# Arguments:
#   File absolute path, e.g. /opt/data/1.tst
#   Tag names
# Returns:
#   None
#######################################
function InitialFiles()
{
	for file in $(find $1 -maxdepth 50 -type f)
	do
		if [ ! -d "$file" ]; then
			# echo $file

			local file_id=`echo -n $file | md5sum | sed -e 's/ //g' | sed -e 's/-//g'`

			local job_id=`date +%N | sed s/....//`

			local file_USER=`stat -c '%U' $file`

			local file_path="$file"

			local file_tags=
			if [ "$2" != "" ]; then
				local arr=($2)
				local arr_size=${#arr[@]}
				local radom_serial=`echo $((RANDOM%11))`
				local i=1
				until [ ! $i -lt $arr_size ]
				do
					# todo
					local tag_name=`echo "${arr[$i]}" | cut -d "," -f1`
					# echo $tag_name

					local _tag_hex_id=`GetTagHexID $tag_name`
					if [ "$_tag_hex_id" != "" ]; then
						echo $file_tags | grep $_tag_hex_id > /dev/null
						if [ $? -ne 0 ]; then
							local file_tags=$file_tags","$_tag_hex_id
						fi
					fi
					# echo $file_tags

					i=`echo $((RANDOM%21))`
					i=`expr $i + 1`
					# echo $i
				done
			fi
			file_tags=`echo $file_tags | sed 's/,,/,/g' | sed 's/^,//g'| sed 's/,$//g'`

			local file_size=`stat --printf="%s" $file`

			local file_type="${file##*.}"

			# local file_mod=`stat -c "%a %n" $file | awk '{print $1}'`
			local file_mod=`ls -l $file | awk '{print $1}'`

			local file_last_modified_time=`stat -c %y $file | cut -d "." -f1`

			AddFile	"$file_id" "$job_id" "$file_tags" "$file_USER" \
					"$file_path" "$file_size" "$file_type" "$file_mod" \
					"$file_last_modified_time"
		fi
	done
}








