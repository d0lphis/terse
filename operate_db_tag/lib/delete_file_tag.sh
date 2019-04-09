#!/bin/bash

. `dirname $0`/commonlib.sh

################################################
# Update tag value to db table.
# Globals:
#   Environment variable $DB_CONN with proper value for DB connection, e.g.
#    mysql -h${_db_host} -P${_db_port} -u${_db_user} --password=${_db_pwd} -D ${_db_base} -N -e 
# Arguments:
#   File id
#   Tag name
#   Tag value
# Returns:
#   None
################################################

# params validation
_script_name=$(basename $0)
_usage="
	Usage:\n\
		$_script_name [-h]\n\
		$_script_name file_id tag_name tag_value"
if [ "$1" == "-h" ]; then
	echo -e $_usage
	exit 0
elif [ $# -lt 3 -o $# -gt 3 ]; then
	echo -e $_usage
	exit 1
fi

_db_table_name1="TAG"
_db_table_name2="FILE_TAG"
_sql_clause=" \
	UPDATE \
		$_db_table_name2 AS FT, \
		(SELECT HEX(TAG_ID) AS T_ID FROM $_db_table_name1 WHERE TAG_NAME='$2' AND TAG_VAL='$3') AS T \
	SET FT.FILE_TAGS=TRIM(BOTH ',' FROM REPLACE(REPLACE(FT.FILE_TAGS, CONVERT(T.T_ID, char), ''), ',,', ',')) \
	WHERE FT.FILE_ID='$1';"
ExecSQL "${_sql_clause}"
AddLog \
	$1 \
	"`GetFile $1 "" JOB_ID`" \
	"`GetFile $1 "" FILE_TAGS`" \
	"`GetFile $1 "" FILE_USER`" \
	"`GetFile $1 "" FILE_PATH`" \
	"DELETE"