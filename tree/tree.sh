#!/bin/sh
# dtree: Usage: dtree [any directory]
dir=${1:-.}
(cd $dir; pwd)
#find $dir -type d -print | sort -f | sed -e "s,^$1,," -e "/^$/d" -e \
#"s,[^/]*/([^/]*)$,'----1,'" -e "s,[^/]*/, | ,g"
find $dir -type d -print | sort -f | sed -e "s,^$1,," -e "/^$/d" \
-e "s,[^/]*/([^/]*)$,----1," -e "s,[^/]*/,| ,g"

