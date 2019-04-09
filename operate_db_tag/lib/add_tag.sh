#!/bin/bash

. `dirname $0`/commonlib.sh

################################################
# Add a tag to db table.
# Globals:
#   Environment variable $DB_CONN with proper value for DB connection, e.g.
#    mysql -h${_db_host} -P${_db_port} -u${_db_user} --password=${_db_pwd} -D ${_db_base} -N -e 
# Arguments:
#   Tag name
#   Tag value
#   Tag type
# Returns:
#   None
################################################

# params validation
_script_name=$(basename $0)
_usage="
	Usage:\n\
		$_script_name [-h]\n\
		$_script_name tag_name tag_value [tag_type]"
if [ "$1" == "-h" ]; then
	echo -e $_usage
	exit 0
elif [ $# -lt 2 -o $# -gt 3 ]; then
	echo -e $_usage
	exit 1
fi

 _db_table_name="TAG"
_sql_clause=" \
	INSERT INTO $_db_table_name ( \
		TAG_NAME, \
		TAG_VAL, \
		TAG_TYPE, \
		TAG_CREATE_TIME \
	) \
	VALUES ('$1', '$2', '$3', NOW());"
ExecSQL "${_sql_clause}"
