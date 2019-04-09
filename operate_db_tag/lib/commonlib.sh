#!/bin/bash

################################################
# Execute SQL clause.
# Globals:
#   DB connection string, e.g.
#    mysql -h${_db_host} -P${_db_port} -u${_db_user} --password=${_db_pwd} -D ${_db_base} -N -e 
# Arguments:
#   Sql clause.
# Returns:
#   None
# TODO: how to return mysql error?
################################################
function ExecSQL()
{
	if [ "$DB_CONN" == "" ]; then
		echo "Database connection string is required."
		return 1
	fi

	_sql="${DB_CONN}\"$1\""
	# echo ${_sql}
	eval "${_sql}"
}

################################################
# Concat string with separator
# Example:
#   ConcatWS WHERE TAG_NAME=\'Sn\' TAG_VAL=\'Tin\'
#   ConcatWS WHERE TAG_NAME=\'Sn\' TAG_VAL=\'Tin\' _tag_type=\'Metals\'
# Globals:
#   None
# Arguments:
#   SQL Keyword, e.g. WHERE
#   Condition field var value pair, e.g. TAG_NAME=\'Sn\' or TAG_ID=1
#   ...
# Returns:
#   None
################################################
function ConcatWS()
{
	# parameters validation
	if [ "$*" == "" ]; then
		echo "Params requried."
		return 1
	fi

	if [ x"$1" == x"$*" ]; then
		echo "Condition is required if keyword is specified."
		return 2
	fi

	echo "$1" | grep = > /dev/null
	if [ $? -eq 0 ]; then
		echo "First param(\"SQL Keyword\") $1 cannot be var value pair."
		return 3
	fi

	local i=1
	for var in "$@"
	do
		if [ $i -ne 1 ]; then
			echo "$var" | grep = > /dev/null
			if [ $? -ne 0 ]; then
				echo "Param $var must be var value pair."
				return 4
			fi
			echo "$var" | grep "^=" > /dev/null
			if [ $? -eq 0 ]; then
				echo "Param $var must be var value pair, var name is required if var value is specified."
				return 5
			fi
			echo "$var" | grep "=$" > /dev/null
			if [ $? -eq 0 ]; then
				echo "Param $var must be var value pair, var value is required if var name is specified."
				return 6
			fi
		fi

		i=`expr $i + 1`
	done



	local _condition=
	local i=1
	for var in "$@"
	do
		if [ $# -ge 2 ]; then
			if [ $i -eq 1 ]; then
				_condition="$1"
			else
				if [ "$var" != "" ]; then
					if [ $i -eq 2 ]; then
						_condition=$_condition" "$var
					else
						_condition=$_condition" AND "$var
					fi
				fi
			fi
		fi

		i=`expr $i + 1`
	done

	echo $_condition
	return 0
}

################################################
# Get tag(s) record.
# Example:
# GetTags "" "" TAG_NAME=\'Sn\' TAG_VAL=\'Tin\'
# GetTags TAG_ID HEX TAG_NAME=\'Sn\' TAG_VAL=\'Tin\' TAG_TYPE=\'Metals\'
# Globals:
#   None
# Arguments:
#   Query filed var name, e.g. "" for all fields, or TAG_ID
#   Numeral system(optional), e.g. "" for decimal, or HEX for hexadecimal
#   Condition field var value pair, e.g. TAG_NAME=\'Sn\' or TAG_ID=1
#   ...
# Returns:
#   None
################################################
function GetTags()
{
	local _db_table_name="TAG"

	# if no query field specified
	if [ x"$1" == x"" ]; then
		_query_field=\"*\"
	else
		_query_field=$1
	fi

	# if hex value is needed
	local _hex=false
	echo "$2" | grep HEX > /dev/null
	if [ $? -eq 0 ]; then
		_query_field="HEX($_query_field)"
		_hex=true
	fi

	_sql_clause=" \
		SELECT $_query_field FROM $_db_table_name"
	# remove first two params
	local _part_of_params=
	local i=1
	for var in "$@"
	do
		if [ $i -gt 2 ]; then
			_part_of_params=$_part_of_params" "$var
		fi

		i=`expr $i + 1`
	done
	_sql_clause=$_sql_clause" "`ConcatWS WHERE $_part_of_params`";"
	# echo "${_sql_clause}"

	ExecSQL "${_sql_clause}"

	# remove redudant string from hex value queried
	if [ $_hex ]; then
		echo $hex_id | sed 's/HEX(TAG_ID) //g'
	fi
}

################################################
# Get tag(s) id's hex value.
# Globals:
#   None
# Arguments:
#   Tag name(optional)
#   Tag value(optional)
#   Tag type(optional)
# Returns:
#   None
################################################
function GetTagHexID()
{
	local _tag_hex_id=`GetTags TAG_ID HEX TAG_NAME=\'$1\' TAG_VAL=\'$2\'`
	echo $_tag_hex_id
}










################################################
# Record file and it's properties to db table(with or without label).
# Globals:
#   None
# Arguments:
#   File id
#   Job id
#   User name
#   File full path
#   File tags
#   File size
#   File type
#   File mode
#   File last modified time
# Returns:
#   None
################################################
function AddFile()
{
	local _db_table_name="FILE_TAG"

	_sql_clause=" \
		INSERT INTO $_db_table_name ( \
			FILE_ID, \
			JOB_ID, \
			FILE_TAGS, \
			FILE_USER, \
			FILE_PATH, \
			FILE_SIZE, \
			FILE_TYPE, \
			FILE_MODE, \
			FILE_LAST_MOD_TIME, \
			TAG_FIRST_ACT_TIME, \
			TAG_LAST_ACT_TIME \
		) VALUES ('$1', $2, '$3', '$4', '$5', $6, '$7', '$8', '$9', NOW(), NOW());"
	# echo "${_sql_clause}"
	ExecSQL "${_sql_clause}"

	# AddLog $1 $2 $3 $4 $5 ${Actions[$CREATE]}
}

################################################
# Get tag(s) record.
# Globals:
#   None
# Arguments:
#   File id(optional)
#   File path(optional)
#   Field name(optional)
# Returns:
#   None
################################################
function GetFile()
{
	local _db_table_name="FILE_TAG"
	local _field_name=
	if [ "$3" == "" ]; then
		_field_name="*"
	else
		_field_name="$3"
	fi

	_sql_clause=" \
		SELECT \"$_field_name\" FROM $_db_table_name"
	if [ "$1" != "" -o "$2" != "" ]; then
		_sql_clause=$_sql_clause" WHERE"
		if [ "$1" != "" ]; then
			_sql_clause=$_sql_clause" FILE_ID='$1'"
			if [ "$2" != "" ]; then
				_sql_clause=$_sql_clause" AND"
			fi
		fi
		if [ "$2" != "" ]; then
			_sql_clause=$_sql_clause" FILE_PATH='$2'"
		fi
	fi
	_sql_clause=$_sql_clause";"
	# echo "${_sql_clause}"
	ExecSQL "${_sql_clause}"
}









################################################
# Add file tag actions as log to db table.
# Globals:
#   None
# Arguments:
#   File id
#   Job id
#   User name
#   File full path
#   File tags
#   Action type
#   File latest modified time
# Returns:
#   None
################################################
function AddLog()
{
	local _db_table_name="FILE_TAG_LOG"

	_sql_clause=" \
		INSERT INTO $_db_table_name ( \
			FILE_ID, \
			JOB_ID, \
			FILE_TAGS, \
			FILE_USER, \
			FILE_PATH, \
			ACT_TYPE, \
			ACT_TIME \
		) VALUES ('$1', $2, '$3', '$4', '$5', '$6', NOW());"
	# echo "${_sql_clause}"
	ExecSQL "${_sql_clause}"
}

################################################
# Get file tag(s) action record.
# Globals:
#   None
# Arguments:
#   File id(optional)
#   Field name(optional)
# Returns:
#   None
################################################
function GetLog()
{
	local _db_table_name="FILE_TAG_LOG"
	local _field_name=
	if [ "$2" == "" ]; then
		_field_name="*"
	else
		_field_name="$2"
	fi

	_sql_clause=" \
		SELECT \"$_field_name\" FROM $_db_table_name"
	if [ "$1" != "" ]; then
		_sql_clause=$_sql_clause" WHERE FILE_ID='$1'"
	fi
	_sql_clause=$_sql_clause";"
	# echo "${_sql_clause}"
	ExecSQL "${_sql_clause}"
}