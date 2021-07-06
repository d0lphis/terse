#!/bin/sh
# Usage: ./word_add_one.sh 'abc def' + 1
# Output: bcd!efg
# Usage: ./word_add_one.sh 'abc def' - 1
# Output: abc def

#word="abc"; for (( i=0; i<${#word}; i++ )); do char="${word:$i:1}" && ascii=$(LC_CTYPE=C printf '%d' "'$char") && printf "\\$(printf '%03o' "$(($ascii+1))")"; done

word=$1
for (( i=0; i<${#word}; i++ )); do
  char="${word:$i:1}"
  ascii=$(LC_CTYPE=C printf '%d' "'$char")
  if [ "$2" == "+" ]; then
    printf "\\$(printf '%03o' "$(($ascii+$3))")"
  elif [ "$2" == "-" ]; then
    printf "\\$(printf '%03o' "$(($ascii-$3))")"
  fi
done
echo
