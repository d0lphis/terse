#!/bin/bash

h=$1
u=$2
s=$3
p=$4
expect -c 'exp_internal 1;spawn ssh -o "StrictHostKeyChecking no" -D '$p' -N -f '$u'@'$h'; expect *password*:; send "'$s'\n"; expect eof'
