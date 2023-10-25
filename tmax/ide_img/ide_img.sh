#!/bin/sh

# USAGE: build ide image based on danchitnis/xrdp image

port=33890
netstat -alnp|grep $port
if [ $? -eq 0 ]; then
  echo "Make sure $port is not occupied, ide container will be launched on it."
fi

dockerBin=
(which docker > /dev/null) 2> /dev/null
if [ $? -eq 0 ]; then
  dockerBin=docker
fi
(which podman > /dev/null) 2> /dev/null
if [ $? -eq 0 ]; then
  dockerBin=podman
fi
if [ -z "$dockerBin" ]; then
  echo "Dcoker is required."
  exit
fi



cd `dirname $0`
exeScriptPath=`pwd`
cd -
cd $exeScriptPath/build/

timestamp=$(date +%Y_$m_%d_%H_%M_%S_%N)

buildImgCmd="$dockerBin build --no-cache -t docker.io/dal0s/ide:ubuntu-xfce-compiler-dev-$timestamp -f Dockerfile.ubuntu.xfce.ide ."
eval $buildImgCmd

runImgCmd="$dockerBin run -dt --privileged=true -v /usr/wks:/usr/wks:rw -p $port:3389 --shm-size=8G docker.io/dal0s/ide:ubuntu-xfce-compiler-dev-$timestamp pharo jinzix yes"
eval $runImgCmd

