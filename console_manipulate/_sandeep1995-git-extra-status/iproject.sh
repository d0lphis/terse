#!/bin/bash

WHITE='\033[1;37m';					BOLD_WHITE='\033[1m'
RED='\033[0;31m'; 	LIGHT_RED='\033[1;31m'
GREEN='\033[0;32m';	LIGHT_GREEN='\033[1;32m';	BOLD_GREEN='\033[1m\033[32m';
BLUE='\033[0;34m';	LIGHT_BLUE='\033[1;34m';	BOLD_BLUE='\033[1m\033[34m';
RESET='\033[0m';

while true; do
    printf "\r${WHITE} this is hint" && sleep 0.2
    printf "\r${LIGHT_BLUE} this is hint" && sleep 0.2
done
exit

TABLE_FORMAT="\n%b %60s %b %30s %b %40s %b %10s %b %20s %b\n"

function Execute()
{
   action=$(echo "$1" | cut -d ' ' -f2)
   printf "\n>>> $1\n"
   eval "$1"
   resCode=$?
   if [ $resCode == 0 ]; then
       ACTION_SYMBOL="$action success"
   else
       ACTION_SYMBOL="$action failure"
   fi
   return $resCode
}

IDENTIFY_SYMBOL="?"	#means the component in folder identified
ACTION_SYMBOL="?"	#means git action result status



handleCount=${1:-30}
i=1
for PROJECT_ROOT in */ ; do
    if [ $i -gt $handleCount ]; then
        exit
    else
        printf '%.s-' {1..180}
        printf "\nhandle the ${i}st project\n"
        i=$(($i+1))
    fi
    #sleep 1

    printf "\n>>> pushd ${PROJECT_ROOT}\n"
    pushd ${PROJECT_ROOT} > /dev/null

    PROJECT=$(ls | grep -E '^(asc|chronicle|conductor_gui|conductorspark_core|conductorspark_gui|cuf50|cuf|ego|elk|emm|gmf|gui|hf|install|libvemlsf|perf|pmc|rest|smc|soam|spark|testgrid|testgrid_suite|yarn)$')
    if [ $? == 0 ]; then
        IDENTIFY_SYMBOL="located"

        BRANCH=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')

        Execute "git fetch --prune upstream $BRANCH" \
        && Execute "git rebase upstream/$BRANCH" \
        && Execute "git push --force-with-lease origin $BRANCH" \
        || break

        STATUS_COLOR=$(echo ${ACTION_SYMBOL} | grep success 2>&1 > /dev/null && echo ${LIGHT_GREEN} || echo ${LIGHT_RED})

        printf "${TABLE_FORMAT}" "${BOLD_WHITE}" "FOLDER"          ""              "PROJECT"      ""              "BRANCH"    ""         "COMPONENT"          ""                "STATUS"           "${RESET}"
        printf "${TABLE_FORMAT}" "${WHITE}"      "${PROJECT_ROOT}" "${LIGHT_BLUE}" "${COMPONENT}" "${LIGHT_BLUE}" "${BRANCH}" "${GREEN}" "${IDENTIFY_SYMBOL}" "${STATUS_COLOR}" "${ACTION_SYMBOL}" "${RESET}"
        #case $PROJECT in
        #    asc)
        #        BRANCH=
        #        ;;
        #    PATTERN_1)
        #        STATEMENTS
        #        ;;
        #     *)
        #        STATEMENTS
        #        ;;
        #esac
    else
        printf "${TABLE_FORMAT}" "${LIGHT_RED}" "${PROJECT_ROOT}" "" "${COMPONENT}" "" "${BRANCH}" "" "${IDENTIFY_SYMBOL}" "" "${ACTION_SYMBOL}" "${RESET}"
    fi


    #printf ">>> exiting ${PROJECT_ROOT}\n"
    popd > /dev/null
done
