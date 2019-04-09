#!/bin/bash

. `dirname $0`/commonlib.sh

################################################
# Update tag value to db table.
# Globals:
#   Environment variable $DB_CONN with proper value for DB connection, e.g.
#    mysql -h${_db_host} -P${_db_port} -u${_db_user} --password=${_db_pwd} -D ${_db_base} -N -e 
# Arguments:
#   Tag name
#   Tag old value
#   Tag new value
# Returns:
#   None
################################################

# params validation
_script_name=$(basename $0)
_usage="
	Usage:\n\
		$_script_name [-h]\n\
		$_script_name tag_name tag_old_value tag_new_value"
if [ "$1" == "-h" ]; then
	echo -e $_usage
	exit 0
elif [ $# -lt 2 -o $# -gt 3 ]; then
	echo -e $_usage
	exit 1
fi

_db_table_name="TAG"
_sql_clause=" \
	UPDATE $_db_table_name \
	SET TAG_VAL='$3' \
	WHERE TAG_NAME='$1' AND TAG_VAL='$2';"
ExecSQL "${_sql_clause}"
