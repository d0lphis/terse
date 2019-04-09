#!/bin/bash

. `dirname $0`/commonlib.sh

################################################
# Update tag value to db table.
# Globals:
#   Environment variable $DB_CONN with proper value for DB connection, e.g.
#    mysql -h${_db_host} -P${_db_port} -u${_db_user} --password=${_db_pwd} -D ${_db_base} -N -e 
# Arguments:
#   File id
#   Tag old name
#   Tag old value
#   Tag new name
#   Tag new value
# Returns:
#   None
################################################

# params validation
_script_name=$(basename $0)
_usage="
	Usage:\n\
		$_script_name [-h]\n\
		$_script_name file_id tag_old_name tag_old_value tag_new_name tag_new_value"
if [ "$1" == "-h" ]; then
	echo -e $_usage
	exit 0
elif [ $# -lt 5 -o $# -gt 5 ]; then
	echo -e $_usage
	exit 1
fi

_db_table_name1="TAG"
_db_table_name2="FILE_TAG"
_sql_clause=" \
	UPDATE \
		$_db_table_name2 AS FT, \
		(SELECT HEX(TAG_ID) AS T_ID FROM $_db_table_name1 WHERE TAG_NAME='$2' AND TAG_VAL='$3') AS T1, \
		(SELECT HEX(TAG_ID) AS T_ID FROM $_db_table_name1 WHERE TAG_NAME='$4' AND TAG_VAL='$5') AS T2 \
	SET FT.FILE_TAGS=TRIM(BOTH ',' FROM REPLACE(REPLACE(FT.FILE_TAGS, CONVERT(T1.T_ID, char), CONVERT(T2.T_ID, char)), ',,', ',')) \
	WHERE FT.FILE_ID='$1';"
# echo "${_sql_clause}" | sed 's/		/ /g' | sed 's/  / /g'
ExecSQL "${_sql_clause}"
AddLog \
	$1 \
	"`GetFile $1 "" JOB_ID`" \
	"`GetFile $1 "" FILE_TAGS`" \
	"`GetFile $1 "" FILE_USER`" \
	"`GetFile $1 "" FILE_PATH`" \
	"UPDATE"