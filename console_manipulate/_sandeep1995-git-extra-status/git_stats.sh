#!/usr/bin/env bash

RED='\033[1;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

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



cd $(dirname $0) && exeScriptPath=`pwd` && cd - > /dev/null
cwd=$PWD && base=$@ && if [ $# -eq 0 ]; then base="${cwd}"; fi

for repo in $base/*; do
    #echo REPO $repo
    repo=$($exeScriptPath/absolute_path.sh "$repo")
    #echo REPO $repo
    if [ -d "${repo}/.git" ]; then
        cd $repo
        #pwd

        #Execute "git fetch --prune upstream $BRANCH"
        #Execute "git fetch -q --prune upstream $BRANCH"

        GIT_STATUS=$($exeScriptPath/git_stat.sh)
        #echo $GIT_STATUS
        BARNCH_NAME=$(git rev-parse --abbrev-ref HEAD)
        if [[ -n $(git status --porcelain) ]]; then
            printf "\n%60s %40s %-30s %b%1s%b %-19s" "$(basename $repo)" "${BARNCH_NAME}" "${GIT_STATUS}" "${RED}" "x" "${NC}" "Uncommitted Changes"
        else

            #Execute "git rebase upstream/$BRANCH" \
            #&& Execute "git push --force-with-lease origin $BRANCH" \
            #|| break

            printf "\n%60s %40s %-30s"               "$(basename $repo)" "${BARNCH_NAME}" "${GIT_STATUS}"
        fi
        cd $cwd
    fi &
    sleep 0.000001
done
wait
echo -ne '\n\n'
