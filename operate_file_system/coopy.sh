#!/bin/bash

# based on files in $1
# if existing in $2, create folder and copy files from $2 to $3
# if not existing in $2, create folder and copy files from $1 to $3
# if already existing in $3, skip without copy

#/coopy.sh /spark_trunk/impl/2.4.3_master/core /spark-3.0.0/core /spark_trunk/impl/3.0.0_master/core
#/coopy.sh /spark_trunk/impl/2.4.3_master/common /spark-3.0.0/common /spark_trunk/impl/3.0.0_master/common
#/coopy.sh /spark_trunk/impl/2.4.3_master/launcher /spark-3.0.0/launcher /spark_trunk/impl/3.0.0_master/launcher
#/coopy.sh /spark_trunk/impl/2.4.3_master/python /spark-3.0.0/python /spark_trunk/impl/3.0.0_master/python
#/coopy.sh /spark_trunk/impl/2.4.3_master/R /spark-3.0.0/R /spark_trunk/impl/3.0.0_master/R


function constructFile(){
    sourceFile=$1
    destFile=$2
    hint=$3
    destFileDir=$(dirname "$destFile")

    if [ ! -d "$destFileDir" ]; then
        mkdir -p "$destFileDir"
    fi

    if [ ! -f "$destFile" ]; then
        cp "$sourceFile" "$destFile" && echo [PASS] $hint $destFile copied || echo [FAIL] $hint $destFile not copied
    else
        echo [SKIP] $hint $destFile already existing
    fi
}


templateSrcPath=$1      #/spark_trunk/impl/2.4.3_master/core/src
openSrcPath=$2          #/spark-3.0.0/core/src
destSrcFolder=$3        #/spark_trunk/impl/3.0.0_master/core/src
#fileList=($(find "$templateSrcPath" -type f))

#echo "$fileList"  #first element
#for file in ${fileList[*]}
find $templateSrcPath -type f -print0 | while IFS= read -r -d '' file; do
    templateFile="$file"
    #sourceFile=${file/\/pc_ego-spark_trunk\/impl\/2.4.3_master\/core\/src/\/spark-3.0.0\/core\/src}
    sourceFile=$(echo "$file" | sed s@$templateSrcPath@$openSrcPath@)
    #echo $sourceFile
    destFile=$(echo "$file" | sed s@$templateSrcPath@$destSrcFolder@)
    destFileDir=$(dirname "$destFile")
    if [ ! -f "$sourceFile" ]; then
        constructFile "$templateFile" "$destFile" "self source"
    else
        constructFile "$sourceFile" "$destFile" "open source"
    fi
done