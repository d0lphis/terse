#!/bin/sh

RED='\033[1;31m'
GREEN='\033[0;32m'
CYAN='\033[1;36m'
LIGHT_PURPLE='\033[1;35m'
NC='\033[0m'
STAT_FORMAT="%b%7s%b %-34s"

UPSTREAM=${1:-'@{u}'};
LOCAL=$(git rev-parse @);
REMOTE=$(git rev-parse "$UPSTREAM");
#if [ $? -ne 0 ]; then
#    git branch --set-upstream-to=upstream/$(git branch | sed -n -e 's/^\* \(.*\)/\1/p') $(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
#    REMOTE=$(git rev-parse "$UPSTREAM");
#fi
BASE=$(git merge-base @ "$UPSTREAM");

if [ "${LOCAL}" == "${REMOTE}" ]; then
    printf "${STAT_FORMAT}" "${GREEN}"        "✓" "${NC}" "Up to date"
elif [ "${LOCAL}" == "${BASE}" ]; then
    printf "${STAT_FORMAT}" "${LIGHT_PURPLE}" "▼" "${NC}" "others changes on upstream repo"
elif [ "${REMOTE}" == "${BASE}" ]; then
    printf "${STAT_FORMAT}" "${CYAN}"         "▲" "${NC}" "self changes committed to local repo"
else
    printf "${STAT_FORMAT}" "${RED}"          "✗" "${NC}" "Diverged"
fi
