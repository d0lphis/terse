#!/bin/bash

#if two jars are different, ouptut diff
#if two jars are the same, ouptut nothing

a=$(unzip -l $1 | tr -s ' ' | cut -d ' ' -f 5 | sort | uniq);
b=$(unzip -l $2 | tr -s ' ' | cut -d ' ' -f 5 | sort | uniq);
diff <(echo "$a") <(echo "$b")
